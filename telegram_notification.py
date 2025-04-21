import requests

chat_id = ''
text = ' this is a test and message goes here'
api = ''
url = f'https://api.telegram.org/bot{api}/sendMessage'

data = {
    'chat_id': chat_id,
    'text': text
}

response = requests.post(url, data=data)

# Print the response status code and content (optional)
print(f"Status Code: {response.status_code}")
print("Response Content:")
print(response.text)
