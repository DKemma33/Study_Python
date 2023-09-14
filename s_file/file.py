# 절대 경로: 대한민국 서울시 강남구 역삼동 123-22 302호
# 어떤 위치에 있든 상관없이 찾아갈 수 있는 경로
# C:/a/b, D:/User/ted, ...

# 상대 경로: 직진해서 좌회전 후 오른쪽 건물
# 현재 위치에 따라 변경되는 경로
# ../../a/b, ./src/images, work/day01, ...

# 파일 생성하기(덮어쓰기)
# file = open('food.txt', 'w', encoding='utf-8')
# file.write("부대찌개\n")
# file.write("햄버거\n")
# file.close()
#
# # 내용 추가하기(이어쓰기)
# file = open('food.txt', 'a', encoding='utf-8')
# file.write("피자\n")
# file.close()
#
# # 파일 읽기
file = open('food.txt', 'r', encoding='utf-8')
line = None

# while line != '':
#     line = file.readline()
#     print(line, end='')

# print(file.readlines())
for line in file.readlines():
    print(line, end='')

file.close()
