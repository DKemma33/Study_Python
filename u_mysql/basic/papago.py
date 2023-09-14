# https://developers.naver.com/docs/papago/papago-nmt-overview.md
# DOiYKHelQeLPpbdvYfWw
# woFunxiYgB

import os
import sys
import urllib.request
import json

client_id = "DOiYKHelQeLPpbdvYfWw" # 개발자센터에서 발급받은 Client ID 값
client_secret = "woFunxiYgB" # 개발자센터에서 발급받은 Client Secret 값
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)


def translate(message):
    encText = urllib.parse.quote(message)
    data = "source=ko&target=en&text=" + encText
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    response_code = response.getcode()

    if response_code == 200:
        response_body = response.read()
        # 받은 데이터는 json이다.
        # print(response_body.decode('utf-8'))
        # json.loads(json)을 사용하여 dict로 변환한다.
        return json.loads(response_body.decode('utf-8'))["message"]["result"]["translatedText"]
    else:
        raise RuntimeError







