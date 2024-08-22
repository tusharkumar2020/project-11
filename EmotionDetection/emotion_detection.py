import json
import requests

def emotion_detector(text_to_analyze):
    # Check if the input text is blank
    if not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = {"raw_document": {"text": text_to_analyze}}
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make the POST request
    response = requests.post(url, json=myobj, headers=header)

    if response.status_code == 400:  # Handle invalid requests
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Parse the JSON response if the request was successful
    formatted_response = json.loads(response.text)

    # Extract emotion scores
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Determine the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    # Format the output
    output = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }

    return output
