import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download("vader_lexicon", quiet=True)  

def emotion_detector(text_to_analize):
    if not text_to_analize:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(text_to_analize)

    emotion_scores = {
        "anger": scores["neg"],
        "disgust": scores["neg"] / 2,
        "fear": scores["neg"] / 2,
        "joy": scores["pos"],
        "sadness": scores["neg"],
    }

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    return {
        "anger": emotion_scores["anger"],
        "disgust": emotion_scores["disgust"],
        "fear": emotion_scores["fear"],
        "joy": emotion_scores["joy"],
        "sadness": emotion_scores["sadness"],
        "dominant_emotion": dominant_emotion,
    }