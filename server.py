from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def emotionDetector():
    textToAnalyze = request.args.get('textToAnalyze')

    result = emotion_detector(textToAnalyze)

    string_result = f"For the given statement, the system response is " 
    string_result += f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
    string_result += f"'fear': {result['fear']}, 'joy': {result['joy']} and "
    string_result += f"'sadness': {result['sadness']}. "
    string_result += f"The dominant emotion is {result['dominant_emotion']}."

    return string_result

@app.route("/")
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)