# # crud에서 import를 사용해 함수들을 가져온다
# # insert = 입력 쿼리 / tbl_parent 테이블에 있는 이름,나이,주소,전화번호,성별을 넣어주고 밑에 values 값을 %s 로 넣어 놓는다
# # 이름,나이,주소,전화번호,성별에 input으로 값을 받는다
# # params이고 변수이름은 바꿔도 된다# parent_datas에 values값을 담는다.
# # parent_id 에 crud의 save안에 insert값과 params값을 담는다 )
# .get('seq') 는 방금 추가된 학부모의 id 번호가 필요하기 때문에 crud 파일에서 정의 해놓은 ('select last_insert_id() seq')를
#  as 인 seq로 가져온다
# #-----------------------------------------------------------------------------------------------------------
# 학부모 (회원가입)
from u_mysql.crud import save, update, find_all
from u_mysql.task.advanced.crud import find_all_by_id, login, save_with_seq

insert_query = "insert into tbl_parent(parent_name, parent_age, parent_address, parent_phone, parent_gender) " \
                "values(%s, %s, %s, %s, %s)"
name = input('이름: ')
age = input('나이: ')
address = input('주소: ')
phone = input('핸드폰 번호: ')
gender = input('성별: ')
parent_datas = [name, age, address, phone, gender]
parent_id = save_with_seq(insert_query, parent_datas).get('seq')
# print(parent_id)
##=========================================================================================================
## (개인 회원 정보 안에 들어갈 정보 입력)
# insert_query에 tbl_child 의 아이 이름,나이 성별과 부모님의 아이디 값을 담는다/values가 4개 이기 때문에 %s 4개
# while문으로 항상 부모의 정보를 입력후 아이가 있는지 선택 해서 있을 시에 아이의 정보를 입력 할수 있다
# choice를 변수로 설정하고 input으로 질문 y/N 로 선택 하게 한다
# if문을 사용해서 choice 가 N과 같을 시에 break 로 멈추게 한다
# y일 시에 if문을 사용 안하고 바로 밑에 input에 값을 입력하게 한다
# 그 변수들을 child_datas에 담아주고 crud의 save에 insert_query 와 값인 child_datas 를 담아서 저장해준다
#--------------------------------------------------------------------------------------------------
# # # 아이가 있다면 아이의 정보까지 입력
insert_query = "insert into tbl_child(child_name, child_age, child_gender, parent_id) " \
               "values(%s, %s, %s, %s)"
while True:
    choice = input("아이 정보를 입력하시겠습니까?[y/N]\n")
    if choice == 'N':
        break
    child_name = input("아이 이름: ")
    child_age = input("아이 나이: ")
    child_gender = input("아이 성별: ")
    child_datas = [child_name, child_age, child_gender, parent_id]

    save(insert_query, child_datas)
##===========================================================================================================
 # insert 쿼리 변수 이름을 login_query로 정해주고 select로 tbl_parent의 parent_name이 입력한 값 %s 이고  and
 #                                                                 phone_number이 입력한 값이 %s 이다
 # login에 (login_query를 넣어주고[안에 키값인 부모의 이름,전화번로를 넣어준다]).get('id')로 부모의 id값을 받아온다
 # parent_id 변수에 login을 넣어준다
 # 마지막 if 문은 parent_id가 True 일때 밑에 입력하는 부분들이 if 문 안에서 실행된다
# #----------------------------------------------------------------------------------------------------------
 # 로그인(학부모 이름, 학부모 휴대폰 번호)
login_query = "select id from tbl_parent where parent_name = %s and parent_phone = %s"
parent_name = input("학부모 이름: ")
parent_phone = input("학부모 핸드폰 번호: ")

parent_id = login(login_query, [parent_name, parent_phone]).get('id')
if parent_id:
##==========================================================================================================
# parent의 id로 아이의 전체 정보를 가져오기 위해 find_by_id_query에 select로 아이의 정보를 where부모의 아이디 =
# %s 입력한 값에서 가져온다. crud에 만들어 놓은 find_all_by_id 함수에 정의해 놓은 query와 위에 로그인 되어있는 parent_id 값을 담아준다
# children 변수에 find_all_by_id를 넣어줘서 값으로 만든다.
# for문으로 children 안의 child를 출력한다

##----------------------------------------------------------------------------------------------------
# 로그인된 학부모의 아이 정보 출력
    find_by_id_query = "select child_name, child_age, child_gender from tbl_child where parent_id = %s"
    children = find_all_by_id(find_by_id_query, parent_id)

    for child in children:
        print(child)
##------------------------------------------------------------------------------------------------------
# 수정을 위해서 update_query를 사용 tbl_child 에서 set child_age 가 입력받을 갑이 되고 where id가 입력 받는 갑이 된다
# input으로 child의 id와 age를 입력 받는다 update()에 쿼리와 리스트를 만들어서 그 안에 id와 age값을 같이 받는다
    # 아이의 정보 중 나이를 수정하기(아이 고유 번호를 이용)
        update_query = "update tbl_child set child_age = %s where id = %s"
        child_id = int(input("정보를 수정할 아이를 선택하세요."))
        child_age = int(input("나이: "))
        update(update_query, [child_age, child_id])
#-----------------------------------------------------------------------------------------------------------------------
# 새로운 정보 추가를 위해  insert로 tbl_child에서 아이의 이름,나이,성별, 부모님 id를 입력 받는다
# while문으로 아이의 정보 추가 [y/N] 중 하나를 선택하는 식/ input으로 질문을 choice 에 담아 실행하고
# choice가 N과 같다면 break를 실행하고
# 아니면 밑의 식을 실행시킨다/  값들을 다시 datas 에 담아준 후  save에 insert쿼리와 child_datas를 넣어준다
#--------------------------------------------------------------------------------------------------
    # 새로운 아이 정보 추가
    insert_query = "insert into tbl_child(child_name, child_age, child_gender, parent_id) " \
                   "values(%s, %s, %s, %s)"

    while True:
        choice = input("아이 정보를 입력하시겠습니까?[y/N]\n")
        if choice == 'N':
            break
        child_name = input("아이 이름: ")
        child_age = input("아이 나이: ")
        child_gender = input("아이 성별: ")
        child_datas = [child_name, child_age, child_gender, parent_id]

        save(insert_query, child_datas)
# ==================================================================================================
# 체험학습을 등록 시킬수 있는 관리자 권한을 만든다 insert로 tbl_parent 에 값을 넣는다 parent_type은 admin이다/
# parent_data 에 값을넣고 save에 inser_query와 parent_data(params)를 담는다
#----------------------------------------------------------------------------------------------------------------
# 인가(Authorization): 권한 부여
    insert_query = "insert into tbl_parent(parent_name, parent_age, parent_address, parent_phone, parent_gender, parent_type) " \
                   "values(%s, %s, %s, %s, %s, %s)"
    name = input('이름: ')
    age = input('나이: ')
    address = input('주소: ')
    phone = input('핸드폰 번호: ')
    gender = input('성별: ')
    type = 'admin'

    parent_datas = [name, age, address, phone, gender, type]

    save(insert_query, parent_datas)
#=================================================================================================================
# 위에 있는 로그인 코드를 가져와서 login_query에 parent_type을 추가해준다 / 학부모의 이름과 전화번호를 input으로 받고/
# parent에 login(로그인 쿼리와 리스트 형식 안에 이름과 전화번호를 담아준다)
# parent_id 에 login을 담아놓은 변수 parent에서 .get으로 id를 가져오고 / parent_type에서도 = parent.get으로 (parent_type)을 가져온다
# if문으로 parent_id 와 type이 == admin과 같을때 체험 학습을 관리자 권한으로 등록할수 있다
# 다시 insert 쿼리로 tbl_field_trip에 타이틀, 컨텐츠, 지원 가능수를 입력한다
# input으로 값을 받아오고 crud의 save에 insert쿼리와 리스트 형식으로 입력받은 값들을 다 넣어 준다
#-------------------------------------------------------------------------------------------------------------

# 체험학습 등록(관리자만 가능)
login_query = "select id, parent_type from tbl_parent where parent_name = %s and parent_phone = %s"
parent_name = input("학부모 이름: ")
parent_phone = input("학부모 핸드폰 번호: ")

parent = login(login_query, [parent_name, parent_phone])
parent_id = parent.get('id')
parent_type = parent.get('parent_type')

if parent_id and parent_type == 'admin':
    insert_query = "insert into tbl_field_trip(field_trip_title, field_trip_content, field_trip_number) " \
                   "values(%s, %s, %s)"

    field_trip_title = input("체험학습 제목: ")
    field_trip_content = input("체험학습 내용: ")
    field_trip_number = int(input("체험학습 최대 인원 수: "))

    save(insert_query, [field_trip_title, field_trip_content, field_trip_number])
#===================================================================================================================
# 지원을 하기 위에 admin에 등록 해놓은 학부모를 로그인 시킨다/ 위의 로그인 코드를 가져왔다
# parent_id 에는 crud의 login 함수에 query와 params(값인 부모 입력한 부모 이름과 전화번호).get('id')로 그 부모의 id를 가져온다
# if parent: 가 True 일때 밑의 코드가 실행된다
# find_all_query에 쿼리를 담는다 = select tbl_field_trip에서 아이디,타이틀,컨텐츠,지원가능수,ifnull(등록된 아이가 없을때 ,0 으로 나오게 한다)
# as는 child_count로 정해줬다,ifnull(만약 지원가능수에서,지원자 수를 빼면,  ) rest_number가 나와야 하는데 만약 지원자가 없다면 지원가능 수가 나오게 한다
# left outer join으로 지원자가 없더라도 목록이 나오게 한다
# () 안에 select tbl_apply 지원목록 에서 체험학습의 id와 count(로 지원한 아이들의 수를 카운트 해준다) as는 child_count로 해주었다
# group by로 field_trip_id를 기준으로 지원한 아이들의 수를 가져온다  as를 a 로 정해서 ()a 를 해주면 ()안에 있는 쿼리를 a 로 사용한다
# 위의 left outer join (  ) a on a의 field_trip_id와 ft의 field_trip_id가 를 join 한다
# crud의 find_all 함수에 find_all_query를 담고 field_trips = 에 담는다
# number = 0 출력할 필드 트립 목록의 번호를 나타내기 위한 변수를 초기화
# for field_trip in field_trips:: 필드 트립 목록을 반복하여 각 필드 트립의 정보를 출력한다
# number += 1 는 필드 트립 번호를 증가시킨다
# print로 (str문자열 (number필드트립 번호) + ". " + str(field_trip 필드트립 ))정보를 출력해주고
# field_trip_choice = 에 모든 값이 int(정수)형태로 저장되고 input을 사용해서 번호를 입력 받도록 해준다
#------------------------------------------------------------------------------------------------------------------
# 체험학습 지원
login_query = "select id from tbl_parent where parent_name = %s and parent_phone = %s"
parent_name = input("학부모 이름: ")
parent_phone = input("학부모 핸드)폰 번호: ")

parent_id = login(login_query, [parent_name, parent_phone]).get('id')
if parent_id:
    find_all_query = "select id, field_trip_title, field_trip_content, field_trip_number, " \
                     "ifnull(child_count, 0) child_count, ifnull(field_trip_number - a.child_count, field_trip_number) rest_number " \
                     "from tbl_field_trip ft " \
                     "left outer join " \
                     "(" \
                     "select field_trip_id, count(child_id) child_count " \
                     "from tbl_apply " \
                     "group by field_trip_id " \
                     ") a " \
                     "on a.field_trip_id = ft.id"

    field_trips = find_all(find_all_query)
    number = 0
    for field_trip in field_trips:
        number += 1
        print(str(number) + ". " + str(field_trip))

    field_trip_choice = int(input("번호: "))
#===================================================================================================================
# feilld_trips 는 위에서 담아놓은 체험학습 목록이다/ [목록에서 체험학습을 선택하면 - 1 이 된다/목록이 0 부터 시작하기 때문에
# 선택한 목록에서 1을 빼야 가져올수 있다] get 남은 지원가능 수가 0이 아니라면
# 선택한 목록을 field_trip_id 변수에 저장한다
# 만약 위에 지원가능 수가 0 이라면  else: 모집마감 메세지를 출력한다 field_trip_id는 None 으로 설정한다
# if field-trip_id가 True(위의 else문이 실행되지 않았을때) 아이의 정보를 넣어주기 위해 find_by_id 쿼리로 id와 아이이 이름,나이,성별을
# tbl_parent의 parent_id 에 %s 값에 있는 학부모의 아이의 정보를 가져온다
# children에 방금 받아온 아이의 정보를 crud 의 find_by_id 함수에 query와 params에 담아와 저장한다
# child_ids 에 아이의 정보를 가져오기 위해 [] 비어있는 리스트를 만든다
# while문을 사용해서 학부모가 지원을 멈출때 까지 반복한다 # number을 0 으로 설정하고
# for문으로 children 에서 child 정보를 가져온다  number += 로 학부모의 정보에서 가져온 아이의 정보 당 숫자가 + 된다
# print로 번호와 아이의 정보를 출력한다
# 번호를 입력하라는 메세지를 input에 넣고 choice 변수에 담아줬다/ 메세지 옆에 [종료: q]\n 종료 방법
# if 문으로 choice가 == q : 이면 break 를 실행 시킨다
# choice = choice를 int로 바꿔준다 (입력받은 번호)
# child-ids에 append 메서드로 find_all_by_id() 함수를 통해 가져온 자녀 정보 목록 추가
# (children[choice - 1].get('id')) / children 에 학무모의 정보로 부터 가져온 아이의 정보가 있고
# choice에 있는 아이의 정보에서 - 1 을 하고 get 으로 그 아이의 id번호를 가져온다
#-----------------------------------------------------------------------------------------------------------------------
#     # 지원 가능 검사
    if field_trips[field_trip_choice - 1].get('rest_number') != 0:
        field_trip_id = field_trips[field_trip_choice - 1].get('id')

    else:
        print("모집이 마감된 체험학습입니다.")
        field_trip_id = None

    if field_trip_id:
        find_by_id_query = "select id, child_name, child_age, child_gender from tbl_child where parent_id = %s"
        children = find_all_by_id(find_by_id_query, parent_id)
        child_ids = []
        while True:
            number = 0
            for child in children:
                number += 1
                print(str(number) + ". " + str(child))

            choice = input("보낼 아이 번호를 입력하세요[종료: q]\n")
            if choice == 'q':
                break

            choice = int(choice)
            child_ids.append(children[choice - 1].get('id'))
#======================================================================================================================
#  지원자 수를 파악해야 지원 가능 여부를 알수있기 때문에 필요하다/
# if 문으로 child_ids를 몇개의 아이디가 있는지 숫자로 알기 위해 len으로 바꾼후 field_trips(체험학습 목록)의
# 지원 가능수가 child_ids와 같거나 크면 for문을 실행
# child_ids 에 있는 child_id에 insert query를 사용해서 crud의 save에 쿼리에 [아이의 id와 부모의 id] 를 저장한 후
# print 지원완료 메세지를 출력하고 아이의 숫자가 더 커서 for문이 실행이 안되었으면
# else로 지원불가능 메세지를 출력한다
#----------------------------------------------------------------------------------------------------------------------
        # 지원자 수 검사
        if len(child_ids) <= field_trips[field_trip_choice - 1].get('rest_number'):
            # 지원
            for child_id in child_ids:
                insert_query = "insert into tbl_apply(child_id, field_trip_id) " \
                               "values(%s, %s)"

                save(insert_query, [child_id, field_trip_id])

            print("지원 드디어 완료!")

        else:
            print("지원 가능 인원 수를 초과하였습니다.")

# ===============================================================================================================
# ===============================================================================================================
# crud 의 함수들을 이용해 tbl_soft_drink 테이블에서 제품명과 가격을 insert 한다
# for 문으로
# # 음료수 등록
save_query = "insert into tbl_soft_drink(soft_drink_name, soft_drink_price) " \
             "values(%s, %s)"

for i in range(10):
    save(save_query, [f'음료수{i + 1}', 3000 + i * 200])


# # 상품 등록
# save_query = "insert into tbl_product(product_name) " \
#              "values(%s)"
#
# for i in range(20):
#     save(save_query, [f'상품{i + 1}'])
#
# # 당첨 번호 등록
# get_count_product_query = "select count(id) product_count from tbl_product"
#
# find_all_query = "select id from tbl_product"
# products = find_all(find_all_query)
# products_ids = []
# for product in products:
#     products_ids.append(product.get('id'))
#
# # 100개 유통
#
# # 100개 유통
# # 음료수 랜덤, 당첨번호 랜덤
# get_count_soft_drink_query = "select count(id) soft_drink_count from tbl_soft_drink"
# get_count_lottery_query = "select count(id) lottery_count from tbl_lottery"
#
# find_all_soft_drink_query = "select id from tbl_soft_drink"
# find_all_lottery_query = "select id from tbl_lottery"
#
# soft_drinks = find_all(find_all_soft_drink_query)
# lotteries = find_all(find_all_lottery_query)
#
# soft_drink_ids = []
# lottery_ids = []
#
# for soft_drink in soft_drinks:
#     soft_drink_ids.append(soft_drink.get('id'))
#
# for lottery in lotteries:
#     lottery_ids.append(lottery.get('id'))
#
# save_query = "insert into tbl_circulation(soft_drink_id, lottery_id) " \
#              "values(%s, %s)"
#
# # 확률
# # 단위 정하기: 10단위
# rating_box = [0] * 10
# rating = 30
# for i in range(rating // 10):
#     rating_box[i] = 1
#
# for i in range(100):
#     random_index = randint(0, 9)
#     soft_drink_index = randint(0, get_count(get_count_soft_drink_query).get('soft_drink_count') - 1)
#     lottery_index = randint(0, get_count(get_count_lottery_query).get('lottery_count') - 1)
#
#     random_soft_drink = soft_drink_ids[soft_drink_index]
#     random_lottery = lottery_ids[lottery_index]
#
#     # 70% 확률
#     if rating_box[random_index] == 0:
#         random_lottery = None
#
#     save(save_query, [random_soft_drink, random_lottery])
