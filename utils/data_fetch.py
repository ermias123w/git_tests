import requests

def fetch_market_data(config):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    r = requests.get(url)
    data = r.json()
    return data

def fetch_news(config):
    news = []
    try:
        newsapi_url = f"https://newsapi.org/v2/everything?q=bitcoin+ethereum&apiKey={config['newsapi']}"
        r = requests.get(newsapi_url)
        news += r.json().get('articles', [])
    except Exception: pass
    try:
        panic_url = f"https://cryptopanic.com/api/v1/posts/?auth_token={config['cryptopanic']}&currencies=BTC,ETH"
        r = requests.get(panic_url)
        news += r.json().get('results', [])
    except Exception: pass
    return news