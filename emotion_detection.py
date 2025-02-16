import requests
def emotion_detector(text_to_analyse):
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }  
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  
    response = requests.post(url, json = myobj, headers=header)  
    return response.text

    formatted_response = json.loads(response.text)
    anger = formatted_response['emotionPredictions']['emotion']['anger']
    disgust = formatted_response['emotionPredictions']['emotion']['disgust']
    fear = formatted_response['emotionPredictions']['emotion']['fear']
    joy = formatted_response['emotionPredictions']['emotion']['joy']
    sadness = formatted_response['emotionPredictions']['emotion']['sadness']
  
    return {'anger': anger, 'disgust': disgust, 'fear': fear, 'joy': joy, 'sadness': sadness}