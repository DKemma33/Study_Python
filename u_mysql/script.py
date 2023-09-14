from crud import save, find_all, update, delete

import hashlib

# insert_query = "insert into tbl_member(member_id, member_password, member_name)" \
#                "values(%s, %s, %s)"
# 암호화
encrypt = hashlib.sha256()
encrypt.update('5555'.encode('utf-8'))
print(encrypt.hexdigest())
# insert_param = ['lss5555', encrypt.hexdigest(), '이순신']
# delete_query = "delete from tbl_member where member_name = %s"
# delete_param = ['이순신']
# find_all_query = "select id, member_id, member_password, member_name from tbl_member"
# update_query = "update tbl_member set member_name = %s where member_id = %s"
# update_param = ['한동숙', 'lss5555']
# find_by_id_query = "select id, member_id, member_password, member_name from tbl_member " \
#                    "where id = %s"
# find_by_id_param = ['8']
# 회원가입
# save(insert_query, insert_param)
# 전체 조회
# for i in find_all(find_all_query):
#     print(f'아이디: {i.get("member_id")}\n이름: {i.get("member_name")}')
# 아이디가 'hds1234'인 회원의 이름을 '한동숙'으로 수정
# update(update_query, update_param)
# 이름이 '이순신'인 회원 삭제
# delete(delete_query, delete_param)
# 회원 번호로 한 명 조회
# print(find_by_id(find_by_id_query, find_by_id_param))

# 단일 테이블 3개 제작 후 CRUD 진행

# 1. 상품 정보 추가
# insert_query = "insert into tbl_product(product_name, product_price, created_date) " \
#                "values(%s, %s, %s)"
# insert_param = ['마우스', 45000, '2023-07-03']
# save(insert_query, insert_param)

# 상품 정보 조회
# find_by_id_query = "select product_name, product_price, created_date from tbl_product " \
#              "where id = %s"
# find_by_id_param = [1]
# product = find_by_id(find_by_id_query, find_by_id_param)
# print(str(product.get('created_date')))

# 2. 학생 정보 추가
# insert_query = "insert into tbl_student(student_name, student_birth) " \
#                "values(%s, %s)"
# insert_param = ['김혜빈', '2000-03-23T01:41:35']
#
# save(insert_query, insert_param)


# ===================================================================================

menu = "1. 회원가입\n" \
       "2. 회원정보 수정\n" \
       "3. 나가기\n"


message1,message2,message3 = ("아이디를 입력하세요 :", "비밀번호를 입력하세요 :","이름을 입력하세요 :")

new_id = input(message1)
new_password = input(message2)
new_name = input(message3)

insert_query = "insert into tbl_member(member_id, member_password, member_name)" \
               "values(%s, %s, %s)"
insert_param = [new_id, encrypt.hexdigest(), new_name]

find_query = "select member_id from tbl_member"
result = find_all(find_query)

update_query = "update tbl_member set %s = %s where member_id = %s"
update_param = [
        new_id = "1"

]

while True:
    menu_choice = int(input(menu))
    if menu_choice == 3:
        break

    if menu_choice == 1:
        cnt = 0
        for i in result:
            if i["member_id"] == new_id:
                cnt = 1
                print("이미 있는 아이디 입니다")
    if cnt == 0 :
        new_info = save(insert_query, insert_param)

    if menu_choice == 2:
        update =


















