# 여러 개의 변수를 한 줄에 선언
a = 10; b = 20; c = 30
print(a, b, c)

a, b, c = 100, 200, 300
print(a, b, c)

# 변수의 값을 서로 바꾸기
a = 11
b = 33
print(a, b)

temp = a
a = b
b = temp

print(a, b)

a, b = b, a
print(a, b)

a = 10
print(type(a))
a = 10.5
print(type(a))
a = 'A'
print(type(a))
a = "ABC"
print(type(a))
a = ['A', 'B', 'C']
print(type(a))
a = {'A': 1, 'B': 2, 'C': 3}
print(type(a))
a = True
print(type(a))

age = 10
print(type(age))
score = 10.5
print(type(score))
grade = 'A'
print(type(grade))
data = "ABC"
print(type(data))
course = ['A', 'B', 'C']
print(type(course))
level = {'A': 1, 'B': 2, 'C': 3}
print(type(level))
room_number = {1, 2, 3}
print(type(room_number))
check = True
print(type(check))


# 반올림에서 5 미만의 숫자는 버림하며 5 초과의 숫자는 올림한다.
# 5의 경우에는 5의 앞자리가 홀수인 경우엔 올림을 하고 짝수인 경우엔 버림을 하여 짝수로 만들어준다.
# 예를 들어 53.45는 53.4로, 32.75는 32.8로 반올림한다.
# 이를 오사오입(round-to-nearest-even)이라고 한다.

# 참고: https://ko.wikipedia.org/wiki/%EB%B0%98%EC%98%AC%EB%A6%BC

name = "한동석"
age = 10
print("이름: %s " % name)
print("나이: %d살", age)
# print("키: %.1f" % 183.55)
print("키: %.1f" % round(183.55 + 0.0000000001, 1))
print("이름: %s\n나이: %d\n키: %.2fcm\n" % (name, age, 183.45))

# 실습
# 정수 2개를 변수에 담기
# 두 정수의 합을 아래 형식으로 출력하기
# 1 + 3 = 4

number1 = 1
number2 = 3
result = number1 + number2

print("%d + %d = %d" % (number1, number2, result))

# format 함수
formatting = "{} + {} = {}".format(number1, number2, result)
print(formatting)

formatting = "{1} + {0} = {2}".format(number1, number2, result)
print(formatting)

formatting = "{number1} + {number2} = {result}".format(number1=number1, number2=number2, result=result)
print(formatting)

# 실습
# 이름과 나이를 변수에 담는다
# format()을 사용해서 출력

name = '한동석'
age = 20

# print(type(name))
# print(type(age))

formatting = "이름: {}, 나이: {}살".format(name, age)
print(formatting)

formatting = "나이: {1}살, 이름: {0}".format(name, age)
print(formatting)

formatting = "이름: {name}, 나이: {age}살".format(name=name, age=age)
print(formatting)

# 아래 메세지 출력
# Hello 파이썬, Python is fantastic
# Hello 리액트, React.js is fantastic
# Hello 장고, Django is fantastic

formatting = "Hello {1}, {0} is fantastic"
kor, eng = "파이썬", "Python"
print(formatting.format(kor, eng))

kor, eng = "리액트", "React.js"
print(formatting.format(kor, eng))

kor, eng = "장고", "Django"
print(formatting.format(kor, eng))


