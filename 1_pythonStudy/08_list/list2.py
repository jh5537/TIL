# 리스트의 주요 메소드

a = [1,2,3,4,5,6,3,9,3,4,5]
# 리스트의 길이 계산 함수: len(리스트명)
print('리스트의 길이 %d' % len(a))

# 리스트의 요소 찾기: count() - ()안에 해당하는 요소가 몇 개 있는지 찾아서 표시.
print(a.count(3))

# 리스트의 요소 추가, 삽입: append()-리스트의 가장 뒤에 요소 추가, insert()-삽입하려는 위치를 지정하여 요소 추가.
a.append(100)
print(a)
a. append([110,120]) # 리스트에 리스트를 요소로 추가할 수 있음.
print(a)

a.insert(2, 100) # 2에 해당하는 위치(세 번째 자리)에 100을 요소로 삽입.
print(a)

b = [] # 빈 리스트 생성
b.append(5.5)
print(b)
b.append(10.5)
print(b)
b.append(6.5) # append를 반복하여 빈 리스트 안에 값을 채움.
print(b)

scores = [] # for문을 사용해 리스트를 채우는 경우.
for i in range(10):
    score = int(input('점수 입력: '))
    scores.append(score) # 입력한 점수가 뒤에 추가됨.
    # socres.insert(0,score) - 새로 입력한 점수를 앞에 삽입할 경우 사용.
print(scores)

# 리스트의 요소 제거: remove(), pop()
# 리스트의 확장: extend()
# 리스트의 요소를 정렬: sort()-오름차순 정렬, reverse()-순서 뒤집기
# 리스트의 요소 찾기: index()
# 리스트 요소 중 특정한 값을 찾기: max()-가장 큰 값 찾기, min()-가장 작은 값 찾기

