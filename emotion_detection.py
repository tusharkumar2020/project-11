import requests,json
def emotion_detector(text_to_analyse):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url = URL, json = myobj, headers = Headers)

    formatted_response = json.loads(response.text)

    set_of_emotions = formatted_response['emotionPredictions'][0]['emotion']

    for emo, value in set_of_emotions.items():
        if max(set_of_emotions.values()) == value:
           dominant_emotion = emo
    set_of_emotions['dominant_emotion'] = dominant_emotion
    
    return set_of_emotions   


            
