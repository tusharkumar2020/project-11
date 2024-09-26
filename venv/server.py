from flask import Flask, jsonify
from flask import make_response
from flask import request
from EmotionDetection.emotion_detection import emotion_detector


app = Flask(__name__)

@app.route("/emotionDetector")
def get_emotion_detected():
    text_to_analyze = request.args.get("q")
    emotion_results = emotion_detector(text_to_analyze)

    # Create the response string
    emotions_str = ', '.join(
        [f"'{key}': {value}" for key, value in emotion_results.items() if key != 'dominant_emotion']
    )
    dominant_emotion = emotion_results['dominant_emotion']

    # Format the output
    response_message = (
        f"For the given statement, the system response is {emotions_str}. "
        f"The dominant emotion is <strong>{dominant_emotion}</strong>."
    )

    return jsonify({"message": response_message})


app.run(port=5000, debug=True)