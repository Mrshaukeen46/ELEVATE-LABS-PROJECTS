🧠 Project: Cyber Threat Intelligence Dashboard

Goal: Build a real-time dashboard that aggregates open-source threat intelligence data (IPs, domains, URLs) from public APIs like VirusTotal, AbuseIPDB, and AlienVault OTX.

⚙️ Step 1 — Setup Environment
🖥️ Install Requirements

Open a terminal or command prompt and run:

# 1. Unzip project
unzip cti_dashboard.zip
cd cti_dashboard

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate   # (Windows)
# or
source venv/bin/activate  # (Linux/Mac)

# 3. Install dependencies
pip install flask requests pymongo

🔑 Step 2 — (Optional) Configure API Keys

Set your API keys to fetch live threat data.
If you don’t have them, you can skip this — the dashboard will still run in demo mode.

# Example (replace with your own keys)
set VIRUSTOTAL_API_KEY=your_key
set ABUSEIPDB_API_KEY=your_key
set OTX_API_KEY=your_key

🚀 Step 3 — Run the Flask App
python app.py


Output will look like:

* Running on http://127.0.0.1:5100


Now open this URL in your browser:
👉 http://127.0.0.1:5100

🕵️ Step 4 — Using the Dashboard
🔍 Lookup Example

In the web form, enter:

8.8.8.8


and select IP Address, then click Lookup.

The dashboard will:

Query AbuseIPDB and VirusTotal (if API keys provided)

Display the JSON threat info in your browser

Store the lookup result for export

📋 View Recent Lookups

Scroll down on the home page — you’ll see:

Recent Lookups:
• 8.8.8.8 - web-ui
• example.com - demo

💾 Export Data

Download recent lookup history:

http://127.0.0.1:5100/export/recent


It returns a JSON file with all recent lookups.

📊 Step 5 — Visual Demo Screenshots

To include in your submission:

Step	Screenshot Description
1	Terminal showing python app.py running
2	Browser with CTI Dashboard form
3	Lookup result (JSON output for IP/domain)
4	Recent Lookups list
5	Exported JSON download (recent lookups)
🧩 Step 6 — Files for Submission
File	Description
app.py	Flask app source code
api_clients.py	API helper file
project_report.pdf	2-page report ready for submission
README.md	Setup & usage instructions
sample_export.json	Example data
🏁 Step 7 — Report Submission

Submit project_report.pdf along with your screenshots and ZIP file as your final project deliverable.🧠 Project: Cyber Threat Intelligence Dashboard

Goal: Build a real-time dashboard that aggregates open-source threat intelligence data (IPs, domains, URLs) from public APIs like VirusTotal, AbuseIPDB, and AlienVault OTX.

⚙️ Step 1 — Setup Environment
🖥️ Install Requirements

Open a terminal or command prompt and run:

# 1. Unzip project
unzip cti_dashboard.zip
cd cti_dashboard

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate   # (Windows)
# or
source venv/bin/activate  # (Linux/Mac)

# 3. Install dependencies
pip install flask requests pymongo

🔑 Step 2 — (Optional) Configure API Keys

Set your API keys to fetch live threat data.
If you don’t have them, you can skip this — the dashboard will still run in demo mode.

# Example (replace with your own keys)
set VIRUSTOTAL_API_KEY=your_key
set ABUSEIPDB_API_KEY=your_key
set OTX_API_KEY=your_key

🚀 Step 3 — Run the Flask App
python app.py


Output will look like:

* Running on http://127.0.0.1:5100


Now open this URL in your browser:
👉 http://127.0.0.1:5100

🕵️ Step 4 — Using the Dashboard
🔍 Lookup Example

In the web form, enter:

8.8.8.8


and select IP Address, then click Lookup.

The dashboard will:

Query AbuseIPDB and VirusTotal (if API keys provided)

Display the JSON threat info in your browser

Store the lookup result for export

📋 View Recent Lookups

Scroll down on the home page — you’ll see:

Recent Lookups:
• 8.8.8.8 - web-ui
• example.com - demo

💾 Export Data

Download recent lookup history:

http://127.0.0.1:5100/export/recent


It returns a JSON file with all recent lookups.

📊 Step 5 — Visual Demo Screenshots

To include in your submission:

Step	Screenshot Description
1	Terminal showing python app.py running
2	Browser with CTI Dashboard form
3	Lookup result (JSON output for IP/domain)
4	Recent Lookups list
5	Exported JSON download (recent lookups)
🧩 Step 6 — Files for Submission
File	Description
app.py	Flask app source code
api_clients.py	API helper file
project_report.pdf	2-page report ready for submission
README.md	Setup & usage instructions
sample_export.json	Example data
🏁 Step 7 — Report Submission

Submit project_report.pdf along with your screenshots and ZIP file as your final project deliverable.🧠 Project: Cyber Threat Intelligence Dashboard

Goal: Build a real-time dashboard that aggregates open-source threat intelligence data (IPs, domains, URLs) from public APIs like VirusTotal, AbuseIPDB, and AlienVault OTX.

⚙️ Step 1 — Setup Environment
🖥️ Install Requirements

Open a terminal or command prompt and run:

# 1. Unzip project
unzip cti_dashboard.zip
cd cti_dashboard

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate   # (Windows)
# or
source venv/bin/activate  # (Linux/Mac)

# 3. Install dependencies
pip install flask requests pymongo

🔑 Step 2 — (Optional) Configure API Keys

Set your API keys to fetch live threat data.
If you don’t have them, you can skip this — the dashboard will still run in demo mode.

# Example (replace with your own keys)
set VIRUSTOTAL_API_KEY=your_key
set ABUSEIPDB_API_KEY=your_key
set OTX_API_KEY=your_key

🚀 Step 3 — Run the Flask App
python app.py


Output will look like:

* Running on http://127.0.0.1:5100


Now open this URL in your browser:
👉 http://127.0.0.1:5100

🕵️ Step 4 — Using the Dashboard
🔍 Lookup Example

In the web form, enter:

8.8.8.8


and select IP Address, then click Lookup.

The dashboard will:

Query AbuseIPDB and VirusTotal (if API keys provided)

Display the JSON threat info in your browser

Store the lookup result for export

📋 View Recent Lookups

Scroll down on the home page — you’ll see:

Recent Lookups:
• 8.8.8.8 - web-ui
• example.com - demo

💾 Export Data

Download recent lookup history:

http://127.0.0.1:5100/export/recent


It returns a JSON file with all recent lookups.

📊 Step 5 — Visual Demo Screenshots

To include in your submission:

Step	Screenshot Description
1	Terminal showing python app.py running
2	Browser with CTI Dashboard form
3	Lookup result (JSON output for IP/domain)
4	Recent Lookups list
5	Exported JSON download (recent lookups)
🧩 Step 6 — Files for Submission
File	Description
app.py	Flask app source code
api_clients.py	API helper file
project_report.pdf	2-page report ready for submission
README.md	Setup & usage instructions
sample_export.json	Example data
🏁 Step 7 — Report Submission

Submit project_report.pdf along with your screenshots and ZIP file as your final project deliverable.🧠 Project: Cyber Threat Intelligence Dashboard

Goal: Build a real-time dashboard that aggregates open-source threat intelligence data (IPs, domains, URLs) from public APIs like VirusTotal, AbuseIPDB, and AlienVault OTX.

⚙️ Step 1 — Setup Environment
🖥️ Install Requirements

Open a terminal or command prompt and run:

# 1. Unzip project
unzip cti_dashboard.zip
cd cti_dashboard

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate   # (Windows)
# or
source venv/bin/activate  # (Linux/Mac)

# 3. Install dependencies
pip install flask requests pymongo

🔑 Step 2 — (Optional) Configure API Keys

Set your API keys to fetch live threat data.
If you don’t have them, you can skip this — the dashboard will still run in demo mode.

# Example (replace with your own keys)
set VIRUSTOTAL_API_KEY=your_key
set ABUSEIPDB_API_KEY=your_key
set OTX_API_KEY=your_key

🚀 Step 3 — Run the Flask App
python app.py


Output will look like:

* Running on http://127.0.0.1:5100


Now open this URL in your browser:
👉 http://127.0.0.1:5100

🕵️ Step 4 — Using the Dashboard
🔍 Lookup Example

In the web form, enter:

8.8.8.8


and select IP Address, then click Lookup.

The dashboard will:

Query AbuseIPDB and VirusTotal (if API keys provided)

Display the JSON threat info in your browser

Store the lookup result for export

📋 View Recent Lookups

Scroll down on the home page — you’ll see:

Recent Lookups:
• 8.8.8.8 - web-ui
• example.com - demo

💾 Export Data

Download recent lookup history:

http://127.0.0.1:5100/export/recent


It returns a JSON file with all recent lookups.

📊 Step 5 — Visual Demo Screenshots

To include in your submission:

Step	Screenshot Description
1	Terminal showing python app.py running
2	Browser with CTI Dashboard form
3	Lookup result (JSON output for IP/domain)
4	Recent Lookups list
5	Exported JSON download (recent lookups)
🧩 Step 6 — Files for Submission
File	Description
app.py	Flask app source code
api_clients.py	API helper file
project_report.pdf	2-page report ready for submission
README.md	Setup & usage instructions
sample_export.json	Example data
🏁 Step 7 — Report Submission

Submit project_report.pdf along with your screenshots and ZIP file as your final project deliverable.
