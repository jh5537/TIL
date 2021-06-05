# 딕셔너리 dictionary : key와 value(값)으로 구성. 중괄호 사용. {키1:값1, 키2:값2, ...}

d = {} # 또는 d = dict(): 빈 딕셔너리 생성.
d = {1:'a', 2:'b', 3:'c'} # item: 키와 값의 짝
print(d)
print(type(d))

# 딕셔너리의 요소(아이템)에 접근할 때에는 인덱스를 쓰지 않고, 키를 사용.
print(d[1]) # 키에 해당하는 값을 반환.

d2 = {'name' : 'Lee', 'tel':'010-111-1111'} # 문자열도 키가 될 수 있음. 값에도 여러 형태의 데이터가 가능.
print(d2['name'])

# 딕셔너리에 요소 추가
d[4] = 'f' # []안에 키, 등호 뒤에 값을 입력하여 딕셔너리에 키:값의 요소를 추가할 수 있음.
print(d)

d2['address'] = '서울시 강남구'
print(d2)

# keys(), values(), items() 메소드
d3 = {'name':'daum',
      'url':'www.daum.net',
      'userid':'dm',
      'pw':1234}
d3_key = d3.keys() # 키의 요소를 리스트 형태로 출력(형태만 리스트, 자료형은 리스트 아님).
print(d3_key)
print(type(d3_key)) # dict_keys 딕셔너리 키 자료형.
print(list(d3_key)[1]) # 키 자료형을 리스트로 변환하여 반환.

d3_value = d3.values() # 밸류를 리스트 형태로 출력.
print(d3_value)
print(type(d3_value)) # dict_values 딕셔너리 밸류 자료형.

d3_item = d3.items() # 아이템을 출력.
print(d3_item) # 아이템 요소 자체는 리스트로 되어 있으나 각 아이템(키-밸류 쌍)은 튜플 형태로 묶여 있음.
print(type(d3_item)) # dict_items 딕셔너리 아이템 자료형.
print(list(d3_item)[0]) # 아이템을 리스트로 변환하여 요소 하나를 출력 - 해당 요소는 튜플의 형태.

# for와 if를 응용하여 찾고자 하는 키, 밸류를 대응할 수 있음.
for key in d3.keys():
    print(key)
for value in d3.values():
    print(value)
for item in d3.items():
    print(item)

print(d3['name']) # 입력한 키에 맞는 밸류를 반환. 그러나, 해당 키가 존재하지 않을 경우에 오류 발생.
print(d3.get('url')) # get을 사용하면 해당 키가 존재하지 않을 때 None을 반환.
print(d3.get('asdf'))
print(d3.get('asf', 'not exist')) # 해당 키가 존재하지 않을 때 , 이후의 문자열을 출력하도록 설정도 가능.

k = 'link'
if d3.get('k') is None: # is 함수
    print(k + '에 대한 데이터가 없음')

# in / not in
print('link' in d3) # 해당 키가 존재하지 않으므로 False 출력.
print('link' not in d3)
print('name' in d3)

# dictionary 객체의 메소드들
print(dir(d3))
"""['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', 
'__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', 
'__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', 
'__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', 
'__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 
'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
"""

print(d3.popitem()) # 가장 마지막에 있는 항목을 추출.
print(d3) # 기존 딕셔너리에서는 popitem으로 추출된 요소 사라짐.

# d.clear() : 딕셔너리 내 요소를 전부 지우고 빈 딕셔너리로 만들어 줌. / del.

# copy, zip(), del, sorted() ...

# 컴프리헨션
et = {x: x**2 for x in (2, 4, 6)} # for를 이용하여 딕셔너리 내에 여러 요소를 추가할 수 있음. 리스트, 튜플에도 사용 가능
print(et)
y = [x**2 for x in (2,3,4)]
print(y)

for key, val in d3.items(): # (key, value) 형식으로 묶인 item을 각각 출력.
    print('%s : %s' %(key, val)) # 튜플()형식으로 묶이지 않고 출력.

students = {1 : [80, 86, 60], # 딕셔너리의 밸류를 2차원 리스트에 연동.
            2 : [87, 90, 30],
            3 : [33, 44, 55]}

endDict = {}
endDict['dog'] = '개'
endDict['cat'] = '고양이'
print(endDict)