import pymysql
from pymysql.cursors import Cursor
# pymysql 드라이버 import

# conn 객체를 pymysql에서 connect 함수를 통해 경로를 가져온다
# cursor 에 conn의 cursor을 담아주고 conn,cursor을 return 해준다
def connect():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='app', charset='utf8')
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    return conn, cursor

# execute 매개변수로 함수를 받아들인다. execute 함수는 실제 CRUD 작업을 수행하는 함수이다.
# result: 결과를 저장하기 위한 변수이다/ nonlocal result: 내부 함수에서 result 변수를 수정할 수 있도록 해준다
def execute_crud(execute):
    result = None

# manage(*args): 내부 함수로서, 실제로 데이터베이스 연결을 설정하고 CRUD 작업을 수행하는 역할을 한다
# conn, cursor = connect(): connect() 함수를 호출하여 데이터베이스에 연결합니다.
# conn은 연결된 데이터베이스 연결 객체이고, cursor는 커서 객체이다.
# result 에 execute(cursor, *args 매개변수)를 전달하면 execute 를 사용해서 데이터베이스 작업을 수행한다
# 작업이 완료되면 커밋을 해서 데이터베이스에 반영해준다
# 예외가 발생했을 경우에 Exception을 a로 사용해서 print(e 일시에 에러메세지를 출력) / rollback을 해준다(복구)
# finally로 cursor와 conn을 닫아서 데이터베이스와 연결을 종료한 후
# result 값(최종결과) 를 리턴해준다
# manage를 리턴해주면 execute 함수가 실행될때 데이터베이스에 연결을 설정 crud 작업이 실행된다
    def manage(*args):
        nonlocal result
        conn, cursor = connect()
        try:
            result = execute(cursor, *args)
            conn.commit()
        except Exception as e:
            print(e.__str__())
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

        return result

    return manage


# 아래의 함수들에 @execute_crud 를 적용한다
# save_with_seq 함수는 cursor, query, params 매개변수를 받는다
# 이 함수는 데이터를 저장하고, 저장된 데이터의 시퀀스(ID) 값을 반환하는 역할을 한다
# cursor.execute(query, params) cursor 객체를 사용하여 query와 params를 실행하여 데이터를 저장한다
# last_insert_id() 함수를 사용하여 최근에 추가된 목록의 시퀀스(ID) 값을 가져온다
# fetchone() 메서드를 사용하여 결과를 가져와 반환해준다.
@execute_crud
def save_with_seq(cursor: Cursor, query: str, params: list):
    cursor.execute(query, params)
    cursor.execute('select last_insert_id() seq')
    return cursor.fetchone()
# 이 함수를 만든 이유는 방금 추가(입력)된 parent 의 id 를 가져와야 하기 때문에
# last_insert_id()를 실행시켜준다 as 를 seq로  정해놓았기 때문에 seq로 사용 할수 있다


@execute_crud
def save(cursor: Cursor, query: str, params: list):
    cursor.execute(query, params)


@execute_crud
def find_all(cursor: Cursor, query: str):
    cursor.execute(query)
    return cursor.fetchall()


@execute_crud
def find_by_id(cursor: Cursor, query: str, params: list):
    cursor.execute(query, params)
    return cursor.fetchone()


# 학부모의 id를 통해 그 id값을 가지고 있는 부모의 아이의 전체 정보를 가져올때 사용한다
@execute_crud
def find_all_by_id(cursor: Cursor, query: str, parent_id: int):
    print(type(parent_id))
    cursor.execute(query, parent_id)
    return cursor.fetchall()

@execute_crud
def find_by_member_id(cursor: Cursor, query: str, params: list):
    cursor.execute(query, params)
    return cursor.fetchone()


@execute_crud
def find_by_member_email(cursor: Cursor, query: str, params: list):
    cursor.execute(query, params)
    return cursor.fetchone()


@execute_crud
def login(cursor: Cursor, query: str, params: list):
    cursor.execute(query, params)
    return cursor.fetchone()
# fetchone()은 중복이 없을때 사용한다

@execute_crud
def update(cursor: Cursor, query: str, params: list):
    cursor.execute(query, params)


@execute_crud
def delete(cursor: Cursor, query: str, params: list):
    cursor.execute(query, params)