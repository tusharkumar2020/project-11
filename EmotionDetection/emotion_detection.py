# emotion_detection.py 

import requests
import json

URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
    "Content-Type": "application/json"
}

#  Task 2: Here is my emotion_detector function. I use the Watson NLP library.
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
                emotions = response_data["emotionPredictions"][0]["emotion"]

                #  Task 3: Set emotions & Scores
                anger_score = emotions.get("anger", 0.0)
                disgust_score = emotions.get("disgust", 0.0)
                fear_score = emotions.get("fear", 0.0)
                joy_score = emotions.get("joy", 0.0)
                sadness_score = emotions.get("sadness", 0.0)

                # Task 3:  Finding of dominant emotion
                emotion_scores = {
                    "anger": anger_score,
                    "disgust": disgust_score,
                    "fear": fear_score,
                    "joy": joy_score,
                    "sadness": sadness_score
                }
                dominant_emotion = max(emotion_scores, key=emotion_scores.get)

                #  Task 3: Creation of final dictionary
                result = {
                    "anger": anger_score,
                    "disgust": disgust_score,
                    "fear": fear_score,
                    "joy": joy_score,
                    "sadness": sadness_score,
                    "dominant_emotion": dominant_emotion
                }

                return result  #  Task 3: Format the output of the application.

            return {"error": "No emotion predictions found"}

        else:
            return {"error": f"Watson API Error: {response.status_code}, {response.text}"}


    except requests.exceptions.RequestException as e:
        return f"Request failed: {str(e)}"


