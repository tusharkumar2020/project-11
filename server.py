from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the Emotion Detection function
@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    # Get the text from the request JSON body
    text_to_analyze = request.json.get('text')
    
    # Call the emotion detection function
    response = emotion_detector(text_to_analyze)
    
    # Format the response in the required format
    response_text = (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} "
        f"and 'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."
    )
    
    # Return the formatted response as JSON
    return jsonify({"response": response_text})

# Run the application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
