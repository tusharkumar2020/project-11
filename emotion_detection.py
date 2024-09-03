import requests

def emotion_detector(text_to_analyze):
    # URL and headers for the Watson NLP API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }

    # Input JSON payload for the API
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Send a POST request to the API
    response = requests.post(url, headers=headers, json=input_json)

    # Return the text attribute of the response object
    if response.status_code == 200:
        return response.json()  # Modify this line if the structure is different
    else:
        print("Error:", response.status_code, response.text)
        return None
