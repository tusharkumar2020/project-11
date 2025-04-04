from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET", "POST"])
def emotion_analysis():
    # Accept query parameter for GET
    if request.method == "GET":
        text = request.args.get("textToAnalyze")
    else:  # for POST (not used by your frontend, but nice to have)
        text = request.form["text"]

    result = emotion_detector(text)

    # Error handling for invalid/blank input
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
