import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url, headers=headers, json=data)
    response_dict = response.json()

    # Extract emotion scores from the nested structure
    emotion_predictions = response_dict.get('emotionPredictions', [])
    if not emotion_predictions:
        emotions = {}
    else:
        emotions = emotion_predictions[0].get('emotion', {})
    
    # Prepare the output dictionary with default scores as 0.0
    output = {
        'anger': emotions.get('anger', 0.0),
        'disgust': emotions.get('disgust', 0.0),
        'fear': emotions.get('fear', 0.0),
        'joy': emotions.get('joy', 0.0),
        'sadness': emotions.get('sadness', 0.0)
    }
    
    # Determine the dominant emotion
    dominant_emotion = max(output, key=output.get)
    output['dominant_emotion'] = dominant_emotion
    
    return json.dumps(output, indent=4)
