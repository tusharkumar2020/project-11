''' Sends text to the WatsonAI side to be analyzed for emotion.
    Returns a dict with 5 emotions as keys and their scores as values and the dominant emotion
    {'anger': 0.0, 'disgust': 0.0, 'fear': 0.0, 'joy': 0.0, 'sadness': 0.0, 'dominant_emotion': 'anger'}
'''

import json
import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    inpt = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=inpt, headers=headers)
    formatted_response = json.loads(response.text)

    if response.status_code == 500 or response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    emotions_dict = formatted_response["emotionPredictions"][0]["emotion"]

    dominant_emotion = "anger"
    for key in emotions_dict.keys():
        if emotions_dict[key] > emotions_dict[dominant_emotion]:
            dominant_emotion = key

    return {
        "anger": emotions_dict["anger"],
        "disgust": emotions_dict["disgust"],
        "fear": emotions_dict["fear"],
        "joy": emotions_dict["joy"],
        "sadness": emotions_dict["sadness"],
        "dominant_emotion": dominant_emotion
    }