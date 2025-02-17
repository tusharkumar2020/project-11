"""
Emotion Detection Flask Application.

This module defines a Flask web application that exposes an API for emotion detection.
It receives a text input via a POST request and returns the emotional analysis, including
emotion scores (anger, disgust, fear, joy, sadness) and the dominant emotion.

The application communicates with an external emotion detection service to classify the 
emotions present in the provided text.

Modules:
    - Flask: Web framework for handling HTTP requests.
    - requests: For sending HTTP requests to the external emotion detection service.
    - json: For parsing JSON responses.

"""


from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

# Initialize the Flask application
app = Flask(__name__)

@app.route("/emotionDetector", methods=["POST"])
def emotion_detector_route():
    """
    Handle the emotion detection request.

    This function accepts a POST request containing the text to analyze. 
    It returns the emotion detection result or an error message if the input is invalid.
    
    Returns:
        Response: A JSON object containing the emotion detection results or an error message.
    """
    # Get the text to analyze from the request
    data = request.get_json()
    text_to_analyse = data.get("text", "")

    # Validate if the text is provided
    if not text_to_analyse:
        return jsonify({"error": "No text provided"}), 400

    # Call the emotion detector function
    result = emotion_detector(text_to_analyse)

    # Check if dominant_emotion is None and return error message
    if result.get("dominant_emotion") is None:
        return jsonify({"response": "Invalid text! Please try again."}), 400

    # Format the response as required by the customer
    emotion_summary = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )

    # Return the formatted response
    return jsonify({"response": emotion_summary})

if __name__ == '__main__':
    # Run the application
    app.run(host='0.0.0.0', port=5000, debug=True)
