import pandas as pd
import ta

def compute_indicators(prices):
    # prices: dict with BTC/ETH price history
    # For demo, use dummy DataFrame
    df = pd.DataFrame(prices)
    df['rsi'] = ta.momentum.RSIIndicator(df['close']).rsi()
    df['macd'] = ta.trend.MACD(df['close']).macd()
    df['ema10'] = ta.trend.EMAIndicator(df['close'], window=10).ema_indicator()
    df['ema50'] = ta.trend.EMAIndicator(df['close'], window=50).ema_indicator()
    df['ema200'] = ta.trend.EMAIndicator(df['close'], window=200).ema_indicator()
    df['bb_high'] = ta.volatility.BollingerBands(df['close']).bollinger_hband()
    df['bb_low'] = ta.volatility.BollingerBands(df['close']).bollinger_lband()
    df['atr'] = ta.volatility.AverageTrueRange(df['high'], df['low'], df['close']).average_true_range()
    # Add more as needed
    return df.iloc[-1].to_dict()