''' 
server.py
Emotion detection Flask application from text input.
'''
from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    '''
        Endpoint to analyse the emotions of the given text.
    '''
    text_to_analyse = request.args.get('textToAnalyze')

    if not text_to_analyse:  # if NO text, return status 400 with None to all fields.
        response_none_data = {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
        # Bad Request
        app.logger.warning('GET/ emotionDetector?textToAnalyze= HTTP/1.1 400 - Bad Request')

        if response_none_data['dominant_emotion'] is None:
            return "Invalid text! Please try again."

    # Call the emotion_detector function
    response = emotion_detector(text_to_analyse)

    # Give error if there is problem with API !
    if "error" in response:
        return jsonify(response), 500

    formatted_response = (
        f"For the given statement, the system response is " f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )
    return formatted_response  # jsonify({"response": formatted_response})

@app.route("/")

def render_index_page():
    """
        Start Web Page with the index.html file in the templates folder.
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
    