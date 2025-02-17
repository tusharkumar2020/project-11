import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyse}}
    
    try:
        # Send the POST request
        response = requests.post(url, headers=headers, json=payload)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Print the full response for debugging
            print("Raw response:", response.text)
            
            # Parse the response text into a dictionary
            response_dict = json.loads(response.text)
            
            # Check if emotionPredictions exists in the response
            if 'emotionPredictions' not in response_dict or not response_dict['emotionPredictions']:
                return {"error": "No emotion predictions found in the response."}
            
            # Extract the emotion predictions
            emotions = response_dict['emotionPredictions'][0]['emotion']
            
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
    
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
    except json.JSONDecodeError:
        return {"error": "Failed to parse the response as JSON"}
