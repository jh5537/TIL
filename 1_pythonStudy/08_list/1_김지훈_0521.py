# 연습 문제 1
print("1번")
member = []
for i in range(3):
    name = input('회원 입력 : ')
    member.append(name)
print("회원 명단 :  %s %s %s" % (member[0], member[1], member[2]))
"""모범답안(명단 출력)
print('회원 명단 : ', end='')
for i in member:
    print(i, end='')
"""
print("==============================")
# 연습 문제 2
print("2번")
scores = []
sum = avg = over = 0
k = int(input("학생 수 입력 : "))
for j in range(k):
    score = int(input("학생 %d 점수 입력 : " % (j+1)))
    scores.append(score)
    sum += score
    if score >= 80:
        over += 1

print("총점 : %d" % sum)
avg = sum/k
print("평균 : %.2f" % avg)
print("80점 이상 학생 : %d명" % over)
print("==============================")
# 연습 문제 3
print("3번")
goods = []
q = input("상품 등록 (엔터키 누르면 종료) : ")
while q != '':
    goods.append(q)
    q = input("상품 등록 (엔터키 누르면 종료) : ")
print("등록된 상품 : ", end='')
for w in range(len(goods)):
    print(" %s" % goods[w], end=' ')
# print(*goods)를 사용할 경우에도 개별 요소의 값만 출력할 수 있음.