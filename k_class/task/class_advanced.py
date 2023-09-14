# 회원
class User:
    count_of_user = 0

    def __init__(self, user_id, user_password, user_name):
        User.count_of_user += 1
        self.id = User.count_of_user
        self.user_id = user_id
        self.user_password = user_password
        self.user_name = user_name


class View:
    users = []

#     추가
    def insert(self, **user):
        View.users.append(user)

#     수정
    def update(self, **user):
        for user_in_db in View.users:
            if user_in_db['id'] == user['id']:
                user_in_db['user_name'], user_in_db['user_id'], user_in_db['user_password'] \
                    = user['user_name'], user['user_id'], user['user_password']
                break

#     삭제
    def delete(self, id):
        for user in View.users:
            if user['id'] == id:
                View.users.remove(user)

#     조회
    def select(self, id):
        for user in View.users:
            if user['id'] == id:
                return user
        return None

#     전체 조회
    def select_all(self):
        return View.users


user = User('hds', '1234', '한동석')
user_view = View()

user_view.insert(id=user.id, user_id='hds', user_password='1234', user_name='한동석')
print(user_view.select_all())

user = user_view.select(1)

user['user_id'] = 'hgd'
user['user_name'] = '홍길동'

user_view.update(**user)
print(user_view.select_all())

user_view.delete(1)
print(user_view.select_all())
