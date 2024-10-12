"""This module has function related to emotions detection
"""
import json
import requests

def emotion_detector(text_to_analyze):
    """This function is for detect the emotion based on the text given.
    it takes the string text and send a post request to watson api and get the text response
    then based on the response convert it to json and then return required parameters as json

    Args:
        text_to_analyze (String): this is the text it takes to detect the emotion.

    Returns:
        dict: output_json which is dictionary out put contains required parameters.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload =  { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url , json = payload , headers = header, timeout=10)
    
    formatted_response = json.loads(response.text)
    output_json = {}
    
    if response.status_code == 200:
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
    elif response.status_code == 500:
        output_json = {
            'anger':None,
            'disgust':None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    return output_json
