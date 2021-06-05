# 리스트의 기본 개념

intL = [1, 3, 4, 5,]
floatL = [1.4, 3.2, 5.6]
nameL = ['홍길동', '성춘향', '변학도', '방자']
numL = [1, 3, 4, [1, 2]] # 리스트의 값으로 리스트를 가질 수 있음.
samL = [1, 3, 2.5, '하하'] # 다양한 종류의 데이터를 값으로 가질 수 있음.
'''
print(intL)
print(type(intL))
print(numL)
print(samL)

for x in numL: # 리스트의 요소를 각각 직접 대입하여 출력.
    print(x)
for i in range(len(numL)): # 길이함수와 위치인덱스를 이용하여 리스트의 요소를 출력.
    print(numL[i])

a, b, c = floatL # 리스트의 각 요소를 a, b, c에 하나씩 할당. 단, 변수의 개수가 리스트 요소의 개수와 일치해야 함.
print(a)
print(b)
print(c)

# 인덱싱과 슬라이싱
print(nameL[-1]) # 가장 뒤의 요소 출력.
print(nameL[-1:]) # 가장 마지막 요소(부터 끝까지).
print(nameL[:-1]) # 리스트의 처음부터, 마지막에서 하나를 뺀 곳까지.
print(nameL[:]) # 전체 요소 출력.
print(nameL[1:3]) # 두 번째와 세 번째 요소 출력. 문자열 인덱싱과 같은 원리.
print(numL[-1][0]) # 리스트의 요소가 리스트일 경우, 이중 인덱싱(대괄호 2번[][])을 통해 요소인 리스트의 요소를 추출할 수 있음.

# allL = [] - 비어 있는 리스트를 생성.
# allL = list() - 비어 있는 리스트를 생성하는 함수.
allL = [intL, floatL, nameL, numL]
print(allL)
print(allL[-1])
print(allL[-1][-1])
print(allL[-1][-1][0]) # 다중 인덱싱을 통한 리스트 속 리스트의 요소 추출.

print(len(nameL)) # 리스트의 길이 측정.
n = len(nameL)
print(nameL[:n]) # 리스트의 길이를 활용해 리스트의 요소 출력.

# 리스트의 +, * 연산
sumL = numL + samL # 연산자를 이용한 리스트 합치기.
print(sumL)
print(numL * 3) # * 연산자를 통해 리스트 반복 가능.
'''
# 리스트의 내용 변경
print(numL)
numL[-1] = 10 # 리스트 인덱싱을 통해 리스트 요소를 다른 것으로 교체.
print(numL)
numL[2:4] = [] # 리스트의 값을 삭제하는 경우.
print(numL)

