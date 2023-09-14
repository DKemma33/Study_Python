# 국어, 영어, 수학 점수의 평균 구하기
# def get_average(kor, eng, math):
#     total = kor + eng + math
#     average = total / 3
#     return average

def get_average(**scores):
    kor, eng, math = scores.values()
    total = kor + eng + math
    average = total / 3
    return average

# scores = {'kor': 100, 'eng': 90, 'math': 80}
# average = get_average(**scores)

# average = get_average(kor=100, eng=90, math=80)
# print(average)


scores = {'kor': 100, 'eng': 90, 'math': 80}
average = get_average(**scores)
print(average)

average = get_average(kor=100, eng=90, math=80)
print(average)

# datas = {"a": 1, "b": 2, "c": 3}
#
# a, b, c = datas
# print(a, b, c)
#
# a, b, c = datas.values()
# print(a, b, c)

