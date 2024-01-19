# ยิง API แปลภาษา

import requests

response = requests.post(
    url="https://text-translator2.p.rapidapi.com/translate",
    headers= {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "e5ce54d008msh309c627db9a6be4p1500bcjsn77bd8c661ae5",
        "X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
    },
    data={
        "source_language": "en",
        "target_language": "th",
        "text": "What is your name?"
    }
)

print(response.json()["data"]['translatedText'])