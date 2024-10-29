import requests
import json

def emotion_detector(text_to_analyze):
    """
    Detects emotions from the provided text.
    
    Parameters:
        text_to_analyze (str): The text to analyze for emotions.
    
    Returns:
        dict: A dictionary containing emotion scores and the dominant emotion,
              or None if there was an error with the request.
    """
    if not text_to_analyze:  # Handle blank input
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        response_data = response.json()
        emotions = response_data.get("emotionPredictions", [{}])[0].get("emotion", {})
        
        anger = emotions.get("anger", 0)
        disgust = emotions.get("disgust", 0)
        fear = emotions.get("fear", 0)
        joy = emotions.get("joy", 0)
        sadness = emotions.get("sadness", 0)

        emotion_scores = {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness
        }
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

        return {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness,
            'dominant_emotion': dominant_emotion
        }
    elif response.status_code == 400:
        # Return None for blank entries as handled earlier
        return None
    else:
        print("Error:", response.status_code, response.text)
        return None
