# coding=utf-8
import requests
import datetime
import time

username = "YOUR_USER_NAME"
password = "YOUR_PASSWORD"
ttg = "https://totheglory.im/"
ttgPayload = {'username': (None, username),
              'password': (None, password),
              'passid': (None, "0"),
              'lang': (None, "0"),
              'rememberme': (None, "no"),
              'otp': (None, ""),
              'passan': (None, ""),
              }

# TTG
myHeaders = {
    "x-requested-with": "XMLHttpRequest",
    "Accept": '''*/*''',
    "Accept-Encoding": '''gzip, deflate''',
    "Accept-Language": '''en-GB''',
    "Connection": "Keep-Alive",
    "Cache-Control": '''no-cache''',
    "Host": "totheglory.im",
    'User-Agent': '''Mozilla/4.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'''
}


def getsingnedTimeStamp(loginTimeStamp):
    loginTime = datetime.datetime.fromtimestamp(int(loginTimeStamp))
    singnedTime = (loginTime + datetime.timedelta(minutes=2))
    # singnedTime = datetime.datetime.now()
    return str(int(time.mktime(singnedTime.timetuple())))


with requests.Session() as s:
    r = s.post(ttg + "takelogin.php", files=ttgPayload, allow_redirects=False)
    r.encoding = "utf-8"
    print r.text
    print r.request.headers
    print r.status_code
    signed_timestamp = dict(r.cookies)["laccess"]
    signed_token = dict(r.cookies)["pass"]

    print "-" * 100

    # u = s.get("https://totheglory.im/browse.php?c=M")
    # u.encoding ="utf-8"
    # print u.headers
    # print u.text
    # print dict(r.cookies)

    signed = {"signed_timestamp": signed_timestamp, "signed_token": signed_token}
    t = s.post(ttg + "signed.php", headers=myHeaders, data=signed)
    for i in t.request.headers:
        print i, t.request.headers[i]
    print t.request.body

    t.encoding = "utf-8"
    print t.text
    print t.headers

