"""
server.py

This module implements a Flask server for emotion detection from text input.
It provides an endpoint '/emotionDetector' that accepts POST requests
with a JSON payload and returns detected emotions.
"""

from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector  # Correct import statement

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_endpoint():
    """
    Endpoint for emotion detection.
    
    Expects a JSON payload with a key 'text' to analyze for emotions.
    Returns a JSON response with detected emotions.
    """
    data = request.get_json()
    text_to_analyze = data.get('text')
    if not text_to_analyze:  # Check for blank entries
        return jsonify({"error": "Invalid text! Please try again!"}), 400
    result = emotion_detector(text_to_analyze)
    if result is None:  # Check for None result
        return jsonify({"error": "Invalid text! Please try again!"}), 400
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
