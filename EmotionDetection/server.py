from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods = ['POST'])
def emotion_detector_api():
    # Obtém o texto do corpo da requisição JSON
    data = request.get_json()
    text_to_analyze = data.get('text')

    # Processa o texto usando a função emotion_detector
    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    if not text_to_analyze:
        return jsonify({"error": "No text provided"}), 400
    
    # Formata a resposta como uma string no formato solicitado
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return response_text, 200

if __name__ == '__main__':
    app.run(debug = False)
