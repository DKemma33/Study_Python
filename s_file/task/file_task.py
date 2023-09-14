# 파일의 단어의 빈도수 구하기

# alice.txt

# 오로지 알파벳만 검사하기
# 대소문자 구문없이 비교
# 글자수 2개 이상인 단어만 카운트 하기
# 빈도수 100회 이상인 단어만 카운트

"""
[출력예]
the 1642
and 872
to 729
it 595
she 553
of 514
said 462
you 411
alice 398
in 369
...
"""

file = open('alice.txt', 'r', encoding='utf-8')

# readline(): 한 줄 가져오기
# readlines(): 전체 내용을 가져온 뒤 각 줄을 리스트로 가져오기
# read(): 전체 내용을 문자열로 가져오기

# 오로지 알파벳만 검사하기
data = file.read().lower()

temp = []
for character in data:
    if 'a' <= character <= 'z':
        temp.append(character)
    else:
        temp.append(" ")

data = ''.join(temp)

# split()을 사용하면 공백은 모두 구분점으로 사용한다.
# print("a       b c".split())

words = [
    word
    for word in data.split()
    if word.__len__() > 1
]

# get(key): 없으면 None값 리턴
# print(test.get('b'))
# [key]: 없으면 KeyError 발생
# print(test['b'])

result = {}
for word in words:
    if result.get(word):
        result[word] += 1
    else:
        result[word] = 1

result = {
    word: result[word]
    for word in result
    if result[word] >= 100
}

# 빈도수 정렬
sorted_key = sorted(result, key=result.get, reverse=True)

for key in sorted_key:
    print(key, result[key])
