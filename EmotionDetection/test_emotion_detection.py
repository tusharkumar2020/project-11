import pytest
from EmotionDetection import emotion_detection  # Asegúrate de importar la funcionalidad que deseas probar

def test_emotion_detection():
    assert emotion_detection.detect("Estoy muy feliz") == "feliz"
    assert emotion_detection.detect("Estoy triste") == "triste"
    assert emotion_detection.detect("No sé cómo me siento") == "neutral"