import requests
import json

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_data = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(URL, json=input_data, headers=headers)
    formatted_response = response.json() # You can also use json.loads(response.text)
    predictions = formatted_response['emotionPredictions'][0]['emotion']
    dominantEmotion = max(predictions, key=predictions.get)
    predictions['dominant_emotion'] = dominantEmotion

    return predictions