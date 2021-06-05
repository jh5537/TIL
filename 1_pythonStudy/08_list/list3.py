'''
# 리스트의 요소를 제거: remove(), pop()
n = [1,2,3,4,5,3,4,-1,-5,-10]
# remove(삭제하려는 값)
n.remove(3) # ()안의 3은 순번이 아닌, 실제 값이 3인 요소를 제거함. 그 중에서도 왼편에서 시작해 제일 먼저 만나는 하나의 요소만을 제거함.
print(n) # remove() 안의 값이 리스트에 존재하지 않으면 오류가 발생.

# 같은 값을 가지는 모든 요소를 제거하려면
cnt = n.count(3) # 다음과 같은 구문을 통해 cnt만큼 삭제를 반복하여야 한다.

# pop() : 가장 마지막 값을 리스트에서 추출. 리스트에는 추출된 값이 존재하지 않게 되고, 추출된 값은 다른 변수에 할당할 수 있게 된다.
data = n.pop(4) # 삭제하는 값을 의미하는 remove와 달리 pop의 ()는 index. 쓰지 않으면 가장 마지막 값, 입력할 경우 해당 인덱스 위치의 값을 반환.
print(n)
print(data)

# extend(): append와 insert의 기능이 합쳐진 것.
a = [3, 6, 0, -4, 1]
b = [40, 30, 20, 50]

a.append(b) # append를 사용하여 리스트를 추가하면 리스트 내부의 요소로 추가됨.
print(a)
a.remove(b)
a.insert(2, b) # insert도 해당 인덱스에 리스트를 요소로서 추가함.
print(a)
a.remove(b)
a.extend(b)
print(a) # extend는 리스트의 개별 요소를 추가함.

# 리스트의 요소를 정렬: sort(), reverse() / 함수 - sorted
a = [3, 6, 0, -4, 1]
print(a)
a.reverse() # 해당 리스트를 반대 순서로 정렬.
print(a)
a.sort() # 리스트 내부의 요소가 오름차순으로 정렬.
print(a)
a.sort(reverse=True) # 내림차순 정렬.
print(a)

# reverse() 메소드를 사용하지 않고 리스트를 역순으로 생성하여 출력하기
b = []
for i in range(len(a)):
    b.append(a.pop()) # a 에서 뒤부터 추출하여 b에 할당.
print(b)

# sorted 함수: 내림차순으로 정렬된 리스트를 생성.
a = [3, 6, 0, -4, 1]
c = sorted(a)
print(c)

# string의 정렬
string = ['Apple', 'GRAPE', 'aPPle', 'banana', 'melon', 'apple']
print(string)
string.sort() # 대문자가 소문자보다 앞에 오도록 정렬한 후 알파벳 순으로 정렬.
print(string)
string.sort(key=str.upper) # 알파벳 순으로 정렬한 후 대문자가 소문자보다 앞에 오도록 정렬.
print(string)

# max(), min()
a = [3, 6, 0, -4, 1]
string = ['Apple', 'GRAPE', 'aPPle', 'banana', 'melon', 'apple']

print(max(a)) # 가장 큰 값을 출력.
print(min(a)) # 최솟값 출력.

print(max(string)) # (알파벳 순으로) 가장 뒤에 있는 값 출력.
print(min(string)) # 가장 앞에 있는 값을 출력.

# index() 메소드: string에서와 유사하게 list에서도 해당하는 값을 가져올 수 있음.
b = a.index(6) # 리스트 중에서 해당하는 값이 있는 위치(index)를 반환함. 값이 존재하지 않으면 오류 출력.
print(b)

# in / not in: 해당 값이 존재하는지 확인.
if 2 in a:
    print('Exist')
else:
    print('Not exist')

if 7 not in a:
    print('Not exist')
else:
    print('Exist')

# 리스트의 일치 검사: 리스트에도 ==, !=, >, <의 연산자를 사용할 수 있다.
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [3, 1, 2]

print(list1 == list2) # True
print(list1 == list3) # False

# 2차원 리스트: 리스트 안에 또 다른 리스트가 들어있는 경우.
list3 = [[1, 2, 3, 6], [4, 9, 5, 6], [0, 7, 8, 9]]
list4 = [[1, 2, 3], [1, 2], [1, 3, 4, 5]]
print(list3)

# 2차원 리스트의 시각화: for문을 활용
for i in list3:
    print(i)

for i in list3:
    for j in i:
        print(j, end=' ')
    print()

print(list3[1][1]) # 두 번째 행, 두 번째 열의 값을 출력.
print(len(list3)) # 행의 길이
print(len(list3[0])) # 열의 길이
'''
# 2차원 리스트 연습문제: 10명의 학생의 국어, 영어, 수학 점수가 2차원 리스트 형식으로 저장된 경우.
# 각 학생별 세 과목의 총점과 평균 점수를 계산하여 과목점수와 함께 출력하는 코드 작성
scores = [[90, 85, 70], [88, 72, 92], [100, 100, 90], [90, 60, 50], [30, 40, 50], [99, 49, 10], [100, 80, 76],
          [22, 33, 44], [11, 55, 99], [80, 70, 30]]
sum = avg = 0
for i in range(len(scores)):
    k = int(len(scores[i]))
    for j in range(k):
        sum += scores[i][j]
    avg = sum/k
    print(scores[i], ' %d, %.1f' % (sum, avg))
    avg = sum = 0
"""짧은 코드
for s in scores:
    total = sum(s) # sum 함수를 활용하여 (수치형) 리스트 내부 요소를 전부 더함.
    print(f"{s}, {total}, {total/len(s):.2f}") # format으로 표현
"""
# 참고할 수 있는 함수
print(round(70.5555, 1)) # 해당 수치를 소숫점 n번째 자리에서 반올림하여 표현.
