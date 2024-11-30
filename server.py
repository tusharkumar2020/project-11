from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    # Render the index.html template
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    # Parse the statement from the POST request
    data = request.json
    statement = data.get("statement", "")
    if not statement:
        return jsonify({"error": "No statement provided"}), 400

    # Call the emotion_detector function
    result = emotion_detector(statement)

    # Format the output for the response
    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
