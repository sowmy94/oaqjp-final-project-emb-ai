"""
Flask web application for emotion detection.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/EmotionDetection", methods=["POST"])
def detect_emotion():
    """
    Handle POST request for emotion detection.
    """
    text = request.form.get("text")

    # Call emotion detector
    result = emotion_detector(text)

    dominant_emotion = result.get('dominant_emotion')

    # Handle blank/invalid input
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']}, "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return response

@app.route("/")
def render_index_page():
    """
    Render the index page.
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
