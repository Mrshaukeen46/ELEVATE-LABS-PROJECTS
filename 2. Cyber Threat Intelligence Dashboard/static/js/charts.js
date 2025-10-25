// Assuming trends data is passed as JSON in template (extend app.py to pass it)
const trends = {{ trends | tojson }};
const timestamps = trends.map(t => t.timestamp);
const levels = trends.map(t => t.threat_level === 'High' ? 3 : t.threat_level === 'Medium' ? 2 : 1);

Plotly.newPlot('trend-chart', [{
    x: timestamps,
    y: levels,
    type: 'scatter',
    mode: 'lines+markers'
}], { title: 'Threat Level Trends' });
