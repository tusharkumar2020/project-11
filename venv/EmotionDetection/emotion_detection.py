import requests


def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    response = requests.post(url, json=input_json, headers=headers)
    # print(response.json().get('emotionprediction', {}).get('emotionmentions', {}).get('text', ''))
    emotion_list = response.json().get('emotionPredictions', None)
    emotion_mentioned = emotion_list[0]['emotionMentions'][0]['emotion']
    # max_score = max(emotion_mentioned.values())
    max_emo = max(emotion_mentioned, key=emotion_mentioned.get)
    emotion_mentioned['dominant_emotion'] = max_emo

    if response.status_code == 200:
        return emotion_mentioned['dominant_emotion']
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")
