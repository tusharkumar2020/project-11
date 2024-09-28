import requests

def sentiment_analysis(text):
    url = 'http://www.sentiment140.com/api/bulkClassifyJson'
    data = {
        "data": [
            {
                "text": text
            }
        ]
    }

    response = requests.post(url, json=data)
    result = response.json()
    
    sentiment = result['data'][0]
    return {
        'text': sentiment['text'],
        'polarity': sentiment['polarity']
    }

# Test the function
result = sentiment_analysis("I am really afraid that this will happen")
print(result)
