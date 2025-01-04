"""
This module provides a Flask application for emotion detection.
"""
from flask import Flask, render_template, request,jsonify
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector", template_folder='templates')
@app.route("/")
def render_index_page():
    """Render the main index.html page."""
    return render_template("index.html")
@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    """
    Process the input text and return the detected emotions.
    Returns:
        JSON response containing emotion scores or an error message.
    """
    data = request.get_json()
    if not data or 'textToAnalyze' not in data:
        return jsonify({"error": "Invalid text! Please try again!"}), 400
    text_to_analyze = data.get("textToAnalyze")
    try:
        dict_response = emotion_detector(text_to_analyze)
        return jsonify(dict_response)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    