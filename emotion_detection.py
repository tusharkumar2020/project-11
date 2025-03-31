import json

import requests


def emotion_detector(text_to_analize):
    text_to_analyse = text_to_analize
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyse}}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return {"error": f"Error al conectar con el servicio: {e}"}

    try:
        result_dict = json.loads(response.text)
    except json.JSONDecodeError as e:
        return {"error": f"Error al decodificar la respuesta: {e}"}

    anger_score = result_dict.get("anger")
    disgust_score = result_dict.get("disgust")
    fear_score = result_dict.get("fear")
    joy_score = result_dict.get("joy")
    sadness_score = result_dict.get("sadness")

    scores = {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
    }

    dominant_emotion = max(
        scores, key=lambda k: scores[k] if scores[k] is not None else float("-inf")
    )

    return {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
        "dominant_emotion": dominant_emotion,
    }
