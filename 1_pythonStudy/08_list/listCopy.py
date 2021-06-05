# 리스트의 복사

# 얕은 복사 - 주소를 복사하는 개념. 이름이 두 개인 하나의 리스트.
scores = [65, 70, 90, 89, 78]
value = scores # 리스트 복사됨(얕은 복사).

print('scores :', scores)
print('value :', value)

scores[3] = 98

print('scores(값변경) :', scores)
print('value :', value) # =를 사용한 복사는 값이 연동됨.

value[0] = 100

print('scores :', scores)
print('value(값변경) :', value) # 두 리스트 중 어느 하나의 요소를 변경하면 다른 리스트에도 반영

# 깊은 복사 - 내용이 같은 새로운 리스트를 생성. 리스트 요소가 서로 독립되어 있음.
value2 = scores.copy()
print('value2', value2)
scores[0] = 50
print('scores :', scores)
print('value :', value)
print('value2 :', value2)

value3 = list(scores)
print('value3', value3)
print('scores', scores)
scores[1] = 150
print('scores :', scores)
print('value :', value)
print('value2 :', value2)
print('value3 :', value3)

import copy
value4 = copy.deepcopy(scores)
print('value4', value4)
scores[2] = 300
print('value4 :', value4)
print('scores :', scores)