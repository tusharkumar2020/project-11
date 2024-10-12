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
    
    return "For the given statement, the system response is {}".format(response)

if __name__ == '__main__':
    app.run(debug=True)