''' Executing this function initiates the application of emotion
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''

import json
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    ''' Renders the page '''
    return render_template("index.html")

@app.route("/emotionDetector")
def detect_emotion():
    ''' Calls the emotion_detector method using text from the application '''
    text_to_analyze = request.args.get("textToAnalyze")
    dict_response = emotion_detector(text_to_analyze)

    #handle if dominant_emotion is None
    if dict_response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    strng = json.dumps(dict_response).strip("{}")
    return f"For the given statement, the system response is {strng}."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
