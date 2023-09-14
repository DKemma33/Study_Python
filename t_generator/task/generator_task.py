import random
import os
import psutil

process_object = psutil.Process(os.getpid())

# 전달받은 명 수만큼 정보를 dict로 리턴한다.

# 리턴할 정보
# 번호, 이름, 전공

names = ['김보령', '김혜빈', '임수현', '이서호', '임웅빈', '장동혁']
majors = ['컴퓨터 공학', '전자 공학', '기계 공학', '의료 공학', '토목 공학']

# random.choice(list): list 요소 중 랜덤한 값 추출
# print(random.choice([1, 2, 3]))


def get_list(count: int = 0) -> dict:
    result = []
    for i in range(count):
        info = {
            'id': i + 1,
            'name': random.choice(names),
            'major': random.choice(majors)
        }

        result.append(info)

    return result


def get_generator(count: int = 0) -> dict:
    for i in range(count):
        info = {
            'id': i + 1,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield info

############################################################################
memory_before = process_object.memory_info().rss / 1024 / 1024

infos = get_list(1000000)

memory_after = process_object.memory_info().rss / 1024 / 1024
print(f'memory: {memory_before} -> {memory_after}')
############################################################################
memory_before = process_object.memory_info().rss / 1024 / 1024

infos = get_generator(1000000)

memory_after = process_object.memory_info().rss / 1024 / 1024
print(f'memory: {memory_before} -> {memory_after}')
############################################################################