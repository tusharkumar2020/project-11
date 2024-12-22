from flask import Flask
from .emotion_detection import emotion_detector

app = Flask(__name__)