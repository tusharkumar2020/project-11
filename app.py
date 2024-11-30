from EmotionDetector import emotion_detector

if __name__ == "__main__":
    # Test the emotion detector locally
    statement = input("Enter a statement to analyze: ")
    result = emotion_detector(statement)
    print("Emotion Analysis Result:")
    print(result)
