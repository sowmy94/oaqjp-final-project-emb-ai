from EmotionDetection.emotion_detection import emotion_detector
import requests

text = " I hate working long hours"
result = emotion_detector(text)
print(result)