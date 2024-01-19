# แปลงข้อความเป็นเสียงพูด

import requests

response = requests.post(
    url="https://api-voice.botnoi.ai/api/service/generate_audio",
    headers={
        'Botnoi-Token': 'Wk95aTlpZVFPelk0RERtc3pJUjNlVE1Edk5JMjU2MTg5NA==',
        'Content-Type': 'application/json'
    },
    json={
        "text": "สวัสดีครับ ผมกำลังเรียนรู้เรื่อง API",
        "speaker": "8",
        "volume": 1,
        "speed": 1,
        "type_media": "m4a",
        "save_file": True
    }
)

if response.status_code == 200:
    print(response.json()["audio_url"])
else:
    print("ทำงานผิดพลาด")