student = {
    "name": "한동석",
    "email": "tedhan1204@gmail.com"
}

print(student['name'])
print(student.get('name'))

# print(student['phone'])
# get()을 사용하면 key를 찾지 못했을 때 원하는 default값 설정 가능
print(student.get('phone', '01012341234'))

student['name'] = '홍길동'
print(student)
student['phone'] = '01012341234'
print(student)

if 'name' in student:
    student['email'] = 'hds1234@gmail.com'
else:
    student['email'] = 'hds1234@gmail.com'

del student['email']
print(student)

my_dict = {
    1: "한동석",
    "two": "20살",
    False: [10, 20, 30],
    "row": [
        {"name": "ted", "age": 40},
        {"name": 'john', "age": 30},
        {"name": "mike", "age": 20}
    ]
}

print(my_dict)
print(my_dict[1])
print(my_dict["two"], type(my_dict["two"]))
print(my_dict[10 > 11])
print(my_dict[False][1])
print(my_dict['row'][2]['name'])

for i in student:
    print(i)

print(list(student))

# key 분리
print(type(student.keys()))
print(list(student.keys()))

for i in student.keys():
    print(i)

# value 분리

print(student.values())
print(list(student.values()))

for i in student.values():
    print(i)

# 한 쌍씩 분리
for key, value in student.items():
    print(key, value)

