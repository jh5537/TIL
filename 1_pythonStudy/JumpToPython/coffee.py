coffee = 10
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print ("커피를 줍니다.")
        coffee = coffee -1
    elif money > 300:
        print ("거스름돈 %d원을 주고 커피를 줍니다." % (money -300))
        coffee = coffee -1
    else:
        print ("돈 %d원을 토해냅니다. 커피는 주지 않습니다." % money)
        print ("남은 커피는 %d개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
    