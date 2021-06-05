# 1. my_variable 이름의 비어있는 튜플을 만들라.
print("1번")
my_variable = () # my_variable = tuple()도 사용 가능.
print(my_variable)
print("==============================")

# 2. 다음 코드를 실행해보고 오류가 발생하는 원인을 설명하라.
# >> t = (1, 2, 3)
# >> t[0] = 'a'
# Traceback (most recent call last):
#  File "<pyshell#46>", line 1, in <module>
#  t[0] = 'a'
# TypeError: 'tuple' object does not support item assignment
print("2번")
print("튜플은 정의된 후 가지고 있는 요소의 수정, 추가, 삭제가 불가능하다. 따라서 t[0]의 값을 'a'로 바꾸는 것은 불가능하다.")
print("==============================")

# 3. 숫자 1 이 저장된 튜플을 생성하라.
print("3번")
tp = (1, ) # tp = (1)이라고 입력할 경우, 변수의 값이 튜플이 아닌 정수 1로 저장됨에 주의. 쉼표,를 사용하거나, 리스트를 만든 후 튜플로 변환하여야 함.
"""
num = list()
num.append(1)
tp = tuple(num)
"""
print(tp)
print("==============================")

# 4. 아래와 같이 t에는 1, 2, 3, 4 데이터가 바인딩되어 있다. t가 바인딩하는 데이터 타입은 무엇인가?
# t = 1, 2, 3, 4
print("4번")
t = 1, 2, 3, 4
print(type(t))
print("튜플")
print("==============================")

# 5. 변수 t에는 아래와 같은 값이 저장되어 있다. 변수 t가 ('A', 'b', 'c') 튜플을 가리키도록 수정 하라.
#  t = ('a', 'b', 'c')
print("5번")
t = ('a', 'b', 'c')
listt = list(t)
listt[0] = 'A'
t = tuple(listt)
print(t)
print("==============================")

# 6. 다음 튜플을 리스트로 변환하라.
# interest = ('삼성전자', 'LG전자', 'SK Hynix')
print("6번")
interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest = list(interest)
print(interest)
print("==============================")

# 7. 다음 리스트를 튜플로 변경하라.
# interest = ['삼성전자', 'LG전자', 'SK Hynix']
print("7번")
interest = ['삼성전자', 'LG전자', 'SK Hynix']
interest = tuple(interest)
print(interest)
print("==============================")

# 8. 파티에 참석한 사람이 다음과 같을 때 집합을 생성하고, 아래 조건에 맞게 출력하시오.
# partyA : "Park","Kim","Lee"
# partyB : "Park","길동","몽룡"

# 1) 파티에 참석한 모든 사람은?
# 2) 2개의 파티에 모두 참석한 사람은?
# 3) 파티 A에만 참석한 사람
# 4) 파티 B에만 참석한 사람
print("8번")
partyA = {"Park","Kim","Lee"}
partyB = {"Park","길동","몽룡"}
print("1)")
all = partyA | partyB # partyA.union(partyB)
print(*all)

print("2)")
every = partyA & partyB # partyA.intersection(partyB)
print(*every)

print("3)")
Aman = partyA - partyB # partyA.difference(partyB)
print(*Aman)

print("4)")
Bman = partyB - partyA # partyB.difference(partyA)
print(*Bman)