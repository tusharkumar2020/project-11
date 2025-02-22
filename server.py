"""
Flask server for emotion detection API.
"""

from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detection

app = Flask(__name__)

@app.route('/')
def home():
    """
    Renders the home page.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_api():
    """
    Handles POST requests for emotion detection.

    Expects JSON data with a "text" key.
    Returns a JSON response containing emotion scores
    and the dominant emotion.
    """
    data = request.json
    text_to_analyze = data.get("text", "").strip()

    if not text_to_analyze:
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    result = emotion_detection.emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']}, "
        f"and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return jsonify({"response": response_text, "data": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7000, debug=True)
