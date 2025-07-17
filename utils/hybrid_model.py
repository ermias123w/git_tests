def predict_signal(features, sentiment, config):
    confidence = min(1.0, abs(sentiment) * 0.8 + 0.2)
    if confidence < config['confidence']:
        return {'action': 'HOLD', 'confidence': confidence}, {}
    action = 'BUY' if sentiment > 0 else 'SELL' if sentiment < 0 else 'HOLD'
    details = {
        'entry_range': (features['close']*0.99, features['close']*1.01),
        'stop_loss': features['close']*0.97,
        'take_profit': features['close']*1.05,
        'leverage': 2 if confidence > 0.8 else 1,
        'explanation': f"Sentiment: {sentiment:.2f}, RSI: {features['rsi']:.1f}, MACD: {features['macd']:.2f}"
    }
    return {'action': action, 'confidence': confidence}, details