# Study_Python
# study_python
<a name="readme-top"></a>
## python 기초

### 리스트 변수

##### 1. 리스트 선언
```
    - 리스트 변수 =[]
    - 리스트 변수 = list()
    - 리스트변수 = [데이터1, 데이터2 ''']
```
##### 2. 리스트 추가
```
    - 리스트변수.append(data)
    - 리스트변수.insert(indexNum, data)
```
##### 3. 리스트 삭제
```
    - 리스트변수.remove(data)
    - del 리스트변수[인덱스번호]
```
##### 4. 리스트 데이터 수정
```
   리스트변수[인덱스번호] = 수정할 데이터
```

  
### 데이터 구조(List, Tuple, Dictionary, Set)

#### 데이터 구조(Tuple)

##### Tuple은 괄호를 이용해 선언할 수 있다.
  - tuple1 = (1, 2, 3, 4)

##### Tuple은 삭제나 추가가 불가능 하다.
    del tuple[1]
    tuple[1] = 'c'

##### Tuple끼리 더하거나 반복하는 것은 가능하다
- tuple2 = (5, 6) <br>
- print(tuple1 + tuple2) <br>
- print(tuple * 3)

#####  tuple로 변수끼리 값을 편하게 바꿀 수 있다
    x = 2 
    y = 3

    (x, y) = (y, x)

    print('x= ',x,'y = ', y)

#### 데이터 구조 (dictionary의 선언)
    dict1 = 3
    print (dict1)
    
##### dictionary는 key와 value로 이루어져 있고, 추가하는 방법
    dict1 = {'name': 'jahyun'} 
    print (dict1)
    dict1 = ('국어': 55, '수학': 80, '과학': [30, 70, 80, 60])
    print (dict1)
    dict1['영어'] = "pass"
    print (dict1)
##### 요소 삭제는 del을 활용
    del dict1['수학']
    print (dict1)

##### key를 활용해 value를 출력
    print (dict1 ['수학'])

##### key만 출력
    print (dict1.keys())

##### value만 출력할땐 이렇게 합니다.
    print (dict1.values())

##### key와 value를 함께 출력합니다.
    print (dict1.items ())

#### 데이터 구조(set)

##### Set 선언
    
    ppap = {'pen', 'apple', 'pineapple', 'pen'}
    print(ppap)

    'apple' in ppap
    'applepen' in ppap
    
    pineapple = set('pineapple')
    pineapple
    
    A = set('golang')
    B = set('python')

<img src="https://github.com/code-hyun/study_python_crawling/assets/122762287/c6ce7111-7143-4107-87bc-d00435ae83c8" align="left">

<br><br><br><br><br><br><br>

------------------------------------------------------------------------------------------------------------------------------
# Crawling
## 크롤링이란?
    방대한 데이터를 활용할 필요성이 커지고 그러한 정보를 쉽고 활용하기 쉽게 데이터를 수집하는 행위를 크롤링이라고 한다.

### 크롤링의 핵심 코드
    * 라이브러리 임포트
    import requests // 웹페이지 가져오기 라이브러리
    from bs4 import BeautifulSoup // 웹페이지 분석(크롤링) 라이브러리

    * 웹페이지 가져오기
    res = reqeuests.get("웹사이트 주소")

    * 웹페이지 파싱하기
    soup = BeautifulSoup(res.content, 'html.parser')

    * 필요한 데이터 추출하기
    mydata = soup.find('title')

    * 추출한 데이터 활용하기
    print(mydata.get_text())
    
