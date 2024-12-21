import requests  # Importar la biblioteca requests para manejar solicitudes HTTP
def emotion_detector(text_to_analyse):  # Definir una función llamada emotion_detector que toma una cadena como entrada (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header)  # Enviar una solicitud POST a la API con el texto y los encabezados
    
    if response.status_code == 200:
        response_dict = response.json()
        predictions = response_dict.get("emotionPredictions", [{}])[0]
        emotions = predictions.get("emotion", {})
        scores = {
            'anger': emotions.get('anger', 0),
            'disgust': emotions.get('disgust', 0),
            'fear': emotions.get('fear', 0),
            'joy': emotions.get('joy', 0),
            'sadness': emotions.get('sadness', 0),
        }
        
        # Buscamos la emoción dominante
        dominant_emotion = max(scores, key=scores.get)
        scores['dominant_emotion'] = dominant_emotion
        
        return scores

    elif response.status_code == 400:
        # Retorna un diccionario con valor None
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
