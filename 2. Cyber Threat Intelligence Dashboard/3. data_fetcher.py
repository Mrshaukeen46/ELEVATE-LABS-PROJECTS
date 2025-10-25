import requests
from datetime import datetime
from models import threats_collection, trends_collection
from config import VIRUSTOTAL_API_KEY, ABUSEIPDB_API_KEY

def fetch_virustotal_data(ip_or_domain):
    url = f'https://www.virustotal.com/api/v3/ip_addresses/{ip_or_domain}' if '.' in ip_or_domain and ip_or_domain.count('.') == 3 else f'https://www.virustotal.com/api/v3/domains/{ip_or_domain}'
    headers = {'x-apikey': VIRUSTOTAL_API_KEY}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        malicious = data['data']['attributes']['last_analysis_stats']['malicious']
        threat_level = 'High' if malicious > 5 else 'Medium' if malicious > 0 else 'Low'
        return {
            'ioc': ip_or_domain,
            'source': 'VirusTotal',
            'threat_level': threat_level,
            'details': data['data']['attributes'],
            'timestamp': datetime.utcnow()
        }
    return None

def fetch_abuseipdb_data(ip):
    url = f'https://api.abuseipdb.com/api/v2/check?ipAddress={ip}'
    headers = {'Key': ABUSEIPDB_API_KEY, 'Accept': 'application/json'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        abuse_score = data['data']['abuseConfidenceScore']
        threat_level = 'High' if abuse_score > 50 else 'Medium' if abuse_score > 10 else 'Low'
        return {
            'ioc': ip,
            'source': 'AbuseIPDB',
            'threat_level': threat_level,
            'details': data['data'],
            'timestamp': datetime.utcnow()
        }
    return None

def aggregate_threats():
    # Example: Pull for a list of known IOCs (extend with open CTI sources like MISP or STIX feeds)
    sample_iocs = ['8.8.8.8', 'malicious.com']  # Replace with real feeds
    for ioc in sample_iocs:
        vt_data = fetch_virustotal_data(ioc)
        if vt_data:
            threats_collection.insert_one(vt_data)
            trends_collection.insert_one({'ioc': ioc, 'threat_level': vt_data['threat_level'], 'timestamp': vt_data['timestamp']})
        if '.' in ioc and ioc.count('.') == 3:  # IP only for AbuseIPDB
            ab_data = fetch_abuseipdb_data(ioc)
            if ab_data:
                threats_collection.insert_one(ab_data)
                trends_collection.insert_one({'ioc': ioc, 'threat_level': ab_data['threat_level'], 'timestamp': ab_data['timestamp']})
