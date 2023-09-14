# set
# 중복이 없고, 순서가 없다
world = {'korea', 'america', 'japan', 'china'}
print(type(world))
print(len(world))
# print(world[0])
world.add('korea')
print(world)

datas = [1, 2, 4, 7, 5, 3, 4, 4, 1]
print(list(set(datas)))

for i in world:
    print(i)

datas = {}
print(type(datas))
