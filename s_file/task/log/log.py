import datetime

from s_file.task.log import NoMoreLineError


def log_time(original_function):
    formatting = None

    def logging(*args, **kwargs):
        nonlocal formatting
        # 파일 출력
        self, other = args
        file, error_message = kwargs.values()
        result = original_function(*args, **kwargs)
        if error_message:
            if 'ValueError' in error_message:
                formatting = f'{error_message}'
            else:
                formatting = f'{self.number}\t{self.oper}\t{other}\t=\t{error_message}'
        else:
            formatting = f'{self.number}\t{self.oper}\t{other}\t=\t'
            if self.oper == '/':
                value, rest = result
                formatting += f"몫: {value}, 나머지: {rest}"
            else:
                formatting += f'{result}'

            formatting += "\t\t\t\t / " + str(datetime.datetime.now()) + "\n"

        file.write(formatting)

        return result

    return logging


# 파일 입력
def get_log(file):
    try:
        for i in file.readlines():
            yield i

        raise NoMoreLineError
    except ValueError:
        print('파일 입력 종료')
