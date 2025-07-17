import requests

def send_telegram_alert(signal, details, config):
    msg = f"{signal['action']} {details.get('entry_range', '')}\nSL: {details.get('stop_loss')}, TP: {details.get('take_profit')}\nConfidence: {signal['confidence']:.2f}"
    url = f"https://api.telegram.org/bot{config['telegram_token']}/sendMessage"
    data = {"chat_id": config['telegram_chat_id'], "text": msg}
    try:
        requests.post(url, data=data)
    except Exception: pass