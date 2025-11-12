import requests
import json


def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    txtObj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post (url, json = txtObj, headers = header)

    formatted_response = json.loads(response.text)

    


    if response.status_code == 200:
            anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
            disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
            fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
            joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
            sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']

            scores = [anger_score,disgust_score,fear_score,joy_score,sadness_score]
            emotions = ['anger','disgust','fear','joy','sadness']

            dominant_emotion = 0
            for x in range(5): 
                current_emotion = scores[x]
                if current_emotion > dominant_emotion:
                    dominant_emotion = current_emotion
                    dominant_emotion_name = emotions[x]        
                return {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
                'dominant_emotion': dominant_emotion_name
                }


    elif response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None
        return "Invalid input! Try again."


    elif response.status_code == 500:
            anger_score = None
            disgust_score = None
            fear_score = None
            joy_score = None
            sadness_score = None
            dominant_emotion = None
            return "Invalid input! Try again."


