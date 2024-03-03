'''
This file is routes in our emotion detection api, using BARD emotion detection
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emo_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant_emotion = response["dominant_emotion"]

    if dominant_emotion is None:
        return "Invalid input! Try again."
    text_1 = "For the given statement, the system response is "
    data_1 = f"'anger': {anger}, 'disgust': {disgust}, "
    data_2 = f"'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
    text_2 = f"The dominant emotion is {dominant_emotion}"
    return text_1 + data_1 + data_2 + text_2

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)