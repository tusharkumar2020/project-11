"""
importing the necessary modules
"""
from flask import Flask, request, render_template, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET", "POST"])
def emotion_api():
    """This function is for the api"""
    text_to_analyze = request.args.get("textToAnalyze")
    if not text_to_analyze:
        return jsonify({"error": "No text provided!"}), 400

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    return jsonify({
        "response": (
            f"For the given statement, the system response is "
            f"'anger': {response['anger']}, "
            f"'disgust': {response['disgust']}, "
            f"'fear': {response['fear']}, "
            f"'joy': {response['joy']}, "
            f"'sadness': {response['sadness']}. "
            f"The dominant emotion is {response['dominant_emotion']}."
        )
    })

@app.route("/")
def render_index_page():
    """This function renders the html"""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
