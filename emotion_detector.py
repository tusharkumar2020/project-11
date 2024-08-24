import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    inp = {'raw_document': {'text': text_to_analyze}}
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = inp, headers=header)
    res = response.json()
    for x in res.values():
        for y in x[0].values():
            maxim = max(y.values())
            l = list(y.keys())
            y["dominant_emotion"] = l[list(y.values()).index(maxim)]
            return y
    
    
            