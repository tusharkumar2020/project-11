import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):  # Corrected the inheritance here
    def test_emotion_detector(self):
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1['dominant_emotion'], 'joy')  # Corrected the key to 'dominant_emotion'

        result_2 = emotion_detector('I am really mad about this')
        self.assertEqual(result_2['dominant_emotion'], 'anger')  # Corrected the key to 'dominant_emotion'
        
        result_3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_3['dominant_emotion'], 'disgust')  # Corrected the key to 'dominant_emotion'

        result_4 = emotion_detector('I am so sad about this')
        self.assertEqual(result_4['dominant_emotion'], 'sadness')  # Corrected the key to 'dominant_emotion'

        result_5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result_5['dominant_emotion'], 'fear')  # Corrected the key to 'dominant_emotion'


if __name__ == '__main__':  # Ensures the test runs only if this file is executed directly
    unittest.main()
