import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyze}}
    
    response = requests.post(url=url, json=myobj, headers=header, timeout=5)

    # Manejo de errores
    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.text}")
        return None

    formated_response = response.json()

    if 'emotionPredictions' in formated_response and formated_response['emotionPredictions']:
        emotions = formated_response['emotionPredictions'][0]['emotion']
        
        # Asegúrate de que las claves existan
        anger = emotions.get('anger', 0)
        disgust = emotions.get('disgust', 0)
        fear = emotions.get('fear', 0)
        joy = emotions.get('joy', 0)
        sadness = emotions.get('sadness', 0)
        
        max_emotion = max(emotions, key=emotions.get)
        
        formated_dict_emotions = {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness,
            'dominant_emotion': max_emotion
        }
        return formated_dict_emotions
    else:
        print("No emotion predictions found in the response.")
        return None
