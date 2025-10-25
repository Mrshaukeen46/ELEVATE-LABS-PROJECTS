🧠 Project: Cyber Threat Intelligence Dashboard

Cyber Threat Intelligence Dashboard project. I've chosen Flask as the web framework (over Django) for its simplicity and lightweight nature, making it suitable for a dashboard prototype. The implementation includes:

Full code: Python scripts, HTML templates, JavaScript for visualizations, and configuration files. All code is provided in a structured format that can be copied into files and run locally.
Assumptions and Setup Instructions: To run this, you'll need API keys for VirusTotal (free tier) and AbuseIPDB (free tier). Install dependencies via pip install flask pymongo requests plotly. Use a local MongoDB instance (install via MongoDB Community Server) or a cloud one like MongoDB Atlas. For real-time aspects, data is pulled on-demand or via a background scheduler (using APScheduler).
Features Implemented:
Pulls data from VirusTotal and AbuseIPDB APIs.
Displays threat levels, IOCs (e.g., IPs, domains), and trends.
User input for IP/domain verification.
Visualizations using Plotly (e.g., threat score trends over time).
Tagging (add custom tags to IOCs) and export (to CSV/JSON).
Real-time aggregation via periodic API pulls (every 10 minutes using APScheduler).
Limitations: Free API tiers have rate limits (e.g., VirusTotal: 4 requests/minute). Visualizations are basic; expand with more data sources for production. No authentication added for simplicity.


How to Run
Set up MongoDB and add API keys in config.py.
Run pip install -r requirements.txt.
Start the scheduler: python scheduler.py (in a separate terminal).
Run the app: python app.py.
Access at http://127.0.0.1:5000/.
