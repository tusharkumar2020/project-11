from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detection

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_api():
    data = request.json
    text_to_analyze = data.get("text", "")
    
    if not text_to_analyze:
        return jsonify({"error": "No text provided for analysis."}), 400
    
    result = emotion_detection.emotion_detector(text_to_analyze)
    
    # Formatting the output as requested
    response_text = (f"For the given statement, the system response is 'anger': {result['anger']}, 'disgust': {result['disgust']}, "
                     f"'fear': {result['fear']}, 'joy': {result['joy']} and 'sadness': {result['sadness']}. "
                     f"The dominant emotion is {result['dominant_emotion']}.")
    
    return jsonify({"response": response_text, "data": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)