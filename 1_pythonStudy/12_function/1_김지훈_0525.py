# 1번
print("1번")
def print_coin():
    print("비트코인")

# 2번
print("2번")
print_coin()

# 3번
print("3번")
for i in range(100): # for _ in range(100): 으로 표현할 수도 있음.
    print_coin()

# 4번
print("4번")
def print_coins():
    for i in range(100):
        print("비트코인")

print_coins()

# 5번
print("5번")
"""
hello() 
def hello(): 
    print("Hi") 

[실행 결과] 
NameError: name 'hello' is not defined """
print("함수의 정의는 함수의 호출보다 앞에 위치해야 한다. 해당 코드는 함수의 정의에 앞서 함수를 호출했기 때문에 정의되지 않았다는 내용의 에러가 출력되었다.")

# 6번
print("6번")
print('-'*13, '내 예측', '-'*13)
print('A\nB\nC\nA\nB')
print('-'*14, '결과', '-'*14)
def message():
    print("A")
    print("B")

message()
print("C")
message()

# 7번
print("7번")
print('-'*13, '내 예측', '-'*13)
print('A\nA\nC\nB')
print('-'*14, '결과', '-'*14)
print("A")

def message():
    print("B")

print("A")
print("C")
message()

# 8번
print("8번")
print('-'*13, '내 예측', '-'*13)
print('A\nC\nB\nE\nD')
print('-'*14, '결과', '-'*14)
print("A")
def messages1():
    print("B")

print("C")
def messages2():
    print("D")

messages1()
print("E")
messages2()

# 9번
print("9번")
print('-'*13, '내 예측', '-'*13)
print('B\nA')
print('-'*14, '결과', '-'*14)
def message1():
    print("A")

def message2():
    print("B")
    message1()

message2()

# 10번
print("10번")
print('-'*13, '내 예측', '-'*13)
print('B\nC\nB\nC\nB\nC\nA')
print('-'*14, '결과', '-'*14)
def message1(): # 콜론:이 누락되어 에러 발생하여 수정함.
    print("A")

def message2(): # 콜론:이 누락되어 에러 발생하여 수정함.
    print("B")

def message3(): # 콜론:이 누락되어 에러 발생하여 수정함.
    for i in range (3) :
        message2()
        print("C")
    message1()

message3()

# 11번
print("11번")
def mult():
    a = int(input("숫자1 입력: "))
    b = int(input("숫자2 입력: "))
    return a*b

print(mult())
# 12번
print("12번")
def up():
    while True:
        txt = input("소문자를 입력하세요. : ")
        if txt.islower():
            text = txt.upper()
            break
        else:
            txt = input("소문자를 입력하세요. : ")
            continue

    return text

print(up())
# 13번
print("13번")
def numL(): # 숫자를 리스트로 입력받음.
    k = []
    while True:
        n = input('숫자를 입력하세요(엔터키 누르면 종료). : ') # n은 최초 문자열(str)형으로 입력.
        if n == '': # 엔터 입력시 종료를 실현하기 위해 n의 문자열 자료형 유지.
            print('입력 완료.')
            break
        else:
            k.append(int(n)) # 숫자를 리스트에 추가하기 위함이므로 int()사용하여 n을 실수형으로 변환. 미리 변환할 경우 n==''과 충돌하여 에러.
    return k

def pickup_even(): # 입력받은 리스트 중에서 짝수만 선별하여 반환.
    lst = numL()
    dmy = []
    for i in lst:
        if i % 2 == 0:
            dmy.append(i)
    return dmy

print(pickup_even())
