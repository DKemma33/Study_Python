# Alt + F12 터미널
# python -m pip install PyMySQL
# pip install cryptography
import pymysql
# (파이썬 연동)
# pymysql에 connect라는 메소드가 있고(host 자리에 네트워크상 서버 내의 ip주소를 알려주는 번호,mysql 처음 실행할때 아이디와 비밀번호이다
# db = 에는 작업할 database의 이름을 입력한다, 한글이 깨지지 않게 utf8 을 넣어준다
# conn 개체로 connect메소드를 담아준다/ cursor 은 쿼리를 완성시키고 생성시켜준다
# cursor 을 connection 객체에서 가지고 온다 딕셔너리 형태로/ cursor 객체를 통해 execute를 써서
# 그 execute 안에 쿼리를 작성한다/ 드라이버를 다 사용했으면 닫아줘야한다
# cursor.close()/ conn.close()를 써준다
# commit을 써 줘야 확정이 된다 commit하기 전에 close를 하게되면 실행이 되지 않는다

conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='app', charset='utf8')
cursor = conn.cursor(pymysql.cursors.DictCursor)
cursor.execute("insert into tbl_member(member_id, member_password, member_name) values('', '', '')")
conn.commit()

cursor.execute("select id, member_id, member_password, member_name from tbl_member")
rows = cursor.fetchall()
print(rows)

cursor.close()
conn.close()