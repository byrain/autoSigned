# coding=utf-8
import requests

ourBitsUrl = "https://ourbits.club/"

username = "YOUR_USER_NAME"
password = "YOUR_PASSWORD"
obPayload = {'username': username, 'password': password}

with requests.Session() as s:
    r = s.post(ourBitsUrl+"takelogin.php", data=obPayload)
    print r.headers
    t = s.get(ourBitsUrl+"attendance.php")
    print t.text
    print t.headers
