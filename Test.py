import json

import requests

url = "http://127.0.0.1:5000/api/Song"

json_data = {
    "title": "two",
    "duration": 2,
}
podcast_json_data = {
    "title": "two",
    "duration": 2,
    "host": "mmm",
    "participants": ["xx", "zz", "ff", "ee"],
}
audiobook_json_data = {
    "title": "two",
    "duration": 2,
    "author": "aaa",
    "narrator": "bbb",
}
# response = requests.post("http://127.0.0.1:5000/api/Song", json=json_data)
# response = requests.post("http://127.0.0.1:5000/api/Podcast", json=podcast_json_data)
# response = requests.post("http://127.0.0.1:5000/api/Audiobook", json=audiobook_json_data)
# response = requests.put("http://127.0.0.1:5000/api/Song/7", json=json_data)
# response = requests.put("http://127.0.0.1:5000/api/Podcast/1", json=podcast_json_data)
# response = requests.put("http://127.0.0.1:5000/api/Audiobook/1", json=audiobook_json_data)
response = requests.get("http://127.0.0.1:5000/api/Podcast/1")
# response = requests.delete("http://127.0.0.1:5000/api/Song/4")

print(response.status_code, response.content)
