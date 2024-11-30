import requests

URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}

def emotion_detector(text_to_analyze):
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    try:
        response = requests.post(URL, headers=HEADERS, json=payload)
        response.raise_for_status()   
        response_data=response.json()        
        emotion_predictions=response_data.get('emotionPredictions',[])  
        if not emotion_predictions:
            return {"error": "No emotion predictions found in response"} 
        emotions=emotion_predictions[0].get('emotion',{})
        if not emotions:
            return {"error": "No emotion data found in response"}


        anger =emotions.get('anger',0)
        disgust=emotions.get('disgust',0)
        fear = emotions.get('fear',0)
        joy = emotions.get('joy',0)
        sadness=emotions.get('sadness',0)
        
        emotion_scores = {
            'anger':anger,
            'disgust': disgust,
            'fear': fear,
            'joy':joy,
            'sadness':sadness                 
        }
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        emotion_scores['dominant_emotion'] = dominant_emotion
        
        return emotion_scores

        
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
