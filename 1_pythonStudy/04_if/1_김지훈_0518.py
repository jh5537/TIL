# 1번 문제
k = input("16진수 한 글자 입력 : ")
if '0' <= k <= '9' or 'a' <= k <= 'f' or 'A' <= k <= 'F': # 문자열에서도 관계연산자(<=) 사용 가능. 소문자와 대문자는 별개로 인식함.
    print("10진수 ==> %d" % int(k,16))
else:
    print("16진수가 아닙니다")

print("========================================")
# 2번 문제
m = int(input("교환할 돈은 얼마 ? "))
q = m//50000 # q=5만원권
rq = m%50000
w = rq//10000 # w=1만원권
rw = rq%10000
e = rw//5000 # e=5천원권
re = rw%5000
r = re//1000 # r=1천원권
rr = re%1000
t = rr//500 # t=5백원
rt = rr%500
y = rt//100 # y=1백원
ry = rt%100
u = ry//50 # u=50원
ru = ry%50
i = ru//10 # i=10원
ri = ru%10
print("  50000원 %d장, 10000원 %d장, 5000원 %d장, 1000원 %d장" % (q,w,e,r))
print("  500원 %d개, 100원 %d개, 50원 %d개, 10원 %d개" % (t,y,u,i))
print("  바꾸지 못한 돈 ==> %d원" % ri)

print("========================================")
# 3번 문제
from random import randint
An = randint(1, 6)
Bn = randint(1, 6)
print("A의 주사위 숫자는 %d 입니다." % An)
print("B의 주사위 숫자는 %d 입니다." % Bn)
if An > Bn:
    print("A가 이기고 B는 졌다.")
elif An == Bn:
    print("A와 B가 비겼다.")
else:
    print("B가 이기고 A는 졌다.")