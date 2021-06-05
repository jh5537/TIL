# set: 집합형. 중복되지 않은 항목이 모인 것. 순서가 없다.
# 집합 만들기
'''
s1 = {1, 2, 3, 4, 5} # s1 = set() 함수를 사용해도 집합 생성 가능.
print(s1)
print(type(s1)) # set(집합) 자료형

# 리스트로 집합 생성
l1 = [10, 20, 30, 20, 30]
s2 = set(l1) # set은 중복을 허용하지 않으므로, 중복된 값은 지워지고 각 요소가 하나씩만 포함.
print(s2)

# set의 요소는 변경 불가능해야 함. 즉, 튜플은 집합의 요소가 될 수 있으나, 리스트는 집합의 요소가 될 수 없음.
# set은 인덱스 사용 불가. s1[0] 등은 오류 발생.
# 그러나 set에 요소 추가나 삭제는 가능. append, insert 대신 .add() 사용.
s2.add(90)
print(s2)

# 데이터 삭제: .remove(), .discard(), .clear(), del
s2.remove(10) # 존재하지 않는 값을 remove하면 오류 발생.
print(s2)
s2.discard(20)
print(s2)
s2.discard(1) # discard는 존재하지 않는 값을 삭제시도 해도 오류 발생하지 않음.
print(s2)
s2.clear() # clear는 리스트, 튜플... 과 마찬가지로 내부 요소를 전부 삭제함.
print(s2)
del s2 # 비어있는 집합 set()를 아예 지우려면 del 사용.
'''
# 집합 연산: union(합집합), intersection(교집합), difference(차집합)
s1 = {3, 4, 1, 6}
s2 = {2, 4, 5, 8, 3}
print(s1.union(s2)) # 합집합. (s1 | s2)로도 사용 가능.
print(s1.intersection(s2)) # 교집합 (s1 & s2)
print(s1.difference(s2)) # 차집합 - s1과 s2 위치가 바뀌면 결과값이 바뀜. (s1 - s2)
print(s2.difference(s1))

a = set('abracadabra') # 문자열을 집합화하면 개별 낱문자들이 집합의 요소가 됨. *주의: {'orange', 'banana', 'pear', 'apple'} 형태와 구분.
b = set('alacazam')
print(a)
print(b)
print(a^b) # ^는 합집합 - 교집합

# set 컴프리헨션
a = {x for x in 'abracadabra' if x not in 'abc'} # in 과 not in도 마찬가지로 사용 가능.
print(a)
