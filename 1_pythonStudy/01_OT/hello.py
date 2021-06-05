# 첫 번째 프로그램

# print('Kim Jihun')
'''(각주 이용)
# 변수에 값을 저장(=할당, assign)
x = 10
y = 20
z = 30
# 또는
x = 10 ; y = 20 ; z = 30

print(x, y, z)
print(x)
print(y)
print(z)

# 여러 개의 변수에 여러 개의 값을 저장
x, y, z = 10, 20, 30

print(x, y, z)
print(x)
print(y)
print(z)

# 여러 개의 변수에 동일한 값을 할당
a = b = c = 100

print(a, b, c)

# 두 변수의 값을 교환(swap)
a, b = 10, 20

print('a=', a)
print('b=', b)

print('[swap]')
"""(원리)
c = a
a = b
b = c
"""
a, b = b, a

print('a=', a)
print('b=', b)

# 변수를 삭제
x = 100

print(x)
print(id(x))
print(type(x))

del x
"""
print(x) -> 사용 시 error 발생
"""

# 문자열에 큰따옴표 사용
name = "이경미"
age = 25
print(name,age) # ',' 사용하여 print 할 경우 띄어쓰기 하나 붙음

address = '서울시 강남구'
print(name + '은 ' + address + "에 삽니다.") # 문자열에 '+' 연산 사용할 경우 띄어쓰기 없이 붙음.
# str( ): 숫자형을 문자열로 형변환
print(name + '은 ' + str(age) + '살입니다.') # 문자열끼리의 합연산에는 숫자를 사용할 수 없기 때문에 숫자를 문자열로 변환해야 함.
print(name + '은', age, '살입니다.') # ','를 이용한 출력은 문자열과 숫자형을 가리지 않음.

# 사각형의 면적을 구하는 프로그램
width = 100
height = 50
area = width * height
print("사각형의 면적은", area)

# 변수 연습문제 1
name = '홍길동'
no = 2016001
year = 4
grade = "A"
average = 93.5
"""(기본형)
print("성명 :", name)
print("학번 :", no)
print("학년 :", year)
print("학점 :", grade)
print("평균 :", average)

# 포맷 코드 사용
print("서식" % 값)
print("문자열 %d 문자열" % 변수) # 정수는 %d, 문자열은 %s, %c 문자 1개, %f 부동소수(실수)
"""
print("성명 : %s" % name)
print("학번 : %d" % no)
print("학년 : %d" % year)
print("학점 : %s" % grade)
print("평균 : %.2f" % average) # .2f는 소수점 앞 2자리만 표현한다는 의미. 10.2f를 사용하면 전체 10자리 확보 후 소수점 2자리까지 표시.

# 소수점 이하 자릿수 설정: format( ) 함수 사용. format(실수, '전체자릿수.소수이하자릿수<서식기호>')
print(format(average, '10.1f'))

# 동시에 표시
print("이름 : %s, 학년 : %d" %(name, year))

# % 기호를 출력하려면 %%를 입력
print("10%") # 정상적으로 표시.

rate = 80
print('이름 : %s, 출석률 : %d%%' %(name, rate)) # %가 사용된 경우에는 '%'를 출력하기 위해 %%입력.

# 포맷 코드 연습문제
kor, eng, math = 90, 80, 80
sum = kor + eng + math
ave = sum / 3

print ("총점: %d, 평균: %.2f" % (sum, ave))

# 상수는 변수와 구분을 위해 대문자를 사용.
PI = 3.141592
r=10
area = r * r * PI
print(area)

INT_RATE = 0.03
deposit = 10000
interest = deposit * INT_RATE
balance = deposit + interest

print(balance)
print(int(balance)) # 정수형으로 변환
print(format(int(balance), ',')) # 천 단위 구분기호 사용

# 리터럴 예제 - 정수 리터럴(Integer Literals)
a = 0b1010 # 2진수(Binary)
b = 300 # 10진수
c = 0o123 # 8진수(Octal)
d = 0x12fc # 16진수(Hexadecimal)

print(a, b, c, d)

# 특수 리터럴(Special Literals). None.
address = None
print(address)
print(type(address))
print(id(address))

# 주석문: 1줄의 경우 #, 여러 줄의 경우 """ """ 등 사용.

# 행 분리: 역 슬래시\ 또는 괄호( ) 사용. 입력 내용이 길어질 경우.
a = 1 + 2 + \
    4 + 5
b = (1 + 2 +
     3 + 5)

# '\n'은 긴 문장에서 행 분리. \\는 백슬래시, \'는 작은따옴표, \"는 큰따옴표, \t는 tab(스페이스 4번)

print(r"C:\info\name") # 첫 번째 따옴표 앞에 r을 추가할 경우 특수문자(\n)의 의미가 없어지고 단순 문자열로 인식.

# print()함수 옆에 출력, 구분자 표시: end" " 안에 넣으면 인식.
print("first", end=" ")
print("second")

# 연습 문제
'''