from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = app = Flask(__name__)

@app.route("/emotionDetector")
def response():
    text_to_analyze = request.args.get('textToAnalyze')
    ##Error handeling
    if text_to_analyze.status_code == 400:
        return f"For the given statement, the system response is 'anger': NONE, 'disgust': NONE, 'fear': NONE, 'joy': NONE and 'sadness': NONE. The dominant emotion is NONE."
    
    emotion_response = emotion_detector(text_to_analyze)
    anger = emotion_response["anger"]
    disgust = emotion_response["disgust"]
    fear = emotion_response["fear"]
    joy = emotion_response["joy"]
    sadness = emotion_response['sadness']
    dominant_emotion = emotion_response["dominant_emotion"]
    
    if dominant_emotion == "None":
        return "Invalid text! Please try again!."

    return f"For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."

@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
