"""
server.py

This module sets up a Flask web server with a single endpoint `/emotionDetector` that
accepts POST requests containing text data. It uses the `emotion_detector` function 
from the `EmotionDetection` package to analyze the emotions in the text and returns 
the results in a formatted response.

The endpoint responds with the emotion scores and the dominant emotion.
"""

from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    """
    Endpoint to receive a POST request with text data and return emotion analysis.

    The endpoint expects JSON data with a 'text' field. It returns the emotion scores 
    and the dominant emotion as a formatted response.

    Returns:
        Response object with JSON data containing the emotion analysis or an error message.
    """
    data = request.get_json()
    text = data.get('text', '').strip()

    response = emotion_detector(text)

    if response['dominant_emotion'] is None:
        return jsonify({"response": "Invalid text! Please try again!"}), 400

    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."
    )
    return jsonify({"response": formatted_response})

if __name__ == '__main__':
    app.run(debug=True)
