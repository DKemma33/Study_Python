animals = ["dog", "cat", "bird", "fish"]
print(animals)
print(type(animals))

# 인덱스로 접근
print(animals[1])
print(animals[2])

# 음수 인덱스 가능(가장 마지막부터 순서대로 앞으로 이동한다)
print(animals[-1])
print(animals[-2])

# len()
print(len(animals))

data = '-' * 50
print(data)

# append()

animals.append('hamster')
print(animals)

animals.append('cat')
print(animals)

# del()
del animals[1]
# del(animals[1])
print(animals)

# remove()
animals.remove('hamster')
print(animals)

# clear()
# animals.clear()
# print(animals)

# index()
index = animals.index('fish')
print(index)

# 수정
animals[2] = 'hamster'
print(animals)

print(animals * 2)

print(9 in [1, 2, 3, 4])

number = 10

print(number >= 1 and number <= 9)
print(1 <= number <= 9)

for i in [10, 20, 30]:
    print(i)














