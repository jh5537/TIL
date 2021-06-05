# 연습 문제 4
print("4번")
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
scores.sort(reverse=True)
print("점수 내림차순 정렬 : ", scores)
print("==============================")
# 연습 문제 5
print("5번")
saja = ["개과천선", "구사일생", "군계일학", "무용지물", "동고동락", "유비무환", "입신양명", "괄목상대", "막역지우", "고장난명"]
sung = ["잘못을 고치고 옳은 길에 들어섬", "죽을 고비를 여러 번 겪으며 살아나다", "평범한 사람 가운데 뛰어난 사람",
        "아무짝에도 쓸모없는 것", "고통과 즐거움을 함께 한다", "미리 준비해두면 근심 걱정이 없다",
        "사회적으로 인정받고 출세하여 이름을 세상에 드날림", "다른 사람의 학식이나 업적이 크게 진보한 것을 말함",
        "생사를 같이 할 수 있는 친밀한 벗", "상대 없이 혼자서는 어떤 일을 이룰 수 없다"]
print("사자성어 맞추기 게임을 시작합니다.")
print("-----------------------------")
from random import randint # 랜덤 임포트는 코드의 가장 윗줄에 작성하는 것이 바람직함.
uh = randint(1, 10)
# uh = randint(1, len(sung)) 으로 표현해야 문제의 수가 늘어나도 대응 가능.
print("%s" % sung[uh])
dap = input("이 말의 사자성어는? : ")
print()
while dap != saja[uh]:
    print("틀렸습니다... 다시 도전!")
    print()
    print("%s" % sung[uh])
    dap = input("이 말의 사자성어는? : ")
    print()
print("맞습니다... 게임을 종료합니다.")
""" 틀릴 때마다 문제를 바꾸는 형식의 코드.
while True:
    uh = randint(1, len(sung))
    print(sung[uh])
    dap = input('이 말의 사자성어는? : ')
    if dap == saja[uh] :
        print('\n맞습니다... 게임을 종료합니다.')
        break
    else:
        print('\n틀렸습니다... 다시 도전!')
"""
