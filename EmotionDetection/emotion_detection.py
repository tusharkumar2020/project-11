import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = {"raw_document": {"text": text_to_analyze}}
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    response = requests.post(url, json=myobj, headers=header, timeout=10)

    if response.status_code == 200:
        try:
            json_response = response.json()
            emotions = json_response['emotionPredictions'][0]['emotionMentions'][0]['emotion']
            dominant_emotion = max(emotions, key=emotions.get, default=None)
            emotion_response = {
                **emotions,
                'dominant_emotion': dominant_emotion
            }
            json_string = json.dumps(emotion_response, indent=4)  
            print(json_string)
            return json_string

        except (KeyError, IndexError) as e:
            print(f"Error extracting text from JSON: {e}")
            print(json.dumps(json_response, indent=4)) # Print the full JSON for debugging
            return "Error: Could not extract text"

    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return f"Error: {response.status_code}"


# Example usage (no changes needed here):

