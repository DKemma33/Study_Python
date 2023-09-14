string1 = "hello"
string2 = "python"

print(string1 + string2)
print(string1.__add__(string2))

print("*" * 10)
print(string2.__mul__(50))

score = [number * 10 for number in range(1, 6)]
print(score[1])
print(score.__getitem__(1))

print('e' in string1)
print(string1.__contains__('e'))


class A:
    number = 10

    def __add__(self, other):
        return A.number + other.number


a = A()
a.number = 20

print(a.__add__(a))


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"{self.name}, {self.age}"


han = Student('한동석', 20)
print(han.name, han.age)
print(han)

class Memory:

    @classmethod
    def __new__(cls, *args, **kwargs):
        print('메모리 할당')
        obj = super().__new__(cls)
        return obj

    def __init__(self, data):
        print('초기화')
        self.data = data


memory = Memory(10)
print(memory.data)

