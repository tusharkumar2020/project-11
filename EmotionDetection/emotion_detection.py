import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download("vader_lexicon", quiet=True)  # Download the lexicon if not already available


def emotion_detector(text_to_analyze):
    # Handle blank or None input (like API status code 400)
    if not text_to_analyze or text_to_analyze.strip() == "":
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(text_to_analyze)

    emotion_scores = {
        "anger": scores["neg"] * 0.5,
        "disgust": scores["neg"] * 0.3 + 0.1 if "disgust" in text_to_analyze.lower() else 0,
        "fear": scores["neg"] * 0.3 + 0.1 if "afraid" in text_to_analyze.lower() or "fear" in text_to_analyze.lower() else 0,
        "joy": scores["pos"],
        "sadness": scores["neg"] * 0.4 + 0.1 if "sad" in text_to_analyze.lower() else 0,
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
