def emotion_detector(text_to_analyze):
    """
    Detects emotions in the given text using Watson NLP's EmotionPredict function.
    Handles blank entries and returns None for all keys in such cases.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        'Content-Type': 'application/json',
        'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock'
    }
    data = {"raw_document": {"text": text_to_analyze}}

    # Check for blank input
    if not text_to_analyze.strip():
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 400:  # Handle blank input or invalid requests
            return {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None,
            }

        if response.status_code == 200:
            emotions = response.json()
            emotion_predictions = emotions.get("emotionPredictions", [])
            if emotion_predictions:
                overall_emotion = emotion_predictions[0].get("emotion", {})
                required_emotions = {
                    "anger": float(overall_emotion.get("anger", 0.0)),
                    "disgust": float(overall_emotion.get("disgust", 0.0)),
                    "fear": float(overall_emotion.get("fear", 0.0)),
                    "joy": float(overall_emotion.get("joy", 0.0)),
                    "sadness": float(overall_emotion.get("sadness", 0.0)),
                }
                dominant_emotion = max(required_emotions, key=required_emotions.get)
                required_emotions["dominant_emotion"] = dominant_emotion
                return required_emotions
        else:
            return {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None,
            }
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
