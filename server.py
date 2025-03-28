"""Flask server for emotion detection API."""

from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector  # Import your function

app = Flask(__name__)

@app.route("/emotionDetector", methods=["POST"])
def emotion_detector_api():
    """API endpoint to analyze emotions from the input text."""
    data = request.get_json()

    if not data or "text" not in data or not data["text"].strip():  # Handle empty input
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    result = emotion_detector(data["text"])

    if not isinstance(result, dict) or result.get("dominant_emotion") is None:
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    formatted_response = {
        "response": (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, "
            f"'joy': {result['joy']} and "
            f"'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}."
        )
    }

    return jsonify(formatted_response)

if __name__ == "__main__":
    app.run(debug=True)
