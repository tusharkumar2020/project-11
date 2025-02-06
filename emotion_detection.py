import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": { "text": text_to_analyse }}

    try:
        response = requests.post(url, json=myobj, headers=headers)
        response.raise_for_status()  # Lanza una excepción para errores HTTP
        res = response.json()  # Parsea directamente el JSON de la respuesta
        
        # Extraer emociones relevantes
        emotions = res.get('emotionPredictions', [{}])[0].get('emotion', {})
        extracted_emotions = {
            'anger': emotions.get('anger', 0),
            'disgust': emotions.get('disgust', 0),
            'fear': emotions.get('fear', 0),
            'joy': emotions.get('joy', 0),
            'sadness': emotions.get('sadness', 0)
        }

        # Determinar la emoción dominante
        dominant_emotion = max(extracted_emotions, key=extracted_emotions.get)
        extracted_emotions['dominant_emotion'] = dominant_emotion

        return extracted_emotions

    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {e}"}

# Ejemplo de uso
text = "I am extremely happy today!"
result = emotion_detector(text)
print(result)



