# 함수
'''
# 함수의 정의와 호출
def area_squre(width, hight): # 함수의 이름과 형식 정의- 함수와 변수를 구분하는 기준은 괄호().
    area = width * hight # 수행 문장 지정
    return area # 반환값 지정

w = 10; h = 20
area = area_squre(w, h) # 정의한 함수를 호출하여 사용.
print(area)

def printHello(): # 함수의 정의는 함수의 호출보다 앞에 위치해야 함.
    print('Hello')

printHello()

# 연습문제
def show_info(): # 입력값(매개변수) 없이 이름, 나이, 연락처를 반환하는 함수.
    print("김지훈\n27\n010-5929-9295")

show_info()

# 연습문제: 숫자 입력받아 합을 출력
def sum():
    a = int(input("숫자1 입력 : "))
    b = int(input("숫자2 입력 : "))
    print("합 : %d" % (a+b))

sum()
'''

