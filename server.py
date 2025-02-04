"""
Flask application for detecting emotions from text input using an external API.
"""
from flask import Flask, render_template, request, jsonify
import requests
# Initialize Flask app
app = Flask(__name__)
def emotion_detector(text_to_analyze):
    """
    Sends the given text to the Watson Emotion API for analysis and extracts emotions.

    Args:
        text_to_analyze (str): The text to be analyzed for emotions.

    Returns:
        dict: Dictionary containing detected emotions and the dominant emotion.
              Returns an error message if no emotions are detected or if there is an issue.
    """
    url = (
    "https://sn-watson-emotion.labs.skills.network/v1/"
    "watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(url, json=input_json, headers=headers, timeout=10)
        response.raise_for_status()
        response_data = response.json()

        if "emotion_predictions" not in response_data or not response_data["emotion_predictions"]:
            return None

        emotions = response_data["emotion_predictions"][0]
        extracted_emotions = {
            "anger": emotions.get("anger", 0),
            "disgust": emotions.get("disgust", 0),
            "fear": emotions.get("fear", 0),
            "joy": emotions.get("joy", 0),
            "sadness": emotions.get("sadness", 0),
        }

        dominant_emotion = max(extracted_emotions, key=extracted_emotions.get)
        extracted_emotions["dominant_emotion"] = dominant_emotion

        return extracted_emotions

    except requests.exceptions.Timeout:
        return {"error": "Request timed out"}
    except requests.exceptions.RequestException as err:
        return {"error": str(err)}

@app.route('/')
def index():
    """
    Serves the index page.
    """
    return render_template('index.html')

@app.route('/detect_emotion', methods=['POST'])
def detect_emotion():
    """
    API endpoint that receives text input, analyzes its emotions, and returns the results.

    Returns:
        JSON response containing detected emotions or an error message.
    """
    text = request.json.get("text", "").strip()

    if not text:
        return jsonify({"error": "No text provided"})

    result = emotion_detector(text)

    if result and result.get("dominant_emotion"):
        return jsonify(result)

    return jsonify({"error": "Invalid text! Please try again!"})

if __name__ == '__main__':
    app.run(debug=True)
