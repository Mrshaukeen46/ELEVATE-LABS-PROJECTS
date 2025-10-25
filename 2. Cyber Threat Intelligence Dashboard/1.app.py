from flask import Flask, render_template, request, jsonify, send_file
import pandas as pd
from models import threats_collection, trends_collection
from data_fetcher import fetch_virustotal_data, fetch_abuseipdb_data
from scheduler import scheduler
import json

app = Flask(__name__)

@app.route('/')
def index():
    threats = list(threats_collection.find().sort('timestamp', -1).limit(10))
    trends = list(trends_collection.find())
    return render_template('index.html', threats=threats, trends=trends)

@app.route('/lookup', methods=['GET', 'POST'])
def lookup():
    if request.method == 'POST':
        ioc = request.form['ioc']
        vt_data = fetch_virustotal_data(ioc)
        ab_data = fetch_abuseipdb_data(ioc) if '.' in ioc and ioc.count('.') == 3 else None
        return render_template('lookup.html', vt_data=vt_data, ab_data=ab_data, ioc=ioc)
    return render_template('lookup.html')

@app.route('/tag/<ioc>', methods=['POST'])
def tag_ioc(ioc):
    tag = request.json.get('tag')
    threats_collection.update_one({'ioc': ioc}, {'$set': {'tag': tag}})
    return jsonify({'status': 'success'})

@app.route('/export')
def export():
    data = list(threats_collection.find())
    df = pd.DataFrame(data)
    df.to_csv('threats_export.csv', index=False)
    return send_file('threats_export.csv', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
