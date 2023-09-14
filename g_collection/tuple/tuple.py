# mutable: 변할 수 있는
data_list1 = [1, 2, 3, 4]
data_list2 = data_list1
data_list2[0] = 10
print(data_list2)
print(data_list1)

# immutable: 변할 수 없는
data_tuple1 = (1, 2, 3, 4)
print(type(data_tuple1))

data_tuple2 = data_tuple1
print(data_tuple2)
data_tuple2 = data_tuple1 + (5, 6)
print(data_tuple2)

datas = 1, 2
print(type(datas))

data1, data2 = 1, 2
print(data1, data2)

for i in datas:
    print(i)

print([i for i in datas])
print(list(datas))

# 한 개의 값을 tuple 타입으로 선언할 때에는 값 뒤에 ,(콤마)를 붙여줘야 한다.
# data = (1,)
data = 1,
print(data[0])