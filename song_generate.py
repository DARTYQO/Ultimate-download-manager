import requests
import time

BASE_URL = 'http://localhost:3000'

def generate_audio_by_prompt(prompt):
    url = f"{BASE_URL}/api/generate"
    payload = {
        "prompt": prompt,
        "make_instrumental": False,
        "wait_audio": False
    }
    response = requests.post(url, json=payload, headers={'Content-Type': 'application/json'})
    response.raise_for_status()
    return response.json()

def get_audio_information(audio_ids):
    url = f"{BASE_URL}/api/get?ids={audio_ids}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

if __name__ == '__main__':
    prompt = "כתוב שיר שמח בעברית על קיץ וחוף הים"
    print("יוצר שיר...")

    data = generate_audio_by_prompt(prompt)
    ids = ",".join([str(item['id']) for item in data])
    print(f"ids: {ids}")

    # ממתין עד שהשירים מוכנים
    for _ in range(60):
        info = get_audio_information(ids)
        if all(item.get("status") == 'streaming' for item in info):
            for item in info:
                print(f"{item['id']} ==> {item['audio_url']}")
            break
        time.sleep(5)
    else:
        print("Timeout: השירים לא הושלמו בזמן.")
