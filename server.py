from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector_view():
    """Analyze the text for emotions and return the results."""
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the emotion scores and dominant emotion from the response
    emotions = response.get('emotion_scores', {})
    dominant_emotion = response.get('dominant_emotion')

    # Check if the dominant emotion is None, indicating an error or invalid input
    if dominant_emotion is None:
        return "Invalid text! Please try again."
    
    # Format the output as required
    formatted_response = ', '.join(
        f"'{emotion}': {score}" for emotion, score in emotions.items()
    )
    
    # Return a formatted string with the sentiment label and score
    return (
        f"For the given statement, the system response is {formatted_response}. "
        f"The dominant emotion is '{dominant_emotion}'."
    )

@app.route("/")
def render_index_page():
    """Render the index page."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
