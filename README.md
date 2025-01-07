# Emotion Detection Flask Application

A lightweight Flask-based web application that analyzes user-provided text to detect emotions such as anger, disgust, fear, joy, and sadness. The application uses a pre-trained emotion detection model and provides detailed emotion scores along with the dominant emotion.

## Features

- Analyze text to predict emotions (anger, disgust, fear, joy, sadness).
- Returns emotion scores and identifies the dominant emotion.
- Handles blank or invalid text inputs with proper error messages.
- Easy-to-deploy Flask application for local or cloud hosting.

## Installation

1. Clone the repository:
   ```bash
   git clone 
   cd emotion-detection-flask
   ```
2. Install dependencies:

  ```bash
  pip install -r requirements.txt
  ```
  
3. Start the Flask server:
```bash
  python3 server.py
```
4. Access the application in your browser:
Visit http://127.0.0.1:5005.


#### Response
```
{
  "anger": 0.0136,
  "disgust": 0.0017,
  "fear": 0.0089,
  "joy": 0.9719,
  "sadness": 0.0552,
  "dominant_emotion": "joy"
}
```
