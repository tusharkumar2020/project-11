from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():

    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)


    anger = response[0]
    disgust = response[1]
    fear = response[2]
    joy = response[3]
    sadness = response[4]
    dominant_emotion = response[5]

    return "For the given statement, the system response is {}, {}, {}, {}, and {}. The dominant emotion is {}.".format(anger, disgust, fear, joy, sadness, dominant_emotion)

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    