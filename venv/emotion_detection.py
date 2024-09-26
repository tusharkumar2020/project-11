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
    print(response.json().get('emotionprediction', {}).get('emotionmentions', {}).get('text', ''))
    l = response.json().get('emotionPredictions', None);
    emotion_mention = l[0]['emotionMentions'][0]['span']['text']

    if response.status_code == 200:
        return emotion_mention
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")
