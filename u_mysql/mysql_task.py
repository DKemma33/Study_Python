from crud import *
import hashlib
import random
#===============================================================================================================
# find_by_id_query에 tbl_member의 입력될 member_id 에 서 id를 select한다
# member_id 에 input 아이디 값을 저장한다
# crud의 find_by_member_id에 쿼리와 member_id 값을 row에 저장한다
# if문으로 만약 row가 True 일때 (아이디가 있을 때) 사용중이라는 메세지를 출력한다
# else: 만약 없다면 사용 가능 하다는 메세지를 출력한다
#---------------------------------------------------------------------------------------------------------------
# 아이디 중복검사

find_by_id_query = "select id from tbl_member where member_id = %s"
member_id = input("아이디:")

row = find_by_member_id(find_by_id_query, member_id)
if row:
    print(f"{row.get('id')}는 사용중 인  아이디 입니다")
else:
    print("사용 가능한 아이디 입니다.")
#-------------------------------------------------------------------------------------------------------------------
# certification_number에 join을 
#-------------------------------------------------------------------------------------------------------------------
# 회원가입(SMS API) - 랜덤한 인증번호 6자리 발송 후 검사
certification_number = "".join([str(random.randint(0, 9)) for i in range(6)])

save_query = "insert into tbl_member(member_id, member_password, member_name)" \
             "values(%s, %s, %s)"
encrypt = hashlib.sha256()
encrypt.update('1234'.encode('utf-8'))
save_params = ['jdh123',encrypt.hexdigest(),'장동혁']

save(save_query,save_params)
# 회원 비밀번호 변경(EMAIL API) - 랜덤한 인증번호 10자리 발송 후 검사

# 사용자가 입력한 문장을 영어로 번역
# 한국어와 번역된 문장을 DBMS에 저장
# 번역 내역 조회

# 업로드한 이미지 파일의 이름과 이미지의 내용을 DBMS에 저장(OCR API)


























