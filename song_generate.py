import requests
import os

API_KEY =  "cbda1568442d9391191970c30a84142a"
ENDPOINT = "https://api.suno.ai/v1/song/generate"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "prompt": "כתוב שיר שמח בעברית על קיץ וחוף הים",
    "language": "he",
    "genre": "pop"
}

response = requests.post(ENDPOINT, headers=headers, json=data)

with open("song_response.json", "w", encoding="utf-8") as f:
    f.write(response.text)

if response.ok:
    print("Song generated and saved to song_response.json")
else:
    print("Error:", response.status_code, response.text)
