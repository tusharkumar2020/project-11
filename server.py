from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector  # Import the function

app = Flask(__name__)

# Route to serve the web application
@app.route("/")
def home():
    return render_template("index.html")

# Route to handle emotion detection
@app.route("/emotionDetector", methods=["POST"])
def detect_emotion():
    try:
        # Get text input from request
        data = request.get_json()
        text_to_analyze = data.get("text", "")

        if not text_to_analyze:
            return jsonify({"error": "No text provided"}), 400

        # Call the emotion detection function
        result = emotion_detector(text_to_analyze)

        # Check if dominant_emotion is None
        if result.get('dominant_emotion') is None:
            return jsonify({"error": "Invalid text! Please try again!"}), 400

        # Format the response as requested
        response_text = (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, 'joy': {result['joy']} and "
            f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
        )

        return jsonify({"message": response_text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)


