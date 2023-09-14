# try:
#     int(input("정수를 입력하지 않는다면 너의 컴퓨터는 해킹당할 것이다.\n정수: "))
#
# except Exception as e:
#     print(e)
#     print("해킹 완료")
#
# try:
#     print(10 / 0)
# except ZeroDivisionError:
#     print("0으로 나눌 수 없습니다.")
#
# # print(10 / 0)
# print("반드시 실행되어야 하는 문장")

# try:
#     number = int(input("10을 나누는 수(분모)를 입력하세요\n"))
#     print(10 / number)
#
# except ZeroDivisionError:
#     print("0으로 나눌 수 없습니다.")
#
# finally:
#     print("반드시 실행되어야 하는 문장")


# class BadWordError(Exception):
#     def __str__(self):
#         return "으응~~~ 안돼요~!"
#
#
# def check_bad_word(message):
#     if message.__contains__('바보'):
#         raise BadWordError
#
#
# message = input("채팅: ")
# check_bad_word(message)
# print(message)

