# email을 입력받고 아이디(email_id)와 도메인(domain)을 각각 변수에 담고 출력
# message = "이메일 입력: "
# email_id, domain = input(message).split("@")
#
# print(f"아이디: {email_id}")
# print(f"도메인: {domain}")

# message1 = "아이디: "
# message2 = "도메인: "
#
# email_id = input(message1)
# domain = input(message2)
#
# print(email_id, domain, sep="@")

'''
첫 번째 값으로 야드를 입력받고, 두 번째 값으로 인치를 입력받아서
각각 cm로 변환하여 다음 형식에 맞추어 소수점 둘 째자리까지 출력한다.

1yd: 91.44cm
1in: 2.54cm

예)
    yard 입력: 10
    inch 입력: 10

    10 yard는 914.4cm
    10 inch는 25.4cm
'''

message1, message2 = "yard: ", "inch: "
yard, inch = float(input(message1)), float(input(message2))
yard_to_cm, inch_to_cm = round(yard * 91.44, 2), round(inch * 2.54, 2)
formatting = f'{yard} yard는 {yard_to_cm}cm\n{inch} inch는 {inch_to_cm}cm'
print(formatting)




