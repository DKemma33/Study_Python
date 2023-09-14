import datetime


def log_time(original_function):
    print("log_time 들어옴")
    def logging(*args):
        print(*args)
        print(datetime.datetime.now())
        print("logging 함수 종료")
        return original_function(*args)

    print("log_time 함수 종료")
    return logging

def post_service():

    def find_post(get_post):
        get_post({"id": 3, "title": "테스트 제목1", "content": "테스트 내용1"})

    def find_all_posts(get_posts):
        get_posts([
            {"id": 3, "title": "테스트 제목1", "content": "테스트 내용1"},
            {"id": 4, "title": "테스트 제목2", "content": "테스트 내용2"}
        ])

    return {"read": find_post, "get_list": find_all_posts}

@log_time
def get_post(post):
    print(post)

@log_time
def get_posts(posts):
    print(posts)

post_service().__getitem__("read")(get_post)
post_service().__getitem__("get_list")(get_posts)
