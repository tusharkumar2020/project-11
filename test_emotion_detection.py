"""This module is for make unit testing on the emotion_detection module
"""
import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    """this class is to introduce some test cases related to emotion_detection module

    Args:
        unittest (testcase): this is to inherit TestCase from the unittest module
    """
    def test_emotion_detector(self):
        """make some test cases related to emotion_detector function inside the emotion_detection module
        """
        #test whether the emotion_detector return the dominant_emotion of the json is equal to joy
        self.assertEquals(emotion_detector("I am glad this happened")['dominant_emotion'],'joy')
        #test whether the emotion_detector return the dominant_emotion of the json is equal to anger
        self.assertEquals(emotion_detector("I am really mad about this")['dominant_emotion'],'anger')
        #test whether the emotion_detector return the dominant_emotion of the json is equal to disgust
        self.assertEquals(emotion_detector("I feel disgusted just hearing about this")['dominant_emotion'],'disgust')
        #test whether the emotion_detector return the dominant_emotion of the json is equal to sadness
        self.assertEquals(emotion_detector("I am so sad about this")['dominant_emotion'],'sadness')
        #test whether the emotion_detector return the dominant_emotion of the json is equal to fear
        self.assertEquals(emotion_detector("I am really afraid that this will happen")['dominant_emotion'],'fear')
unittest.main()
