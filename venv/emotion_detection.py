import requests
import json


def emotion_detector(emotion):
    """ URL: 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers: {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    Input json: { "raw_document": { "text": text_to_analyse } }"""
    url = "http://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock'}
    body = {"raw_document": {"text": emotion}}

    response = requests.post(url, json=body, headers=headers)
    print("hi hi ")
    text = ''
    return text


emotion_detector("I love you ! ")
