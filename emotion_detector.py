# -*- coding: utf-8 -*-


import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

analyzer = SentimentIntensityAnalyzer()

def detect_emotion(text):
    scores = analyzer.polarity_scores(text)
    compound = scores['compound']

    if compound >= 0.4:
        emotion = "happy"
    elif compound <= -0.4:
        emotion = "frustrated"
    else:
        emotion = "neutral"

    intensity = abs(compound)
    return emotion, intensity

