# 만약 값을 매개변수로 전달하지 않았을 경우
# 기본 값을 설정하기 위해서는 arg=default_value로 설정한다

def sub(number1, number2, number3, number4=0):
    return number1 - number2 - number3 - number4


result = sub(1, 2, 3)
print(result)


def get_info(name='익명', age=0):
    return {"name": name, "age": age}


print(get_info('한동석', 20))