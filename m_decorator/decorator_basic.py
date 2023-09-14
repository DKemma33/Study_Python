# 스터디
# 여러 함수에서 동일한 코드가 반복된다? -> 데코레이터 만들자!

# 실무
# 붙이라고 하니까 붙이자!

def 데코레이터이름(원래함수):
    def 주변로직(원래함수가받은거):
        완성코드 = 원래함수가받은거 + "님"
        원래함수(완성코드)

    return 주변로직

@데코레이터이름
def 원래함수(이름):
    print(이름)
    
원래함수('한동석')

# 나이를 전달받은 뒤 나이 뒤에 '살'을 붙여 출력
def add_sal(original):
    def change(age):
        original(str(age) + '살')

    return change


@add_sal
def print_age(age):
    print(age)

print_age(10)







