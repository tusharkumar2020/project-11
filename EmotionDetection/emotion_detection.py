import requests
import json

def emotion_detector(text_to_analyze):
    """Function to analyze emotions in text using Watson NLP and handle errors properly."""
    
    if not text_to_analyze.strip():  # Check if input is empty or contains only spaces
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyze}}
    
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        
        if 'emotionPredictions' not in formatted_response:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
        
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        
        return {
            'anger': emotions.get('anger', 0),
            'disgust': emotions.get('disgust', 0),
            'fear': emotions.get('fear', 0),
            'joy': emotions.get('joy', 0),
            'sadness': emotions.get('sadness', 0),
            'dominant_emotion': max(emotions, key=emotions.get)
        }
    
    elif response.status_code == 400:  # Handle bad request errors
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    else:
        return {"error": f"Request failed with status code {response.status_code}"}

# Example usage
if __name__ == "__main__":
    text = " "
    result = emotion_detector(text)
    print(result)
