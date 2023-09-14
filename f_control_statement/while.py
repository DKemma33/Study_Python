# 이름 10번 출력 -> for문을 사용하자
# count = 0
# while count != 10:
#     print(f"{count}.한동석")
#     count += 1

# 사용자가 입력한 정수가 몇 자리수인지 출력
message = "정수: "
number = int(input(message))

count = 0
# while True:
#     count += 1
#     number //= 10
#     if number == 0:
#         break

while number != 0:
    count += 1
    number //= 10

print(count)
