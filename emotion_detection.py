# emotion_detection.py 
# Task 2: Create an emotion detection application 
#              using the Watson NLP library.

import requests
import json

URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
    "Content-Type": "application/json"
}

# Here is my emotion_detector function. I use the Watson NLP library.
def emotion_detector(text_to_analyse):
    # JSON payload
    jsonPayload = {"raw_document": {"text": text_to_analyse}}

    try:
        response = requests.post(URL, headers=HEADERS, json=jsonPayload)

        # This is to Check ALL Raw Response
        # print("Raw Response:", response.text)

        # response check
        if response.status_code == 200:
            response_data = response.json()

            #return response_data.get("text", "No text found in response")
            # if there is emotion predictions, export the text
            if "emotionPredictions" in response_data and response_data["emotionPredictions"]:
                return response_data["emotionPredictions"][0]["emotionMentions"][0]["span"]["text"]

            return "No emotion predictions found"

        else:
            return f"Error: {response.status_code}, {response.text}"

    except requests.exceptions.RequestException as e:
        return f"Request failed: {str(e)}"


