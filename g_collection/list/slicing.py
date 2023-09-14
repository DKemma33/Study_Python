# 인덱스 슬라이싱
animals = ['dog', 'dog', 'cat', 'bird', 'fish']

# list[inclusive_start=0:exclusive_end=len(list)] -> list
print(animals[0])
print(animals[0:3])
print(animals[1:4])
print(animals[:2])
print(animals[2:])

food = ['noodle', 'meat', 'bread', 'chicken']

# list[inclusive_start=0:exclusive_end=len(list):step=1] -> list
print(food[:3:2])
print(food[2::2])

# 역순 출력
print(food[::-1])

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# [1, 3, 5, 7, 9]
print(number_list[::2])

# [6, 5, 4, 3, 2]
print(number_list[5:0:-1])

# [2, 4, 6]
print(number_list[1:6:2])

# [2, 3, 4, 5, 6, 7]
print(number_list[1:7])

animals = ['dog', 'dog', 'cat', 'bird']
zoo = ['panda', 'giraffe']

animals[1:2] = zoo
print(animals)

animals.insert(animals.index('dog') + 1, 'giraffe')
animals.insert(animals.index('dog') + 1, 'panda')
print(animals)


animals = ['dog', 'dog', 'cat', 'bird']
# ['dog', 'dog', 'shark', 'fish']
zoo = ['shark', 'fish']
animals[2:4] = zoo
print(animals)

# 슬라이싱, insert, del을 사용하여 아래의 list 만들기
# ['dog', 'hamster', 'fish', 'dog' 'whale', 'bird']
# animals = ['dog', 'dog', 'cat', 'bird']

# del animals[animals.index('cat')]
# animals.remove('cat')

# animals[-2:-3:-1] = ['whale']
# print(animals)

# animals.insert(animals.index('dog') + 1, 'fish')
# animals.insert(animals.index('dog') + 1, 'hamster')
# print(animals)

# animals[1:2] = ['hamster', 'fish', 'dog']
# print(animals)

number_list = [4, 6, 2, 1, 3]
number_list.sort()
print(number_list)

# sort()는 원본이 변경됨
# number_list.sort(reverse=True)
# print(number_list)

# 원본이 변경되지 않음
print(number_list[::-1])

# 원본이 변경되지 않음
number_list = [4, 6, 2, 1, 3]
print(sorted(number_list))
print(number_list)

