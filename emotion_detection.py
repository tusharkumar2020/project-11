import requests  # Importar la biblioteca requests para manejar solicitudes HTTP
def emotion_detector(text_to_analyse):  # Definir una función llamada emotion_detector que toma una cadena como entrada (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header)  # Enviar una solicitud POST a la API con el texto y los encabezados
    return response.text  # Devolver el texto de respuesta de la API
