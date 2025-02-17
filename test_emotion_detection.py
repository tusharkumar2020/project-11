import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    """Pruebas unitarias para la función emotion_detector."""

    def test_joy(self):
        """Prueba si la emoción dominante es 'joy'."""
        result = emotion_detector("I am glad this happened")
        self.assertIn("dominant_emotion", result)
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_anger(self):
        """Prueba si la emoción dominante es 'anger'."""
        result = emotion_detector("I am really mad about this")
        self.assertIn("dominant_emotion", result)
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_disgust(self):
        """Prueba si la emoción dominante es 'disgust'."""
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertIn("dominant_emotion", result)
        self.assertEqual(result["dominant_emotion"], "disgust")

    def test_sadness(self):
        """Prueba si la emoción dominante es 'sadness'."""
        result = emotion_detector("I am so sad about this")
        self.assertIn("dominant_emotion", result)
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_fear(self):
        """Prueba si la emoción dominante es 'fear'."""
        result = emotion_detector("I am really afraid that this will happen")
        self.assertIn("dominant_emotion", result)
        self.assertEqual(result["dominant_emotion"], "fear")

if __name__ == "__main__":
    unittest.main()


