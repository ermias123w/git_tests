# Crypto Predictor Web App

A mobile-optimized, resource-efficient crypto prediction app for BTC/ETH using hybrid ML, technicals, and news sentiment. Runs on Replit or Google Colab.

## Features
- No-code setup page for API keys and config
- Live BTC/ETH data, news, technicals, FinBERT sentiment
- Hybrid LSTM+Transformer+FinBERT ensemble
- Real-time BUY/SELL/HOLD signals with entry, SL/TP, leverage, confidence, explanation
- SQLite/JSON logging, backtesting, Telegram alerts
- Modular, secure, and easy to extend

## Quickstart
1. `pip install -r requirements.txt`
2. `python app.py`
3. Open the setup page in your browser, enter your API keys and config

## Notes
- Default mode is paper trading for safety
- All credentials are masked in logs
- For Colab, use `ngrok` to expose the Flask app

---