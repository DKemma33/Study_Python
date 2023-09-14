print(list("ABC"))

for i in "ABC":
    print(i)

# upper(), lower()
print("Apple123!@#".upper())
print("Apple123!@#".lower())

data = "사과, 바나나, 파인애플, 포도, 복숭아"
# maxsplit=값개수
print(data.split(", ", maxsplit=2))
# split(): 한 개 또는 여러 개의 모든 공백을 구분점으로 삼는다.
# 임수현씨 제보: split(" "): 직접 공백 문자를 전달하면 1개의 공백만 구분점으로 삼는다.
print("A B C D E F".split())
print("A      B".split())
print("A    B".split(" "))

# map(function, list): 함수를 배운 후 다시 이해하도록 하자!
print(list(map(str, [1, 2, 3, 4])))

# join()
print(":".join(['a', 'b', 'c']))
print("".join(['a', 'b', 'c']))

#replace('기존 값', '새로운 값')
print("A b C d".replace(" ", ""))
print("    Abcd     ".replace(" ", ""))
#허은상
print("     abcd    ".strip())

#find()
# print("ABC".index("Z")) : 못찾았을 때 화가 많다(Error 발생)

# 못찾았을 때 -1을 리턴함으로써 프로그램이 종료되지 않는다.
print("ABC".find("Z"))

# count('검색할 값') : 검색한 값이 몇 개인지 검사
print("fndohfndiosniofnsdionfiodsnfiodsniofdnsiofniosdndfiosnfiosdin".count('f'))

# 아래 문자열을 189000 출력, join()사용
s = "189,000 원"
print(''.join(i for i in s if '0' <= i <= '9'))

# data_list = []
# for i in s:
#     if '0' <= i <= '9':
#         data_list.append(i)
#
# print("".join(data_list))


