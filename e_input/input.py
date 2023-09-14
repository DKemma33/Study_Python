# name = input("이름: ")
# formatting = "{}님 환영합니다.".format(name)

# f 문자열 (3.6버전 이상)
# formatting = f"{name}님 환영합니다."
# print(formatting)

# 제 이름은 ???, 키는 ???cm
name, height = '한동석', 183.5
formatting = f'제 이름은 {name}, 키는 {height}cm'
print(formatting)

# 두 정수를 입력 받은 후 곱셈 결과 출력
# message1, message2 = "첫 번째 정수: ", "두 번째 정수: "
# number1, number2 = int(input(message1)), int(input(message2))
# result = number1 * number2
# formatting = f"{number1} * {number2} = {result}"
# print(formatting)

a, b, c = "A,B,C".split(",")
print(a, b, c, sep=",")

hour, minute = "10:30".split(":")
print(f'{hour}시 {minute}분')

print("010-1234-1234".split("-"))

name, age = "한동석 20".split(" ")
print(f'{name}님의 나이는 {age}살')

number1, number2, number3 = input("3개의 정수를 입력하세요.\n예)1 2 3\n").split(" ")
result = int(number1) + int(number2) + int(number3)
formatting = f'{number1} + {number2} + {number3} = {result}'
print(formatting)

#






