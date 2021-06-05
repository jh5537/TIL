'''
# 집합적 자료형: tuple. 리스트는 대괄호[]or list()를 사용하는 것과 달리 튜플은 소괄호()or tuple()를 사용함.
t1 = tuple()
t2 = ()

t1 = (1, 2, 3)
print(t1)
print(type(t1))

t2 = 1, 3, 4 # 자료를 나열하기만 해도 튜플 형식으로 저장.
print(t2)
print(type(t2))

t3 = t1, (5, 6, 7) # 2차원 형식의 튜플을 생성할 수도 있음.
print(t3)

t4 = [1, 4], [5, 6] # 리스트를 요소로 가지고 있는 튜플.
print(t4)

t5 = tuple([1,4]) # tuple()함수를 이용하여 리스트를 튜플 형식으로 변환.
print(t5)

# 튜플의 요소 다루기
print(t1[2]) # 인덱스에 해당하는 요소 출력(리스트와 동일한 원리).
# t1[2] = 10 등으로 튜플 요소를 다른 값으로 수정할 수는 없음.
# t1.append(-9) 요소를 추가하는 것도 불가능.
# del(t1[2]) 요소 삭제도 불가능.

del(t1) # 그러나 튜플 자체를 삭제하는 것은 가능함.

# tuple.index(), .count()
tt = 'a', 'b', 'c', 'e', 'a', 'd'
i = tt.index('e') # .index()를 활용하여 ()안의 요소의 위치(인덱스)를 확인할 수 있음.
print(i)
c = tt.count('a') # .count()를 활용하여 튜플 내 해당 요소의 개수를 확인할 수 있음.
print(c)

# slicing
t = tt[:] # 튜플 전체 반환.
print(t)
t = tt[1:5] # 튜플 1~5의 값을 반환(리스트와 동일한 원리).
print(t)

# +, * 연산
t1 = (1, 2, 3)
t2 = 1, 3, 4
print(t1 + t2) # 기존의 튜플을 수정할 수는 없지만, 연산자를 이용하여 새로운 튜플을 생성하는 것은 가능.
print(tt * 2) # 합연산과 곱연산 모두 적용. 새로운 튜플을 생성.

# 튜플 연습문제
tt = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(tt[1][2]) # 2차원 튜플의 요소 접근도 리스트와 동일.

# for문을 활용한 2차원 튜플의 전개(리스트와 동일).
for i in tt:
    for j in i:
        print(j, end=' ')
    print()

for i in tt:
    print(*i) # *튜플을 활용할 수도 있음.

# tuple의 값을 새로이 설정하는 법.
myTuple = (10, 20, 30) # (10, 20, 30, 40)으로 만들기.
myList = list(myTuple) # list() 함수를 사용하여 튜플의 요소를 리스트에 입력.
print(myList)
myList.append(40)
print(myList)
myTuple = tuple(myList) # tuple() 함수를 사용하여 요소를 추가한 리스트를 튜플에 입력.
print(myTuple)

t4 = [1, 4], [5, 6]
print(t4[0])
print(type(t4[0]))
t4[0][0] = 10 # 튜플 자체의 요소는 바꿀 수 없지만, 튜플 내 리스트의 요소는 수정할 수 있음.
print(t4)
'''
l1 = []
print(dir(l1)) # 디렉토리를 통해 리스트에서 사용할 수 있는 메소드를 표시.
"""['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', 
'__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', 
'__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', 
'__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
'__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 
'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'] """

t1 = ()
print(dir(t1)) # 튜플에서 사용할 수 있는 메소드 표시.
"""['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', 
'__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', 
'__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', 
'__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', 
'__str__', '__subclasshook__', 'count', 'index'] """
