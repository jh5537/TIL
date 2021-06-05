'''
# for문 예시
for name in ["홍길동", "이몽룡", "성춘향", "변학도"]:
    print(name)

for x in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print(x)

for num in range(1, 10): # range(a, b)는 a 이상 b '미만'인 정 이므로 b는 포함되지 않음. a,가 공백일 경우 시작은 0.
    print(num, end= ' ') # end = 을 이용하여 한 줄에 출력할 수 있음.

print('\n==============================') # \n을 이용해 행 띄움.
# 실행 단축키 ⌃⇧R

# range(start, stop, step): start에서 stop-1까지 step 간격으로 정수 생성.
for i in range (10): # 특정 범위의 정수 생성.
    print (i, end=' ')
print('\n----------------')
for i in range (1, 10): # start에서 stop-1까지의 정수.
    print(i, end=' ')
print('\n----------------')
for i in range (2, 10, 2): # start에서 stop-1까지 step의 간격으로 정수 생성. 즉, range(10)은 range(0, 10, 1)과 같음.
    print(i, end=' ')
print('\n----------------')
for i in range (12, 1, -3): # step이 음수일 경우 점점 줄어드는 수열을 형성.
    print(i, end=' ')
print('\n----------------')

# 1~10 사이의 수를 더하고, 더한 결과 출력
num = 0 # 누적변수가 반드시 초기화 되어야 함(num=0). 변수가 정의되지 않거나 다른 임의의 값이 입력되어 있으면 안 됨.
for i in range (1, 11):
    num = num + i
print(num)

# 1에서 100까지 합 구하기
num = 0
for i in range (1, 101):
    num = num + i # num += i로도 쓸 수 있음.
print("1에서 100까지의 합은 %d 입니다." % num)

# 1에서 20까지의 정수 중 3의 배수만 출력한 뒤, 합을 구하기
sum = 0
for i in range (3, 21, 3):
    print(i, end=' ')
    sum += i
print("\n3의 배수의 합은 %d 입니다." % sum)

# range의 step을 쓰지 않고 ~
sum = 0
for i in range(1,21):
    if i%3 == 0:
        print(i, end=' ')
        sum += i

print("\n3의 배수의 합은 %d 입니다." % sum)
# 또는
for i in [1, 2, 3, 4, 5, 6]:
    x = i*3
    print(x, end=' ')
    sum += x

print("\n3의 배수의 합은 %d 입니다." % sum)

# 두 숫자를 입력받아서 그 수 사이에 있는 숫자의 합을 구하기
a = int(input('숫자1 입력 : '))
b = int(input('숫자2 입력 : '))
sum = 0

if(a <= b):
    for i in range(a, b+1):
        sum += i
    print("%d와(과) %d사이의 합은 %d입니다." % (a, b, sum))
else:
    for i in range(b, a+1):
        sum += i
    print("%d와(과) %d사이의 합은 %d입니다." % (a, b, sum))

# 구구단의 단 수를 입력받아서 해당 구구단 출력
c = int(input('단 수 입력 : '))
for k in range(1, 10):
    d = c * k
    print("%d * %d = %2d" % (c, k, d)) # 결과값 항에 2d를 입력하여 두자리 단위로 표시를 정렬.

# 카운트 다운 프로그램 작성
e = int(input("시작 숫자를 입력하시오: "))
for j in range(e, 0, -1):
    print(j, end=' ')
print("발사")

# 숫자 10개를 입력받아 양, 음, 0의 개수를 출력
n1 = int(input('숫자1입력 : '))
n2 = int(input('숫자2입력 : '))
n3 = int(input('숫자3입력 : '))
n4 = int(input('숫자4입력 : '))
n5 = int(input('숫자5입력 : '))
n6 = int(input('숫자6입력 : '))
n7 = int(input('숫자7입력 : '))
n8 = int(input('숫자8입력 : '))
n9 = int(input('숫자9입력 : '))
n10 = int(input('숫자10입력 : '))
print('--------------------')
numbers = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]
q = w = e = 0
for a in numbers:
    if a > 0:
        q += 1
    elif a < 0:
        w += 1
    else:
        e += 1
print('양의 개수 : %d' % q)
print('음의 개수 : %d' % w)
print('0의 개수 : %d' % e)

# 모범답안
p = n = z = 0
for i in range(1, 11):
    number = int(input('숫자{} 입력 : '.format(i)))
    if number > 0:
        p += 1
    elif number < 0:
        n += 1
    else:
        z += 1
print('--------------------')
print('양의 개수 : %d' % p)
print('음의 개수 : %d' % n)
print('0의 개수 : %d' % z)

# 다음과 같이 이름이 명단에 있는지 검색
nameboard = ["홍길동", "이몽룡", "성춘향", "변학도"]
name = input("이름 입력: ")
"""
for n in nameboard:
    if name == n:
        print("명단에 있습니다.")
        break               # break는 반복문(for, while)을 벗어날 때 사용.
    else:
        print("명단에 없습니다.")
그러나 이 방식으로 코드를 짜면, '명단에 없습니다'가 반복되어 출력됨. 아래와 같이 논리값을 주는 신호를 사용하여 해소."""
for n in nameboard:
    if name == n:
        f = True
        break
if f:
    print("명단에 있습니다.")
else:
    print("명단에 없습니다.")

# 다중 for문(중첩 루프)
for y in range(3):
    for x in range(5):
        print(x, end=' ')
    print() # 공백 행 출력

for i in range(3):
    for j in range(4):
        print("%3d" % (i*4+j+1), end=' ')
    print()

# 다른 방법
a = 0
for i in range(3):
    for j in range(4):
        a+=1
        print(a, end="\t")
    print() # 행 띄우기
'''
# 구구단 출력
for dan in range(2,10):
    for n in range(1, 10):
        print("%d * %d = %s" % (dan, n, str(dan * n)))
    print()

