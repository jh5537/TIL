# 함수의 반환값(return)
'''
def sum():
    a = int(input("숫자1 입력 : "))
    b = int(input("숫자2 입력 : "))
    # print(a+b)
    return a+b # 반환값이 없으면 변수=sum() 식으로 실행했을 때, 변수가 값을 가지지 못함.

res = sum()
print(res)
# print(sum())을 사용하여 변수(res)를 거치지 않고 바로 결과를 출력할 수 있음.

# 연습문제 - 삼각형의 넓이 계산 함수
"""
def get_triangle_area():
    h = int(input('높이 : '))
    w = int(input('밑변 : '))
    area = h * w / 2
    return area

print("삼각형의 면적 : ", get_triangle_area())
"""
def get_triangle_area():
    h = int(input('높이 : '))
    w = int(input('밑변 : '))
    area = h * w / 2
    return h, w, area # 여러 값을 반환값으로 정할 경우 쉼표, 등으로 구분. return을 여러번 사용하면 처음의 return만 인식됨.
# return 명령어 이후에 함수 정의 코드가 끝나기 때문에 이후의 return은 인식되지 않음.

area = get_triangle_area()
print(area) # (w, h, area): 쉼표,를 기준으로 다수의 반환값을 지정하면 튜플 형식으로 반환.
print("높이 %d, 밑변 %d, 삼각형의 넓이 %.1f" % area)

# 연습문제
def order():
    p = int(input("상품가격 입력 : "))
    q = int(input("주문수량 입력 : "))
    return p, q, (p * q)
get = order()
print("------------------------------")
print("상품가격 : %d원\n주문수량 : %d개\n주문액 : %d원" % get)

# 반환값 자료형의 변경 - 리스트
def getNames():
    names = []
    for i in range(3):
        name = input('이름 입력 : ')
        names.append(name)
    return names

nameL = getNames()
print(type(nameL))
print(nameL)

# 이름과 나이를 입력받아 딕셔너리 형식으로 반환
def getNA():
    na = {}
    nam = input('이름을 입력: ')
    age = int(input('나이를 입력: '))
    na['name'] = nam # na = {'name':nam, 'age':age}의 형식으로 직접 딕셔너리 작성해도 됨.
    na['age'] = age
    return na
NA = getNA()
print(NA)

for key, value in NA.items(): # 딕셔너리의 내부 항목을 분리하여 출력- .items() 메소드 활용
    print(key, ':', value)

for key in NA.keys(): # 딕셔너리의 내부 항목을 분리하여 출력- .keys() 메소드 활용
    print(key,':',NA[key])

# 함수의 반환값이 없는 경우 None 출력
def showHello():
    print("Hello")

result = showHello()
print(result) # None 출력. 반환값 없음.

# 함수의 매개변수(parameter): 함수를 정의할 때 전달(입력)되는 형식의 값.
# 인수(argument): 함수에 실제로 전달(입력)되는 값.
def showInfo(name, age): # 이때의 name과 age는 매개변수(parameter)
    print('이름은 %s이고, 나이는 %d세입니다.' % (name, age))

showInfo('홍길동', 18) # 이때의 '홍길동'과 18은 인수(argument)

def getArea(width, height):
    return width * height/2

width = int(input("밑변: "))
height = int(input("높이: "))
a = getArea(width, height) # 표기는 똑같은 width, height이지만, 함수정의 단계의 매개변수와 실제 호출시의 인수는 다른 변수로 취급.
print(a)

# 사칙연산을 수행하는 함수들을 정의하여 호출: add(x, y), sub(x, y), mul(x, y), div(x, y)
# 2개의 숫자를 키보드로 입력받고, 각 함수에 전달하여 계산 결과를 출력하는 코드.
def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def mul(x, y):
    return x * y
def div(x, y):
    return x / y
a = int(input("숫자1 입력: "))
b = int(input("숫자2 입력: "))
print("%d + %d = %d" % (a, b, add(a,b)))
print("%d - %d = %d" % (a, b, sub(a,b)))
print("%d * %d = %d" % (a, b, mul(a,b)))
print("%d / %d = %.2f" % (a, b, div(a,b)))

# 연습문제2: 상품 가격과 주문 수량을 전달받아서, 주문액, 할인액, 지불액을 계산하여 반환.
def order(price, qty):
    amount = price * qty
    if amount >= 100000:
        discount = amount * 0.1
    elif amount >= 50000:
        discount = amount * 0.05
    else:
        discount = 0
    total = amount - discount
    amount = format(amount, ",") # format을 사용하여 자릿수 입력. -> 문자열로 자료형 변환됨.
    discount = format(discount, ",")
    total = format(total, ",")
    return amount, discount, total
p = int(input("상품 가격 입력 : "))
q = int(input("주문 수량 입력 : "))
od = order(p,q)
print('-'*30)
print('주문액 : %s원\n할인액 : %s원\n지불액 : %s원' % (od[0].rjust(10),od[1].rjust(10),od[2].rjust(10))) # 오른쪽 정렬(rjust)

# 딕셔너리를 활용하여 문제 계산.
def order(price, qty):
    amount = price * qty
    if amount >= 100000:
        discount = amount * 0.1
    elif amount >= 50000:
        discount = amount * 0.05
    else:
        discount = 0
    total = amount - discount
    info = {'상품 가격':price, '주문 수량':qty, '주문액':amount, '할인액':discount, '지불액':total}
    return info
p = int(input("상품 가격 입력 : "))
q = int(input("주문 수량 입력 : "))
od = order(p,q)
print('-'*30)
for key in od.keys():
    print(key, ':', od[key])

# 함수의 매개변수 형식 - 매개변수에 기본값 지정: default parameter
def showMessage(message='Hi!'):
    print(message)

def showMessage2(name, message='Hello!'): # 두번째 매개변수 message의 기본값이 'Hello!'로 지정됨.
    print(name + message)

# def showMessage3(message='Hello!', name): # 첫번째 매개변수에 기본값을 설정할 수는 없음. 기본값을 설정하려는 매개변수는 가장 뒤에 설정.

showMessage('Hello')
showMessage2('Kim', 'Hi')
showMessage2('Kim') # 두번째 인수를 입력하지 않으면 기본값인 'Hello!'가 반환.
showMessage() # 매개변수 하나짜리는 인수를 입력하지 않으면 기본값 반환.

# 매개변수가 세개일 때 디폴트값에 따른 함수의 인수 설정 경우의 수.
def showInfo(name, age=10, sex='F'):
    print(name, age, sex)

showInfo('홍길동')
showInfo('강감찬', 40)
showInfo('변학도', 40, 'M')

# 리스트를 실인수로 갖는 함수.
def showNames(names):
    for name in names:
        print(name)

names = ['Hong', 'Park', 'Choi', 'Lee']
showNames(names)
# showNames(['Hong', 'Park', 'Choi', 'Lee'])로도 사용 가능.

# 딕셔너리를 실인수로 갖는 함수.
def showInfoStd(student):
    print(student)
    print('이름 : ', student['name'])
    print('나이 : ', student['age'])
    print('연락처 : ', student.get('phone'))

info_std = {'name' : 'Kim', 'age' : 19, 'phone': '010-1234-5849'}
showInfoStd(info_std)
'''
# *args : arguments 를 1개 이상 지정
# *kwargs : keyword argument key=value

def mySum(*args): # args를 사용해 여러개의 인수를 등록할 수 있음.
    total = 0
    for x in args:
        total += x
    return total

print(mySum(1, 3, 5))
print(mySum(3, 4))
print(mySum(1,2,3,4,5,6,7))

def myShowInno(**kwargs): # 매개변수에 키워드와 값을 사용할 수 있음.
    for key in kwargs.keys():
        print(key, end=' ')
    print()
    for value in kwargs.values():
        print(value, end=' ')
    print()
    for item in kwargs. items():
        print(item)

myShowInno(id = 123, name='Kim', add='Seoul')
myShowInno(id = 123, name='Kim')
myShowInno(id = 123, name='Kim', add='Seoul', phone='010-1234-1234')

def calculator(operator, *args): # ?
    pass

def studentInfo(name, age, sex):
    student = {'name' : name, 'age':age, 'sex':sex}
    return student

print(studentInfo('Lee', 30, 'F')) # 위치인수: 위치를 기반으로 하는 인수.
print(studentInfo(name = 'Kim', age = 30, sex = 'M')) # 키워드 기반 인수: 순서가 바뀌어도 해당 인수가 할당되는 곳에 들어감.
print(studentInfo(name = 'Moon', sex = 'F', age = 22))
print(studentInfo('Hong', sex='M', age=15)) # 위치인수와 키워드인수를 혼용할 때는 키워드인수는 위치인수 뒤에 입력.
# print(studentInfo(name = 'Hong', 15, 'F'))는 오류.

