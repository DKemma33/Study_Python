number = 15

if number % 3 == 0:
    print(f"{number}는 3의 배수입니다.")
if number % 5 == 0:
    print(f"{number}는 5의 배수입니다.")

# number가 양수인지, 음수인지, 0인지 검사
positive_condition = number > 0
negative_condition = number < 0
zero_condition = number == 0

if positive_condition:
    print(f"{number}는 양수입니다.")
elif negative_condition:
    print(f"{number}는 음수입니다.")
else:
    print(f"{number}")

# 나이 입력 받기
# 미성년자인지 검사
message = "나이: "
age = input(message)
adult_check = int(age) > 19

if adult_check:
    print("성인입니다.")
else:
    print("미성년자입니다.")
# if not adult_check:
#     print("미성년자입니다.")

message, example_message = "정수 2개를 입력하세요.", "ex)1 5\n"
data1, data2 = input(message + "\n" + example_message).split(" ")
number1, number2 = int(data1), int(data2)

if number1 > number2:
    print(f"큰 값: {number1}")
elif number1 != number2:
    print(f"큰 값: {number2}")
else:
    print("두 수가 같습니다.")


