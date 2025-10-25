from apscheduler.schedulers.background import BackgroundScheduler
from data_fetcher import aggregate_threats

scheduler = BackgroundScheduler()
scheduler.add_job(aggregate_threats, 'interval', minutes=10)  # Real-time pull every 10 min
scheduler.start()
