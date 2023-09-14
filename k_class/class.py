class A:
    # 클래스 변수(static)
    name = "A"

    # 생성자
    def __init__(self, data=0):
        print(self)
        self.data = data


print(A.name)


# 클래스 이름 뒤에 소괄호: 생성자
# a = A(10)
# b = A()
# print(a)
# print(b)
# print(a.data)
# print(b.data)
