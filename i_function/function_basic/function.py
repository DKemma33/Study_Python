# 두 정수의 합
def add(number1, number2):
    return number1 + number2


result = add(1, 2)
print(result)


# 두 정수의 곱셈
def mul(number1, number2):
    return number1 * number2


result = mul(3, 4)
print(result)


# 두 정수의 나눗셈 후 몫과 나머지 구하기
def div(number1, number2):
    return number1 // number2, number1 % number2


value, rest = div(10, 3)
print(f"{value} / {rest}")


# 1~10까지 print()로 출력하는 함수
def print_from_one_to_ten():
    for i in range(10):
        print(i + 1)


print_from_one_to_ten()


# 이름을 n번 print()로 출력하는 함수
def printName(name, count):
    for i in range(count):
        print(name)


printName('한동석', 10)


# 1~n까지의 합을 구해주는 함수
def get_total_from_one(end):
    total = 0
    for i in range(end):
        # total = total + i + 1
        total += i + 1
    return total


result = get_total_from_one(10)
print(result)

# 1~100까지 중 n의 배수를 print로 출력하는 함수
# 배수 검사 : a % n == 0 -> n의 배수

def print_time_from_one_to_hundred(time):
    for i in range(100):
        if (i + 1) % time == 0:
            print(i + 1)


print_time_from_one_to_hundred(3)

# 두 정수의 뺄셈 함수
def sub(number1, number2):
    return number1 - number2

result = sub(10, 3)

print(result)

# 문자열을 입력받고 원하는 문자의 개수를 구해주는 함수


def get_count_of_search_result(string, target):
    count = 0
    for i in string:
        if i == target:
            count += 1

    return count


count = get_count_of_search_result("ABCCCC", "C")
print(count)

# 문자열과 문자를 입력받은 뒤 해당 문자가 몇 번째 인덱스에 있는 지 검사하고,
# 만약 해당 문자가 없으면 -1을 리턴한다


def get_index(string, target):
    for i in range(len(string)):
        if string[i] == target:
            return i

    return -1

    # index = -1
    # for i in range(len(string)):
    #     if string[i] == target:
    #         index = i
    #         break
    #
    # return index


index = get_index("Apple", "p")
print(index)

# 파이썬 함수는 같은 이름으로 선언 시 가장 아래에 선언된 내용으로 실행된다.
# 메소드는 저장공간이기 때문에 마지막에 들어간 소스코드의 주소값으로 반영되기 때문이다.

# 두 정수의 뺄셈 함수
def sub(number1, number2):
    return number1 - number2


# 세 정수의 뺄셈 함수
def sub(number1, number2, number3):
    return number1 - number2 - number3


# 네 정수의 뺄셈 함수
def sub(number1, number2, number3, number4):
    return number1 - number2 - number3 - number4

