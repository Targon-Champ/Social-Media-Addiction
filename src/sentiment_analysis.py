import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(text)
    return score['compound']

# Example usage
example_post = "I love spending time on Instagram, it's amazing!"
print(analyze_sentiment(example_post))  # Output: Sentiment Score
