import requests, json
def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=headers)
    return response.text
    formatted_response = json.loads(response.text)
    anger = formatted_response['emotionPredictions']['anger']
    disgust = formatted_response['emotionPredictions']['disgust']
    fear = formatted_response['emotionPredictions']['fear']
    joy = formatted_response['emotionPredictions']['joy']
    sadness = formatted_response['emotionPredictions']['sadness']