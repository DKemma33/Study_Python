# packing과 unpacking
# 함수 선언 시 매개변수에 한 번에 받을 것인지(packing)
# 따로 따로 분리해서 받을 것인지(unpacking)를 선택할 수 있다.

# unpacking
# 매개변수: a, b, c
# 사용 시: (*datas)

# packing
# 매개변수: *args(가변인자)
# 사용 시: (*datas)


def sub(number1, number2, number3):
    return number1 - number2 - number3


data = 1, 2, 3

# unpacking
result = sub(*data)
print(result)


def sub(*args):
    result = 0
    for i in args:
        result -= i


datas = 1, 2, 3
# packing
sub(*datas)

# n개 정수의 합
# 매개변수의 개수를 알 수 없을 때에는 가변인자(*args)로 선언한다.
# 가변인자는 Tuple 타입이며, 전달할 대에는 ,로 여러 개의 값을 전달할 수 있다.


# packing
def getTotal(*numbers):
    total = 0
    for i in numbers:
        total += i

    return total


datas = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

result = getTotal(*datas)
print(result)

# unpacking
# def getTotal(number1, number2, number3):
#     return number1 + number2 + number3
#
#
# datas = 1, 2, 3
# result = getTotal(*datas)
# print(result)


# 함수 정의시 매개변수 첫 번째에 *를 명시하면
# 반드시 명시적으로 매개변수명을 사용하여 호출하든지
# 언패킹 등을 활용해서 묶은 뒤 호출해야 한다.
def print_info(*, name, email):
    print(name, email)


# print_info('han', 'han@gmail.com')
# print_info(**{'name': 'han', 'email': 'han@gmail.com'})
print_info(name='han', email='han@gmail.com')







