import unittest
from EmotionDetection.emotion_detection import sentiment_analysis  # Adjust the import based on your structure

class TestSentimentAnalysis(unittest.TestCase):
    
    def test_positive_sentiment(self):
        result = sentiment_analysis("I am so happy I am doing this.")
        self.assertEqual(result['polarity'], 4)  #

    def test_negative_sentiment(self):
        result = sentiment_analysis("I am really mad about this.")
        self.assertEqual(result['polarity'], 2)  

    def test_disgusted_sentiment(self):
        result = sentiment_analysis("I feel disgusted just hearing about this.")
        self.assertEqual(result['polarity'], 2)  

    def test_sad_sentiment(self):
        result = sentiment_analysis("I am so sad about this.")
        self.assertEqual(result['polarity'], 0)  

    def test_fearful_sentiment(self):
        result = sentiment_analysis("I am really afraid that this will happen.")
        self.assertEqual(result['polarity'], 2)  

if __name__ == '__main__':
    unittest.main()
