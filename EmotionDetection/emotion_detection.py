"""NO TERMINAL: from emotion_detection import emotion_detector"""
import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock',
        'Content-Type': 'application/json'
    }
    payload = {
        "raw_document": {"text": text_to_analyze}
    }

    # Fazendo a requisição para a API
    response = requests.post(url, headers = headers, json = payload)

    # Verificando se a resposta é válida
    if response.status_code == 200:
        # Convertendo o corpo da resposta JSON para um dicionário
        response_dict = json.loads(response.text)

        # Extraindo as pontuações das emoções
        anger_score = response_dict["emotionPredictions"][0]["emotion"]["anger"]
        disgust_score = response_dict["emotionPredictions"][0]["emotion"]["disgust"]
        fear_score = response_dict["emotionPredictions"][0]["emotion"]["fear"]
        joy_score = response_dict["emotionPredictions"][0]["emotion"]["joy"]
        sadness_score = response_dict["emotionPredictions"][0]["emotion"]["sadness"]

        # Determinando a emoção dominante
        emotions = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }
        
        dominant_emotion = max(emotions, key = emotions.get)

        # Retornando o resultado formatado
        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
    
    elif response.status_code == 400:
        return {"anger": None, "disgust": None, "fear": None, "joy": None, "sadness": None, "dominant_emotion": None}
    
    else:
        return f"Error: {response.status_code}, {response.text}"

# Testando a função
formatted_output = emotion_detector("I love this new technology.")
print(json.dumps(formatted_output, indent = 4))
