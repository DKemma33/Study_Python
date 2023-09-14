import json
import platform
import requests
import u_mysql.task.basic.sms.config as config
import u_mysql.task.basic.sms.auth as auth


default_agent = {
    'sdkVersion': 'python/4.2.0',
    'osPlatform': platform.platform() + " | " + platform.python_version()
}

url = "http://api.coolsms.co.kr/messages/v4/send"
headers = auth.get_headers('API KEY', 'API SECRET')


def send_certification_number(*args):
    certification_number, phone = args

    data = {
        "message": {
            "to": phone,
            "from": "발신번호",
            "text": certification_number
        }
    }
    print(json.dumps(data, ensure_ascii=False))
    response = requests.post(config.get_url('/messages/v4/send'),
                             headers=auth.get_headers(config.api_key, config.api_secret),
                             json=data)
    print(response.status_code)
    print(response.text)
    return certification_number
