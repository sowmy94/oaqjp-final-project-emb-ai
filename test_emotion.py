from EmotionDetection.emotion_detection import emotion_detector
import requests

text = "I am so happy I am doing this."
result = emotion_detector(text)
print(result)