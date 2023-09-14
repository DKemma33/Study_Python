# https://hyunmin1906.tistory.com/276
import smtplib, ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "test.eastshine@gmail.com"
receiver_email = "jangdh51@gmail.com"
password = "pqcfwaikgbulwxse"
message = "<h1>똑바로 하자</h1>"

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
