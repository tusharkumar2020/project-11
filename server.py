from flask import Flask,request,render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Analyser")

@app.route("/emotionDetector")
def self_detection():
    text_to_analyse = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyse)
    
    return f"For the given statement, the system response is {response}. The dominant emotion is {response['dominant_emotion']}"

@app.route("/")
def html_index_page():
    return render_template('index.html')    

if __name__ == "__main__":
     app.run(host="0.0.0.0", port=5000)   