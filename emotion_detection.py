import requests
import json

def emotion_detector(text):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Prepare the input JSON structure
    input_json = {
        "raw_document": {
            "text": text
        }
    }
    
    # Set the headers, including the custom grpc metadata header
    headers = {
        'Content-Type': 'application/json',
        'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock'
    }
    
    try:
        # Send the POST request to the API
        response = requests.post(url, json=input_json, headers=headers)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse and return the JSON response
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
text_to_analyze = "I love this new technology."
response = emotion_detector(text_to_analyze)

if response:
    print("API Response:", json.dumps(response, indent=4))
