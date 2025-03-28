"""Server module for handling emotion detection API."""

import requests
import json

def emotion_detector(text_to_analyze):
    """Detects emotions from the given text using an external API."""
    if not text_to_analyze.strip():  # Check if input is blank
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
    
    URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(URL, json={"raw_document": {"text": text_to_analyze}}, headers=HEADERS)

    if response.status_code == 400:  # Handle bad request response
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    if response.ok:
        response_dict = response.json()
        emotion = response_dict.get("emotionPredictions", [{}])[0].get("emotion", {})

        anger_score = emotion.get("anger", 0)
        disgust_score = emotion.get("disgust", 0)
        fear_score = emotion.get("fear", 0)
        joy_score = emotion.get("joy", 0)
        sadness_score = emotion.get("sadness", 0)
        dominant_emotion = max(emotion, key=emotion.get) if emotion else "unknown"

        return {
            "anger": anger_score,
            "disgust": disgust_score,
            "fear": fear_score,
            "joy": joy_score,
            "sadness": sadness_score,
            "dominant_emotion": dominant_emotion
        }

    return {"error": response.text}
