from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    text_to_analyze = request.args.get('textToAnalyze')

    # Call the emotion detector function
    response = emotion_detector(text_to_analyze)

    # Check if the dominant emotion is None
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    # Extract the emotions and dominant emotion from the response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Format the response for display
    formatted_response = ("For the given statement, the system response is "
                          "'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {}, "
                          "and 'sadness': {}. The dominant emotion is {}."
                          .format(anger, disgust, fear, joy, sadness, dominant_emotion))

    return formatted_response

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
