# Import the 'unittest' module to create unit tests for your code.
import unittest

# Import the 'emotion_detector' function from the 'EmotionDetection' module.
from EmotionDetection.emotion_detection import emotion_detector

# Define a test case class for testing the 'emotion_detection' function.
class TestEmotion(unittest.TestCase): 
    # Define the first test method for the 'emotion_detector' function.
    def test1(self): 
        # Check that the sentence "I am glad this happened" returns "Joy"
        input_text = "I am glad this happened"
        result = emotion_detector(input_text)
        self.assertEqual(result['dominant_emotion'], 'joy')
    
    def test2(self): 
        # Check that the sentence "I am really mad about this" returns "anger"
        input_text = "I am really mad about this"
        result = emotion_detector(input_text)
        self.assertEqual(result['dominant_emotion'], 'anger')
    
    def test3(self): 
        # Check that the sentence "I feel disgusted just hearing about this" returns "disgust"
        input_text = "I feel disgusted just hearing about this"
        result = emotion_detector(input_text)
        self.assertEqual(result['dominant_emotion'], 'disgust')
    
    def test4(self): 
        # Check that the sentence "I am so sad about this" returns "sadness"
        input_text = "I am so sad about this"
        result = emotion_detector(input_text)
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test5(self): 
        # Check that the sentence "I am really afraid that this will happen" returns "fear"
        input_text = "I am really afraid that this will happen"
        result = emotion_detector(input_text)
        self.assertEqual(result['dominant_emotion'], 'fear')
        
if __name__ == '__main__':
    unittest.main()