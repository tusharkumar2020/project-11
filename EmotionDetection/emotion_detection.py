import requests, json  # Import the requests library to handle HTTP requests


def emotion_detector(
    text_to_analyse,
):  # Define a function named emotion_detector that takes a string input (text_to_analyse)
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    myobj = {"raw_document": {"text": text_to_analyse}}
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header)

    if response.status_code == 200:
        formatted = json.loads(response.text)
        emotion = formatted["emotionPredictions"][0]["emotion"]
        emotion["dominant_emotion"] = find_dominant_emotion(emotion)
        return emotion
    # If the response status code is 400, set to None
    elif response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }


def find_dominant_emotion(emotions):
    return max(emotions, key=emotions.get)
