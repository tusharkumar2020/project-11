from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_analyzer():

    text_to_analyze = request.args.get('textToAnalyze')
    emotion_result = emotion_detector(text_to_analyze)
    
    if emotion_result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    else:
        anger = emotion_result.get('anger', 0.0)
        disgust = emotion_result.get('disgust', 0.0)
        fear = emotion_result.get('fear', 0.0)
        joy = emotion_result.get('joy', 0.0)
        sadness = emotion_result.get('sadness', 0.0)
        dominant_emotion = emotion_result.get('dominant_emotion', '')

        formatted_response = (
            f"For the given statement, the system response is 'anger': {anger}, "
            f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
            f"The dominant emotion is {dominant_emotion}."
        )
        return formatted_response

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)