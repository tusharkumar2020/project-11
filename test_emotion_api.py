import requests

# Define the URL with the updated port
url = "http://localhost:3000/emotionDetector"

# Define the payload
data = {"statement": "I think I am having fun"}

# Send the POST request
response = requests.post(url, json=data)

# Print the response
if response.status_code == 200:
    print("Test Passed!")
    print("Response:", response.json())
else:
    print("Test Failed!")
    print("Error:", response.json())
