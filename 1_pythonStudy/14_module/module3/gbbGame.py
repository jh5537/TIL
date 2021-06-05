def gbb_game(you_n):
    from random import randint
    cn = randint(1, 3)
    if cn-you_n == -2 or cn-you_n == 1:
        print("컴퓨터가 이겼습니다.")
    elif cn-you_n == 0:
        print("비겼습니다.")
    else:
        print("당신이 이겼습니다.")
    return cn

def input_num():
    yn = int(input('YOU 입력 (1:가위, 2:바위, 3:보) : '))
    print("COM : %d" % (gbb_game(yn)))
