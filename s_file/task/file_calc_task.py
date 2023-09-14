import datetime

from log.log import log_time, get_log
import calc.calc as c
from s_file.task.log import NoMoreLineError

# 두 정수의 연산을 수행하는 계산기 모듈 제작
# 연산 수행 시 해당 시간을 기록하고,
# 연산 수행 중 오류 발생 시 오류 사항과 시간을 기록하도록 한다.

# 입력 예
# 두 정수를 입력하세요.
# 연산자를 선택하세요

# 출력 예
# 1 + 3 = 4
# 10 / 0 = ZeroDivisionError

menu = "1. 계산하기\n2. 로그보기\n3. 종료하기\n"
number_message = "두 정수를 입력하세요.\n예)3 4\n"
oper_message = "연산자를 입력하세요.(+, -, *, / 중 1 택)\n"
continues_message = '계속 하시겠습니까? [y/N]'

while True:
    choice = int(input(menu))

    if choice == 3:
        break

    if choice == 1:

        while True:
            number1, number2, oper = 0, 0, ""
            error_message = ""
            file = open('log/log.txt', 'a', encoding='utf-8')
            try:
                number1, number2 = map(int, input(number_message).split())
                oper = input(oper_message)
            except ValueError:
                error_message = "ValueError, 입력 오류"
            finally:
                if oper == '/' and number2 == 0:
                    error_message = f'ZeroDivisionError, 0으로 나눔\t\t\t\t / {datetime.datetime.now()}\n'
                result = c.Calc(number1).calc(number2, oper, file, error_message)
                file.close()

            continues = input(continues_message)
            if continues == 'N':
                break

    elif choice == 2:
        file = open('log/log.txt', 'r', encoding='utf-8')
        line = get_log(file)
        while True:
            choice = input('로그 불러오기 [y/N] >> ')
            if choice == 'N':
                file.close()
                break

            if choice == 'y':
                try:
                    print(next(line))
                except Exception:
                    print('더 이상 불러올 로그가 없습니다.')
                    file.close()
                    break


    









