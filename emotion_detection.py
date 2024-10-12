import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload =  { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url , json = payload , headers = header)
    formatted_response = json.loads(response.text)
    anger = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness = formatted_response['emotionPredictions'][0]['emotion']['sadness']
    emotion_scores = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
    }
    dominant_emotion_score = max(emotion_scores.values())
    dominant_emotion_list = [dominant for dominant in emotion_scores if emotion_scores[dominant] == dominant_emotion_score]
    output_json = emotion_scores.copy()
    output_json.update({'dominant_emotion':dominant_emotion_list[0]})
    return output_json