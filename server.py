from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    data = request.get_json()
    text = data.get('text', '')

    response = emotion_detector(text)

    if response['dominant_emotion'] is None:
        return jsonify({"response": "Invalid text! Please try again!"}), 400

    formatted_response = (f"For the given statement, the system response is "
                          f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
                          f"'fear': {response['fear']}, 'joy': {response['joy']} and "
                          f"'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}.")
    
    return jsonify({"response": formatted_response})

if __name__ == '__main__':
    app.run(debug=True)
