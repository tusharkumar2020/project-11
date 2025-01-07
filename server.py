"""
This module implements a Flask web server for emotion detection.
It uses a predefined emotion detection function to analyze text input
and returns the corresponding emotion scores and dominant emotion.
"""

from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """
    Handle the emotion detection request.

    Expects a query parameter 'textToAnalyze'. 
    Validates the input and calls the emotion_detector function. 

    Returns:
        JSON response:
            - If input is valid: Emotion scores and the dominant emotion.
            - If input is invalid or empty: Error message with status 400.
    """
    text_to_analyze = request.args.get('textToAnalyze', "").strip()

    if not text_to_analyze:
        return jsonify({"message": "Invalid text! Please try again!"}), 400

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return jsonify({"message": "Invalid text! Please try again!"}), 400

    return jsonify({
        "anger": response['anger'],
        "disgust": response['disgust'],
        "fear": response['fear'],
        "joy": response['joy'],
        "sadness": response['sadness'],
        "dominant_emotion": response['dominant_emotion']
    }), 200

@app.route("/")
def render_index_page():
    """
    Render the index page for the application.

    Returns:
        Rendered HTML content from the index.html template.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)
