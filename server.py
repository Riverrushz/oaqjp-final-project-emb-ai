from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")



@app.route("/emotionDetector")
def sent_analyzer():
    
    text_to_analyze = request.args.get('textToAnalyze')

    
    response = emotion_detector(text_to_analyze)

    
    emotion = response['dominant_emotion']
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']

    
    return "For the given statement, the system response is 'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {}, 'sadness': {}. The dominant emotion is {}.".format(anger_score,disgust_score,fear_score,joy_score,sadness_score,emotion)



@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    

