import json
import platform
import requests
import config
import auth


default_agent = {
    'sdkVersion': 'python/4.2.0',
    'osPlatform': platform.platform() + " | " + platform.python_version()
}


url = "http://api.coolsms.co.kr/messages/v4/send"
headers = auth.get_headers('NCSU79HJUQFATMNU', 'PJWN6YD6WAS88GKGUWK0L5XRPFCZKKR5')

data = {
    "message": {
        "to": "01062377087",
        "from": "01062377087",
        "text": "내용"
    }
}
print(json.dumps(data, ensure_ascii=False))
response = requests.post(config.get_url('/messages/v4/send'),
                         headers=auth.get_headers(config.api_key, config.api_secret),
                         json=data)
print(response.status_code)
print(response.text)
