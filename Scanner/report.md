```markdown
# Web Vulnerability Scanner — Project Report

Introduction
This project builds a small Python-based web application scanner for educational use. It targets common web vulnerabilities (XSS, SQLi, CSRF) by crawling pages, enumerating forms, injecting basic payloads, and flagging potential issues.

Abstract
A minimal scanner (Flask UI) demonstrates automated discovery and testing techniques. It uses requests + BeautifulSoup to crawl and find inputs, injects payloads for XSS/SQLi, and inspects responses for evidence. Results are shown in a simple web UI and logged with severity.

Tools Used
- Python 3.x
- Flask (UI)
- requests (HTTP client)
- BeautifulSoup (HTML parsing)

Steps Involved in Building the Project
1. Crawler: Use requests to fetch pages and BeautifulSoup to parse links/forms and build an internal link set.
2. Form enumeration: Extract form actions, methods, and input names to identify injection points.
3. Payloads & tests:
   - XSS: inject a JavaScript payload into form fields and check if it appears in responses.
   - SQLi: inject common SQL error payloads and search responses for database error signatures.
   - CSRF: inspect forms for hidden token fields (names containing csrf/token).
4. UI: Build a Flask frontend to start scans and show results. Restrict scans to localhost by default for safety.
5. Reporting: Log findings with type, severity, URL, and evidence strings for each alert.

Conclusion
This lightweight scanner demonstrates the core workflow of automated web vulnerability scanning and reporting. It is intended for local test targets (Juice Shop, DVWA) and as a learning tool rather than a production-grade scanner. Future enhancements include authenticated scanning, stronger payload sets, timing-based tests, and more robust fingerprinting to reduce false positives.
