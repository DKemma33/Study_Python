import json

data = {'name': '책', 'price': 25_000, 'stock': 55}

# dict를 json으로 변환
# ensure_ancii: 한글을 원본으로 출력(기본은 유니코드, True),
# indent: 보기 좋게 바꾸며, 전달한 값은 들여쓰기 공백 개수이다
json_data = json.dumps(data, ensure_ascii=False, indent=4)

# json을 dict로 변환
data_dict = json.loads(json_data)
print(data_dict.__getitem__('name'))
