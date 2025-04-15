'''Deploy a Flask application that will allow the user to provide a text string
and return a breakdown of five emotions conveyed by the text
'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/emotionDetector')
def emotion_analyzer():
    '''Retrieves (get) the user input text string, pass the text into the 
    emotion_detector function inside of emotion_detection.py. Error handeling
    '''
    text_to_analyse = request.args.get('textToAnalyze')
    emotion_result = emotion_detector(text_to_analyse)

    if emotion_result['dominant_emotion'] is None:
        return "Invalid text! Please try again"

    formatted_result = (
        f"For the given statement, the system response is "
        f"'anger': {emotion_result['anger']}, "
        f"'disgust': {emotion_result['disgust']}, "
        f"'fear': {emotion_result['fear']}, "
        f"'joy': {emotion_result['joy']} and "
        f"'sadness': {emotion_result['sadness']}. "
        f"The dominant emotion is {emotion_result['dominant_emotion']}."
    )
    return formatted_result

@app.route("/")
def render_index_page():
    '''Render the index page to the user. This is the page that prompts the user
    to enter text into the box and emotion detection will be returned
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
