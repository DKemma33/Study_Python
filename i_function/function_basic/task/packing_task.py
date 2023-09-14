# 국어, 영어, 수학 점수를 전달받은 뒤 총 점을 출력하는 함수
# list에 국어, 영어, 수학 점수를 각각 담은 후 unpacking 발생시키기
def print_total(kor, eng, math):
    print(f'총 점: {kor + eng + math}')


def print_total(*scores):
    total = 0
    for i in scores:
        total += i
    print(f'총 점: {total}')


scores = [100, 90, 80]

print_total(*scores)

# 문자열에서 'A'가 몇 개 있는 지 검사하는 함수
# packing


def get_count_of_A(*string):
    count = 0
    for i in string:
        if i == 'A':
            count += 1
    return count


count = get_count_of_A(*"ABCDA")
print(count)

