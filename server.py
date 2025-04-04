"""
Flask server application for emotion detection.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    """
    Render the main page with the input form.
    """
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET", "POST"])
def emotion_analysis():
    """
    Handle requests to the /emotionDetector route.
    Analyze the input text and return the detected emotions.
    """
    if request.method == "GET":
        text = request.args.get("textToAnalyze")
    else:
        text = request.form["text"]

    result = emotion_detector(text)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
