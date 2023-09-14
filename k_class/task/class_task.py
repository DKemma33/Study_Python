# 동물
# 이름, 나이, 성별, 음식개수, 체력개수
# 먹기, 산책하기

# 먹기: 음식 1개 소진, 체력 1개 획득
# 산책하기: 음식 1개 획득, 체력 1개 소진
class Animal:
    def __init__(self, name, age, gender, food_count=0, health=10):
        self.name = name
        self.age = age
        self.gender = gender
        self.food_count = food_count
        self.health = health
        
    def eat(self):
        self.food_count -= 1
        self.health += 1
        
    def walk(self):
        self.food_count += 1
        self.health -=1


tiger = Animal('호랑이', 23, '암컷')
elephant = Animal('코끼리', 56, '수컷')

tiger.walk()
elephant.walk()

print(tiger.name, tiger.food_count, tiger.health)
print(elephant.name, elephant.food_count, elephant.health)









