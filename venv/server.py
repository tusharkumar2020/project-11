"""
A simple Flask application for emotion detection from text input.
"""

from flask import Flask, jsonify, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def get_emotion_detected():
    """
    This function returns the dominant emotion detected in the input text.
    """
    text_to_analyze = request.args.get("q")

    if not text_to_analyze:
        # Return a 400 status code and a dictionary with None values
        output = jsonify({
            key: None for key in [
                'happy', 'sad', 'angry', 'surprised', 'neutral', 'dominant_emotion'
            ]
        })
        return output, 400

    emotion_results = emotion_detector(text_to_analyze)

    emotions_str = ', '.join(
        [f"'{key}': {value}" for key, value in emotion_results.items()
         if key != 'dominant_emotion']
    )

    # Create the response string
    dominant_emotion = emotion_results.get('dominant_emotion')

    if dominant_emotion is None:
        return jsonify({"message": "Invalid text! Please try again!"})

    response_message = (
        f"For the given statement, the system response is {emotions_str}. "
        f"The dominant emotion is <strong>{dominant_emotion}</strong>."
    )

    return jsonify({"message": response_message})


if __name__ == "__main__":
    app.run(port=5000, debug=True)
