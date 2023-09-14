import hmac
import hashlib

api_key = "NCSU79HJUQFATMNU"
date = "2023-07-13T12:00:00Z"
salt = "Jj8xyDixpYHLkl"
secret_key = "PJWN6YD6WAS88GKGUWK0L5XRPFCZKKR5"

concatenated_string = f"apiKey={api_key}, date={date}, salt={salt}"
signature = hmac.new(secret_key.encode(), concatenated_string.encode(), hashlib.sha256).hexdigest()

print(signature)
