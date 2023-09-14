from u_mysql.crud import *
import hashlib


# 회원가입

while True:
    def checking(new_member):
        find_by_id_query = "select id, member_id from tbl_member group by id having member_id = %s"

        while True:
            id_check = find_by_member_id(find_by_id_query, new_member)

            if id_check:
                print(f"{id_check.get('member_id')}는 이미 사용중인 아이디 입니다")
                return False
            else:
                print("사용 가능한 아이디 입니다")
                return True
    new_member_id = input("아이디를 입력하세요")
    done_checking = checking(new_member_id)

    if done_checking:
        save_insert_query = "insert into tbl_member(member_id,member_password,member_name)" \
                            "values (%s, %s, %s)"

        new_password = input("새로운 비밀번호를 입력하세요: ")
        name = input("이름을 입력하세요: ")

        encrypt = hashlib.sha256()
        encrypt.update(new_password.encode('utf-8'))
        save_params = [new_member_id, encrypt.hexdigest(), name]

        save(save_insert_query,save_params)
        break

    else:
        print("다른 아이디를 입력하세요")







