from flask import Flask, request, jsonify
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_endpoint():
    """
    Endpoint to process emotion detection requests.

    Accepts a JSON payload containing a statement and returns the detected emotions
    along with the dominant emotion. Handles blank input or invalid requests gracefully.
    """
    try:
        data = request.get_json()
        statement = data.get("statement", "")

        if not statement.strip():
            return jsonify({"error": "Invalid text! Please try again!"}), 400

        result = emotion_detector(statement)

        if result["dominant_emotion"] is None:
            return jsonify({"error": "Invalid text! Please try again!"}), 400

        formatted_response = (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, "
            f"'joy': {result['joy']} and "
            f"'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}."
        )
        return jsonify({"response": formatted_response}), 200
    except KeyError as key_error:
        return jsonify({"error": f"Missing key in input: {key_error}"}), 400
    except ValueError as value_error:
        return jsonify({"error": f"Invalid value: {value_error}"}), 400
    except Exception as error:
        return jsonify({"error": str(error)}), 500

@app.route('/')
def index():
    """
    Home endpoint for the API.

    Returns a simple message indicating the API is running.
    """
    return "Emotion Detection API is running!", 200

@app.route('/favicon.ico')
def favicon():
    """
    Favicon endpoint to prevent 404 errors.

    Returns an empty response.
    """
    return '', 204

if __name__ == '__main__':
    app.run(host='localhost', port=3000, debug=True)
