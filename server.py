from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detection():
    text_to_analyze = str(request.args.get('textToAnalyze'))
    response = emotion_detector(text_to_analyze)
    
    if not response:
        return "Invalid text! Please try again!"
    response_str = ", ".join(
        f"'{key}': {value}" for key, value in response.items())
    response_arr = response_str.split(", 'dominant_emotion':")
    response_str = "For the given statement, the system response is " + response_arr[0] + ". The dominant emotion is <b>" + response_arr[1]+"</b>."
    return response_str

if __name__ == '__main__':
    app.run(debug=True)
