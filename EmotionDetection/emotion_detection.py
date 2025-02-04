import requests
import json

def emotion_detector(text_to_analyse):
    # Check for blank input
    if not text_to_analyse.strip():
        return {
            'emotion_scores': {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None
            },
            'dominant_emotion': None
        }
    
    # URL of the emotion detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    # Custom header specifying the model ID for the emotion detection service
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Sending a POST request to the emotion detection API
    response = requests.post(url, json=myobj, headers=headers)
    
    # Check for HTTP errors and handle status code 400
    if response.status_code == 400:
        return {
            'emotion_scores': {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None
            },
            'dominant_emotion': None
        }
    
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    
    # Creating a dictionary to hold all emotion scores
    emotions = {
        'anger': formatted_response['emotionPredictions'][0]['emotion']['anger'],
        'disgust': formatted_response['emotionPredictions'][0]['emotion']['disgust'],
        'fear': formatted_response['emotionPredictions'][0]['emotion']['fear'],
        'joy': formatted_response['emotionPredictions'][0]['emotion']['joy'],
        'sadness': formatted_response['emotionPredictions'][0]['emotion']['sadness']
    }
    
    # Finding the dominant emotion (the one with the highest score)
    dominant_emotion = max(emotions, key=emotions.get)

    # Returning a dictionary containing all emotion scores and the dominant emotion
    return {
        'emotion_scores': emotions,
        'dominant_emotion': dominant_emotion
    }
