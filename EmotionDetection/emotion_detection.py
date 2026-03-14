import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, json=obj, headers=headers)
    formatted_response = response.json()
    
    # Extract emotion scores from the first item in 'emotionPredictions'
    emotions = formatted_response.get('emotionPredictions', [{}])[0].get('emotion', {})
    
    # Round scores to 1 decimal place
    anger_score = round(emotions.get('anger', 0), 1)
    disgust_score = round(emotions.get('disgust', 0), 1)
    fear_score = round(emotions.get('fear', 0), 1)
    joy_score = round(emotions.get('joy', 0), 1)
    sadness_score = round(emotions.get('sadness', 0), 1)
    
    scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    
    # Determine dominant emotion by highest rounded score
    dominant_emotion = max(scores, key=scores.get)
    
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }