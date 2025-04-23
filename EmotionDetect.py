import requests
import json
def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
       result = json.loads(response.text)
       emotions = result['emotionPredictions'][0]['emotion']
       dominant_emotion = max(emotions, key=emotions.get)
       emotions['dominant_emotion'] = dominant_emotion 
       return emotions  # Converti la risposta in dizionario
    else:
        return {
            "error": f"Error: {response.status_code}",
            "details": response.text
        }
