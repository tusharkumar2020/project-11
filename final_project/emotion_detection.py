import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = { "raw_document": { "text": text_to_analyse } }

    # Send the POST request
    response = requests.post(url, headers = header, json = payload)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Print the full response for debugging
        print("Raw response:", response.text)
        
        # Parse the response text into a dictionary
        response_dict = json.loads(response.text)
        
        # Extract the required emotions and their scores
        emotions = response_dict.get("emotion", {}).get("document", {}).get("emotion", {})
        
        # List of required emotions
        required_emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness']
        
        # Extract the scores for each emotion
        emotion_scores = {emotion: emotions.get(emotion, 0.0) for emotion in required_emotions}
        
        # Find the dominant emotion (the one with the highest score)
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        
        # Return the result in the desired format
        return {
            'anger': emotion_scores['anger'],
            'disgust': emotion_scores['disgust'],
            'fear': emotion_scores['fear'],
            'joy': emotion_scores['joy'],
            'sadness': emotion_scores['sadness'],
            'dominant_emotion': dominant_emotion
        }
    else:
        return {"error": f"Request failed with status code {response.status_code}"}