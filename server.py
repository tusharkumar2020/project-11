from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import sentiment_analysis

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector():
    """Handles incoming POST requests to analyze the emotion of the provided text.

    Returns:
        JSON response containing emotion scores and the dominant emotion or an error message.
    """
    data = request.get_json()
    text = data.get('text', '').strip()
    
    # Check for blank input
    if not text:
        return jsonify({"error": "No text provided"}), 400

    result = sentiment_analysis(text)
    
    emotions = {
        "anger": 0.0,
        "disgust": 0.0,
        "fear": 0.0,
        "joy": 0.0,
        "sadness": 0.0
    }

    # Adjust this mapping based on observed polarities
    if result['polarity'] == 4:
        emotions["joy"] = 1.0
    elif result['polarity'] == 2:
        emotions["fear"] = 1.0
    elif result['polarity'] == 1:
        emotions["disgust"] = 1.0
    elif result['polarity'] == 0:
        emotions["sadness"] = 1.0

    dominant_emotion = max(emotions, key=emotions.get)

    # Check if the dominant emotion is valid
    if emotions[dominant_emotion] == 0.0:
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    response = {
        **emotions,
        "dominant_emotion": dominant_emotion
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
