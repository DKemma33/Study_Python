# 아이디 중복검사
# find_by_member_id_query = "select id from tbl_member where member_id = %s"
# member_id = input("아이디: ")
#
# row = find_by_member_id(find_by_member_id_query, member_id)
#
# if row:
#     print(f'{row.get("id")}번 회원이 사용중인 아이디입니다.')
# else:
#     print('사용 가능한 아이디입니다.')

# 회원가입(SMS API) - 랜덤한 인증번호 6자리 발송 후 검사
# certification_number = "".join([str(random.randint(0, 9)) for i in range(6)])
#
# phone = input("핸드폰 번호: ")
#
# certification_number = send_certification_number(certification_number, phone)
#
# input = input('인증번호: ')
# check = certification_number == input
#
# if check:
#     save_query = "insert into tbl_member(member_id, member_password, member_name, member_phone, member_email) " \
#                  "values(%s, %s, %s, %s, %s)"
#     encrypt = hashlib.sha256()
#     encrypt.update('1234'.encode(encoding='utf-8'))
#     save_params = ['hds1234', encrypt.hexdigest(), '한동석', '01012341234', 'dev.tedhan@gmail.com']
#
#     save(save_query, save_params)

# 회원 비밀번호 변경(EMAIL API) - 랜덤한 인증번호 10자리 발송 후 검사
# 마이페이지에서 비밀번호 변경
# 로그인 후 비밀번호 변경 페이지에서 기존 비밀번호 입력 후 새로운 비밀번호로 변경
# ✔ 비밀번호 찾기 페이지에서 비밀번호 변경
# certification_number = "".join([str(random.randint(0, 9)) for i in range(10)])
# find_by_member_email_query = "select id from tbl_member where member_email = %s"
# email = input('이메일: ')
#
# row = find_by_member_email(find_by_member_email_query, email)
#
# if row:
#     id = row.get('id')
#     certification_number = send_certification_number_by_email(email, certification_number)
#     input_number = input("인증번호: ")
#     if certification_number == input_number:
#         new_password = input("새로운 비밀번호: ")
#         encrypt = hashlib.sha256()
#         encrypt.update(new_password.encode('utf-8'))
#         new_password = encrypt.hexdigest()
#
#         update_query = "update tbl_member set member_password = %s where id = %s"
#         update_params = [new_password, id]
#         update(update_query, update_params)
#
# else:
#     print("이메일을 다시 확인해주세요.")

# 사용자가 입력한 문장을 영어로 번역
# korean_message = input("번역할 문장: ")
# insert_query = "insert into tbl_translate(korean_message, english_message) " \
#                "values(%s, %s)"
# try:
#     english_message = translate(korean_message)
# except Exception:
#     english_message = None
# finally:
#     # 한국어와 번역된 문장을 DBMS에 저장
#     save(insert_query, [korean_message, english_message])

# 번역 내역 조회
# find_all_query = "select id, korean_message, english_message from tbl_translate"
# rows = find_all(find_all_query)
#
# for row in rows:
#     print(row)

# 업로드한 이미지 파일의 이름과 이미지의 내용을 DBMS에 저장(OCR API)
# insert_query = "insert into tbl_image_text(image_url, image_text) " \
#                "values(%s, %s)"
# image_url = "https://thumb.mt.co.kr/06/2012/02/2012021613230156226_1.jpg/dims/optimize/"
# image_text = ocr(image_url)
# print(image_text)
# save(insert_query, [image_url, image_text])












