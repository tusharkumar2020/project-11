""" Import flask, render_tempalate, request from flask
import emotion_detector from EmotionDetection.emotion_detection package
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
#  Initiate the Flask app
app = Flask('Emotion Detection')

@app.route('/emotionDetector')
def analyzer():
    """ Analysis the response and return the sentiment emotion and dominent emotion """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return 'Invalid text! Please try again!.'
    # Return a formatted string with the sentiment emotion and dominent emotion
    return f"For the given statement, the system response is 'anger': {response['anger']},\
     'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']},\
     and 'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."

@app.route('/')
def render_index_page():
    """ Render an index.html file"""
    return render_template('index.html')

if __name__ == "__main__":
    # Host on the 5000 port
    app.run(host="0.0.0.0", port=5000)
