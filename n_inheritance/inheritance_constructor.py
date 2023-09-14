class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print("두 발로 걷기")


class Monkey(Human):
    def __init__(self, name, age, zoo):
        super().__init__(name, age)
        self.zoo = zoo

    # Overriding: 재정의
    # 부모의 메소드이름과 동일하게 자식에서 선언하면
    # 자식 객체에서는 자식에서 선언한 메소드로 실행된다.
    def walk(self):
        super().walk()
        print("네 발로 걷기")


kingkong = Monkey('멍순이', 10, '서울 어린이 대공원')
kingkong.walk()
