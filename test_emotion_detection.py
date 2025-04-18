from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        def test_sentiment_analyzer(self):
        
        result_1 = emotion_detection('I am glad this happened')
        self.assertEqual(result_1['label'], 'joy')