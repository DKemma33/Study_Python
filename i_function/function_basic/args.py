# 가변인자: 매개변수의 개수가 정해지지 않았을 경우 사용한다.
# *args는 Tuple 타입이다.

# n개의 정수 합
def getTotal(*numbers):
    total = 0
    for i in numbers:
        total += i
    return total


result = getTotal(1, 2, 3, 4, 3, 4, 5, 6, 7)
print(result)