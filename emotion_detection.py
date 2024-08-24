import requests
import json

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL, json = myobj, headers=headers)

    ##jsonifying the response
    formated_response = json.loads(response.text)
    return_dict = formated_response["emotionPredictions"][0]['emotion']
    
    ##finding the dominant emotion
    dominant_emotion = "anger"
    for i in return_dict:
        if return_dict[dominant_emotion] < return_dict[i]:
            dominant_emotion = i
    
    ##adding the dominant emotion to the dictionary that the function will return
    return_dict['dominant_emotion'] = dominant_emotion

    return return_dict

