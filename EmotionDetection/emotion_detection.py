from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def emotion_detector():

    data = request.get_json() 
    text_to_analyze = data.get('text', '')

    if not text_to_analyze:
        return jsonify({"error": "No text provided"}), 400

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }    

    json_input = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, headers=headers, json=json_input)

    if response.status_code == 200:
        response_data = response.json()
        
        emotion_data = response_data['emotionPredictions'][0]['emotion']
        
        anger_score = emotion_data.get('anger', 0)
        disgust_score = emotion_data.get('disgust', 0)
        fear_score = emotion_data.get('fear', 0)
        joy_score = emotion_data.get('joy', 0)
        sadness_score = emotion_data.get('sadness', 0)

        emotions = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }

        dominant_emotion = max(emotions, key=emotions.get)

        result = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
        
        return jsonify(result)  
    else:
        return jsonify({"error": "Failed to analyze emotion"}), 500
    

if __name__ == '__main__':
    app.run(debug=True)