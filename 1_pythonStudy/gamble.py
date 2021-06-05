from random import randint

def repay(money, debt):
    if money > debt:
        maxrep = debt
    else:
        maxrep = money
    while True:
        rep = int(input("현재 잔고는 %d원, 대출금은 %d원입니다.\n얼마를 상환하시겠습니까? (최대 %d원)" % (money,debt,maxrep)))
        if maxrep > rep:
            debt -= rep
            money -= rep
            print("현재 잔고는 %d원, 대출금은 %d원입니다." % (money, debt))
            break
        elif maxrep < rep:
            print("그렇게는 할 수 없습니다. 다시 입력하려면")

        elif debt == rep:
            debt -= rep
            money -= rep
            print("대출을 모두 상환하셨습니다.")
        else:
            break
    return debt

money = money1 = int(input("잔고입력(단위: 원)"))
maxdebt = int(money1/10000)*5000
debt = 0
k = 0
while money>0:
    key = input("시작하시겠습니까?(y/n)")
    if key == 'n':
        break
    elif key == 'y':
        times = int(input("몇 번 플레이하시겠습니까?"))
        for t in range(times):
            k = randint(1, 10000)
            a = randint(900, 6500)
            b = 10000/randint(int(4*a/5), int(6*a / 5)) # 실제배당(랜덤)
            winr = round(a/10000, 3) * 100
            bet = int(input('%d회차 게임입니다. 승률은 %.1f%%, 배당률은 %.2f입니다.\n얼마를 거시겠습니까? (최대 %d원)'
                            % (t+1, winr, b, money)))
            if bet > money:
                print('돈이 부족합니다.')
                print('현재 잔고 %d원' % money)
                break
        # 구현하고 싶은 것 : 빚, 빚에 대한 1판당 이자율(이자율 설정 기준은?), 상환(함수정의)
            # 초기 시드머니에 따른 빚의 한도 설정(.
            money -= bet
            if a >= k:
                win = int(b * bet)
                print('승리했습니다. 상금은 %d원입니다.' % win)
                money += win
                print('현재 잔고 %d원' % money)
            else:
                print('패배했습니다.')
                print('현재 잔고 %d원' % money)
            if money<=0:
                print('돈이 다 떨어졌네요!')
                break
            elif money >= 2*money1:
                print('많이 따셨네요. 그만 들어가시죠.')
if k != 0:
    if money > money1:
        print('돈 버셨네요!')
    else:
        print('다음엔 딸 수 있을거에요.')
print('안녕히가세요.')
