import requests
import json

# Function to analyze emotions in the given text
def emotion_detector(text_to_analyze):
    # URL to access the Watson NLP API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Headers that are passed in the request
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    # Data to be sent in the request (in JSON format)
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    # Sending the POST request to Watson NLP service
    response = requests.post(url, headers=headers, json=payload)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Extract and return the text from the response JSON
        return response.json().get('text', 'No emotion detected')
    else:
        # Return an error message if the request fails
        return "Error: Unable to process the request."

result = emotion_detector("I love this new technology.")
print(result)
