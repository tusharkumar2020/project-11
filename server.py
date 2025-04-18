from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

@app.route("/emotionDetector")



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)