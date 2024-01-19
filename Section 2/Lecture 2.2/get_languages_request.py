# ยิง API ดูภาษาที่รองรับ

import requests

response = requests.get(
    url= 'https://text-translator2.p.rapidapi.com/getLanguages',
    headers={
        'X-RapidAPI-Key': 'e5ce54d008msh309c627db9a6be4p1500bcjsn77bd8c661ae5',
        'X-RapidAPI-Host': 'text-translator2.p.rapidapi.com'
    }
)

languages = response.json()["data"]["languages"]

print(type(languages))

