from flask import Flask, render_template, request, redirect, url_for
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import re

app = Flask(__name__)

# Allowed hosts - default to localhost for safety
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Simple payloads
XSS_PAYLOAD = "<script>alert('XSS')</script>"
SQLI_PAYLOADS = ["' OR '1'='1", '" OR "1"="1', "' OR 1=1--"]

# Simple SQL error signatures
SQL_ERRORS = [r"SQL syntax", r"mysql", r"syntax error", r"ORA-", r"unknown column"]

results_store = []

def is_allowed(url):
    try:
        host = urlparse(url).hostname
        return host in ALLOWED_HOSTS or host is None
    except Exception:
        return False

def get_internal_links(base_url, html):
    soup = BeautifulSoup(html, 'html.parser')
    links = set()
    for a in soup.find_all('a', href=True):
        href = urljoin(base_url, a['href'])
        if urlparse(href).hostname == urlparse(base_url).hostname:
            links.add(href)
    return links

def find_forms(html, base_url):
    soup = BeautifulSoup(html, 'html.parser')
    forms = []
    for form in soup.find_all('form'):
        action = form.get('action') or base_url
        method = form.get('method', 'get').lower()
        inputs = []
        for inp in form.find_all(['input', 'textarea']):
            name = inp.get('name')
            itype = inp.get('type', 'text')
            inputs.append({'name': name, 'type': itype})
        forms.append({'action': urljoin(base_url, action), 'method': method, 'inputs': inputs})
    return forms

def test_xss(session, url, form=None):
    evidence = None
    try:
        if form:
            data = {}
            for inp in form['inputs']:
                if not inp['name']:
                    continue
                data[inp['name']] = XSS_PAYLOAD
            if form['method'] == 'post':
                r = session.post(form['action'], data=data, timeout=10)
            else:
                r = session.get(form['action'], params=data, timeout=10)
            if XSS_PAYLOAD in r.text:
                evidence = f"Payload reflected in response at {form['action']}"
        else:
            r = session.get(url, timeout=10)
            if XSS_PAYLOAD in r.text:
                evidence = f"Payload reflected in page at {url}"
    except Exception as e:
        evidence = f"Error during XSS test: {e}"
    return evidence

def test_sqli(session, url, param=None):
    evidence = None
    try:
        if param:
            for payload in SQLI_PAYLOADS:
                params = {param: payload}
                r = session.get(url, params=params, timeout=10)
                for sig in SQL_ERRORS:
                    if re.search(sig, r.text, re.IGNORECASE):
                        evidence = f"SQL error signature '{sig}' found with payload {payload}"
                        return evidence
        else:
            for payload in SQLI_PAYLOADS:
                test_url = url + payload
                r = session.get(test_url, timeout=10)
                for sig in SQL_ERRORS:
                    if re.search(sig, r.text, re.IGNORECASE):
                        evidence = f"SQL error signature '{sig}' found at {test_url}"
                        return evidence
    except Exception as e:
        evidence = f"Error during SQLi test: {e}"
    return evidence

def test_csrf(form):
    # Check for common anti-CSRF hidden inputs
    has_token = False
    for inp in form['inputs']:
        if inp['type'] == 'hidden' and inp['name'] and ('csrf' in inp['name'].lower() or 'token' in inp['name'].lower()):
            has_token = True
    if not has_token:
        return "No CSRF token field detected in form"
    return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        target = request.form.get('target')
        # sanitize and ensure allowed
        if not is_allowed(target):
            return render_template('index.html', error='Target host not allowed. For safety, only localhost targets are allowed by default.')
        depth = int(request.form.get('depth', 2))
        results_store.clear()
        run_scan(target, depth)
        return redirect(url_for('results'))
    return render_template('index.html')

@app.route('/results')
def results():
    return render_template('results.html', results=results_store)

def run_scan(start_url, depth=2):
    session = requests.Session()
    to_crawl = {start_url}
    crawled = set()
    for current_depth in range(depth):
        next_round = set()
        for url in to_crawl:
            if url in crawled:
                continue
            try:
                r = session.get(url, timeout=10)
                crawled.add(url)
                links = get_internal_links(url, r.text)
                for l in links:
                    if l not in crawled:
                        next_round.add(l)
                # analyze forms
                forms = find_forms(r.text, url)
                for f in forms:
                    # CSRF
                    csrf = test_csrf(f)
                    if csrf:
                        results_store.append({'type': 'CSRF', 'severity': 'Medium', 'url': f['action'], 'evidence': csrf})
                    # XSS
                    xss = test_xss(session, url, form=f)
                    if xss:
                        results_store.append({'type': 'XSS', 'severity': 'High', 'url': f['action'], 'evidence': xss})
                # test XSS on page
                xss_page = test_xss(session, url, form=None)
                if xss_page:
                    results_store.append({'type': 'XSS', 'severity': 'High', 'url': url, 'evidence': xss_page})
                # test SQLi on query params if present
                parsed = urlparse(url)
                if parsed.query:
                    params = dict([part.split('=') for part in parsed.query.split('&') if '=' in part])
                    if params:
                        p = list(params.keys())[0]
                        sqli = test_sqli(session, url, param=p)
                        if sqli:
                            results_store.append({'type': 'SQLi', 'severity': 'High', 'url': url, 'evidence': sqli})
            except Exception as e:
                results_store.append({'type': 'ERROR', 'severity': 'Low', 'url': url, 'evidence': str(e)})
        to_crawl = next_round

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
