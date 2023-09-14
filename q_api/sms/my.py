import requests
import datetime

url = "http://api.coolsms.co.kr/messages/v4/send"

headers = {
  "Authorization": "HMAC-SHA256 apiKey=NCSU79HJUQFATMNU, date=2023-07-12T00:41:48Z, salt=Jj8xyDixpYHLkl, signature=12c83d00b8c11f3ecbde7b8126b49dae89fafaff89792b892f086f9108058a96",
  "Content-Type": "application/json"
}
current_date = datetime.date.today().strftime("%Y-%m-%d")
data = '{"message":{"to":"01058073170","from":"01062377087","text":"Today is {current_date}. Hello, this is a test message!"}}}'

response = requests.post(url, headers=headers, data=data)
print(response.status_code)
print(response.text)



