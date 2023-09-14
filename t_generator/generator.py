import os
import psutil

process_object = psutil.Process(os.getpid())

############################################################################
memory_before = process_object.memory_info().rss / 1024 / 1024

data_list = [i ** 2 for i in range(100)]
# TypeError: 'list' object is not an iterator
# print(next(data_list))
print(data_list)

memory_after = process_object.memory_info().rss / 1024 / 1024
print(f'memory: {memory_before} -> {memory_after}')

############################################################################

# data_iterator = iter(data_list)
# print(type(data_iterator))
# print(next(data_iterator))

############################################################################
memory_before = process_object.memory_info().rss / 1024 / 1024

data_generator = (i ** 2 for i in range(100))
# print(type(data_generator))
print(next(data_generator))

memory_after = process_object.memory_info().rss / 1024 / 1024
print(f'memory: {memory_before} -> {memory_after}')


############################################################################

def increase(number: int = 0):
    while True:
        number += 1
        yield number


result = increase()
while True:
    data = input("다음[y/N] >> ")
    if data == 'y':
        print(next(result))
    else:
        break
