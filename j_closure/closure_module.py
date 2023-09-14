import datetime


def string_service():
    def getA():
        return "A"

    def getB():
        return "B"

    return {"a": getA, "b": getB}


print(string_service()["a"]())


def post_service():
    def save_post(*, title, content):
        print(title, content)

    def find_post(post_id, print_found_post=None):
        if print_found_post:
            print_found_post({"id": post_id, "title": "테스트 제목1", "content": "테스트 내용1"})
        return {"id": post_id, "title": "테스트 제목1", "content": "테스트 내용1"}

    # 수정
    def update_post(*, post_id, title, content):
        post = find_post(post_id)
        post['title'] = title
        post['content'] = content
        print(post)

    # 삭제
    def delete_post(post_id):
        posts = find_all_post()
        # len(posts), range에서 컬렉션의 길이로 반복횟수를 결정할 때,
        # for문 안에서 컬렉션의 추가 및 삭제 등을 진행하면
        # 매번 len()가 연산되기 때문에 인덱스 접근에 문제가 생길 수 있다.
        # count = 0
        for post in posts:
            if post["id"] == post_id:
                # del posts[count]
                posts.remove(post)
            # count += 1
        print(posts)

    # 전체 조회
    def find_all_post(print_found_posts=None):
        posts = [
            {
                "id": 1,
                "title": "테스트 제목1",
                "content": "테스트 내용1"
            },
            {
                "id": 2,
                "title": "테스트 제목2",
                "content": "테스트 내용2"
            },
        ]

        if print_found_posts:
            print_found_posts(posts)
        return posts

    return {
        'write': save_post,
        'getPost': find_post,
        'update': update_post,
        'delete': delete_post,
        'getList': find_all_post
    }


post_service()['write'](title='테스트 제목3', content='테스트 내용3')
post_service()['getPost'](1, lambda post: print(post))
post_service()['update'](post_id=2, title='수정된 제목', content='수정된 내용')
post_service()['delete'](2)
post_service()['getList'](lambda posts: print(posts))

