import sqlite3, json, os
from datetime import datetime

DB_PATH = "predictions.db"
FALLBACK_JSON = "predictions.json"

MASK_KEYS = ['coingecko', 'newsapi', 'cryptopanic', 'telegram_token']

def mask_config(config):
    masked = config.copy()
    for k in MASK_KEYS:
        if k in masked:
            masked[k] = '***MASKED***'
    return masked

def log_prediction(signal, details, config):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS predictions
                     (timestamp TEXT, signal TEXT, details TEXT, config TEXT)''')
        c.execute("INSERT INTO predictions VALUES (?, ?, ?, ?)",
                  (datetime.utcnow().isoformat(), json.dumps(signal), json.dumps(details), json.dumps(mask_config(config))))
        conn.commit()
        conn.close()
    except Exception as e:
        with open(FALLBACK_JSON, 'a') as f:
            f.write(json.dumps({
                "timestamp": datetime.utcnow().isoformat(),
                "signal": signal,
                "details": details,
                "config": mask_config(config)
            }) + "\n")