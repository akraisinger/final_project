from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        self.assertEqual(emotion_detector("I am glad this happened")['dominant emotion'], 'joy')
        self.assertEqual(emotion_detector("I am really mad about this")['dominant emotion'], 'anger')
        self.assertEqual(emotion_detector("I feel disgusted just hearing about this")['dominant emotion'], 'disgust')
        self.assertEqual(emotion_detector("I am so sad about this")['dominant emotion'], 'sadness')
        self.assertEqual(emotion_detector("I am really afraid that this will happen")['dominant emotion'], 'fear')

unittest.main()