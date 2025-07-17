from flask import Flask, render_template, request, redirect
import os, json
from apscheduler.schedulers.background import BackgroundScheduler
from utils.data_fetch import fetch_market_data, fetch_news
from utils.indicators import compute_indicators
from utils.sentiment import analyze_sentiment
from utils.hybrid_model import predict_signal
from utils.risk import apply_risk_rules
from utils.logger import log_prediction
from utils.backtest import run_backtest
from utils.telegram import send_telegram_alert
from datetime import datetime

app = Flask(__name__)
CONFIG_PATH = "api_keys.json"
scheduler = BackgroundScheduler()
scheduler.start()


def load_config():
    if not os.path.exists(CONFIG_PATH):
        return None
    with open(CONFIG_PATH) as f:
        return json.load(f)

@app.route('/setup', methods=['GET', 'POST'])
def setup():
    if request.method == 'POST':
        config = {k: request.form[k] for k in request.form}
        config['confidence'] = float(config['confidence'])
        config['frequency'] = int(config['frequency'])
        with open(CONFIG_PATH, 'w') as f:
            json.dump(config, f)
        return redirect('/')
    return render_template('setup.html')

@app.route('/')
def index():
    config = load_config()
    if not config:
        return redirect('/setup')
    # Fetch latest signals, logs, stats for dashboard
    return render_template('index.html', config=config)

def scheduled_job():
    config = load_config()
    if not config:
        return
    prices = fetch_market_data(config)
    news = fetch_news(config)
    features = compute_indicators(prices)
    sentiment = analyze_sentiment(news, config)
    signal, details = predict_signal(features, sentiment, config)
    signal, details = apply_risk_rules(signal, details, config)
    log_prediction(signal, details, config)
    if signal['confidence'] >= config['confidence']:
        send_telegram_alert(signal, details, config)

def reschedule():
    scheduler.remove_all_jobs()
    config = load_config()
    if config:
        scheduler.add_job(scheduled_job, 'interval', minutes=config['frequency'])

@app.before_first_request
def init():
    reschedule()

@app.route('/reschedule')
def reschedule_route():
    reschedule()
    return "Rescheduled"

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860)