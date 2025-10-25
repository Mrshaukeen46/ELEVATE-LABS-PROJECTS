# Web Vulnerability Scanner (Local)

This is a simple Python-based web vulnerability scanner with a Flask UI. It's intentionally minimal and designed for educational use against test targets (e.g., OWASP Juice Shop, DVWA) running locally.

Usage:
1. Install dependencies: `pip install -r requirements.txt`
2. Ensure your target is running on localhost (e.g., `docker run --rm -p 3000:3000 bkimminich/juice-shop`).
3. Start the app: `python app.py`
4. Open http://127.0.0.1:5000 in your browser, enter target URL, and run the scan.

Safety:
- The scanner restricts targets to localhost by default. Do not use against third-party systems without permission.

Limitations:
- Basic payload tests only; may generate false positives/negatives.
