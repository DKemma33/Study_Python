def add(number1, number2):
    return number1 + number2


def getTotal(*numbers):
    total = 0
    for i in numbers:
        total += i
    return total