from transformers import pipeline

finbert = pipeline("sentiment-analysis", model="yiyanghkust/finbert-tone")

def analyze_sentiment(news, config):
    texts = [item['title'] for item in news if 'title' in item]
    if not texts:
        return 0
    results = finbert(texts)
    score = sum(1 if r['label']=='positive' else -1 if r['label']=='negative' else 0 for r in results)
    return score / len(results)