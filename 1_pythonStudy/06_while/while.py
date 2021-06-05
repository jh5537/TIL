# while 구문 이해: 조건이 만족(True)하는 동안만 반복문을 수행.
'''
# 1~10까지의 정수를 출력
n = 1
while n <= 10:
    print(n, end=' ')
    n += 1 # 조건식에 변화를 주어 최종적으로 반복문을 탈출할 수 있도록 함. 없을 경우 무한루프.

# 1~100까지의 정수 중 3의 배수의 합을 출력
a = 1
sum = 0
while a <= 100:
    if a%3 == 0:
        sum += a
    a += 1
print(sum)
"""다른 방법으로 출력
a = sum = 0
wihle a<= 100:
    sum += a
    a += 3
또는
while a*3 <= 100:
    sum += a
    a += 1
"""
# 무한 반복: 조건문이 무조건 참인 경우 문장이 계속 반복. 반복문을 종료하기 위해서 break 사용.
while True: # 조건이 항상 참
    print("반복 수행되는 문장입니다.")
    answer = input("종료하려면 x 입력: ")
    if answer == 'x':
        break
print("종료했습니다.")
# continue문 : 반복문 수행 중에 continue를 만나면 현재 시점에서 중단하고 다음 반복을 계속 수행.
x = 0
while x < 10:
    x += 1
    if x % 2 == 0: # 짝수일 경우
        continue # 현재 수행을 중단하고 다음 반복을 수행
    print(x) # continue일 때는 출력되지 않아 결과적으로 홀수만 출력됨.
'''



