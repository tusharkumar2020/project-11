import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    data = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Send the POST request
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        # Convert the response to a dictionary using json()
        response_data = response.json()

        # Extract the emotions
        emotions = response_data.get('result', {}).get('emotion', {})

        # Get the specific emotions and their scores
        anger_score = emotions.get('anger', 0)
        disgust_score = emotions.get('disgust', 0)
        fear_score = emotions.get('fear', 0)
        joy_score = emotions.get('joy', 0)
        sadness_score = emotions.get('sadness', 0)

        # Create a dictionary with the required format
        emotion_output = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }

        # Determine the dominant emotion by finding the highest score
        dominant_emotion = max(emotion_output, key=emotion_output.get)

        # Add the dominant emotion to the dictionary
        emotion_output['dominant_emotion'] = dominant_emotion

        return emotion_output
    else:
        return "Error: " + response.text
