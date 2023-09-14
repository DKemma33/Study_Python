# https://hyunmin1906.tistory.com/276
import smtplib, ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "test.bbori@gmail.com"
password = "nluchuyeobdzqbrb"

def send_certification_number_by_email(*args):
    receiver_email, message = args

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.encode('utf-8'))

    return message

