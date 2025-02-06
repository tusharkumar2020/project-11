# server.py 
# Emotion detection Flask application from text input.

from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    # Endpoint to analyse the emotions of the given text.
    text_to_analyse = request.args.get('textToAnalyze') 

    # Call the emotion_detector function
    response = emotion_detector(text_to_analyse) 

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
   
    return render_template('index.html')

if __name__ == '__main__': 
    app.run(host="0.0.0.0", port=5000, debug=True)
           
