import requests
import json

def emotion_detector(text_to_analyse):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    Input =  { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url=URL, json=Input,headers=Headers )

    emotion_dict = response.json()
    emotion = emotion_dict.get("emotionPredictions", [{}])[0].get("emotion", {})

    if response.status_code == 400:
        
        return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None 
                }

    anger_score = emotion.get("anger", 0)
    disgust_score = emotion.get("disgust", 0)
    fear_score = emotion.get("fear", 0)
    joy_score = emotion.get("joy", 0)
    sadness_score = emotion.get("sadness", 0)
    dominant_emotion = max(emotion, key=emotion.get)
    
    return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
            }

