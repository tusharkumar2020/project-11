import requests

def emotion_detector(text_to_analyze):
    # URL de la API de Watson NLP
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Encabezados necesarios para la solicitud
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Formato JSON de entrada
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    # Realizar la solicitud POST
    response = requests.post(URL, headers=headers, json=input_json)
    
    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        return response.json()  # Devolver el contenido de la respuesta como JSON
    else:
        return {"error": "Error al analizar las emociones", "status_code": response.status_code}
    