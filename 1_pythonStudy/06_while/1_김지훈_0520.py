# 실습 문제 1번
# 1)
for a in range (5):
    print("*"*(5-a))
"""모범답안
for i in range(5,0,-1)
    for j in range(i)
        print('*', end='')
    print()
    """
print("--------------------------------")
# 2)
for b in range (5):
    print(" "*(4-b),"*"*(2*b+1)," "*(4-b))
"""모범답안
for i in range(5, 0, -1):
    for j in range(i-1):
        print(' ', end='')
    for j in range(11-2*i):
        print('*', end='')
    print()
    """
print("================================")
# 2번
num = int(input("숫자 입력 : "))
while num != 7:
    num = int(input("다시 입력 : "))
print("7 입력! 종료")
"""모범답안
num = int(input("숫자 입력 : "))
while True:
    if num == 7:
        print(num, ' 입력! 종료')
        break
    else:
        num = int(input('다시 입력 : '))
"""
print("================================")
# 3번
poc = 10000
song = 1
while poc > 0:
    print("노래를 %d곡 불렀습니다." % song)
    song += 1
    poc -= 2000
    if poc > 0:
        print("현재 %d원 남았습니다." % poc)
    else:
        break
print("잔액이 없습니다. 종료합니다.")
