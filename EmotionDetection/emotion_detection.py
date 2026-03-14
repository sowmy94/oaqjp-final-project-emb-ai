import requests

def emotion_detector(text_to_analyze):
    # Mock response since the API is not reachable
    # In a real scenario, replace with actual API call
    mock_emotions = {
        'anger': 0.1,
        'disgust': 0.0,
        'fear': 0.2,
        'joy': 0.5,
        'sadness': 0.2
    }
    dominant_emotion = max(mock_emotions, key=mock_emotions.get)
    
    return {
        'anger': mock_emotions['anger'],
        'disgust': mock_emotions['disgust'],
        'fear': mock_emotions['fear'],
        'joy': mock_emotions['joy'],
        'sadness': mock_emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }