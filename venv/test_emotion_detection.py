import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotion(unittest.TestCase):
    def test_emotion_detector(self):
        self.assertEqual(emotion_detector("I am glad this happened"), "joy")
        self.assertEqual(emotion_detector("I am really mad about this"), "anger")
        self.assertEqual(emotion_detector("I feel disgusted just hearing about this"), "disgust")
        self.assertEqual(emotion_detector("I am so sad about this"), "sadness")
        self.assertEqual(emotion_detector("I am really afraid that this will happen"), "fear")


unittest.main()