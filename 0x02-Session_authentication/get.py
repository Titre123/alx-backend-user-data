import requests
import base64

x = requests.get('http://127.0.0.1:5000/', cookies={"_my_session_id fake"})
y = x.text
print(y)
