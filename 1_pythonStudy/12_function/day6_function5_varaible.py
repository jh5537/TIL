# 함수내에 사용되는 변수 : local variable(지역변수)

def show():
    a = 'Hello'  #지역변수
    print(a)

def show1(a):
    a = a + 'Hello'
    print(a)

# 전역변수를 함수 내부에서 사용
def show2():
    print(a)

# 전역변수를 함수 내부에서 수정(변경)
def show3():    # 전역변수 a를 변경하고 싶다
    global a
    a = a + 'H'
    print(a)

# a ='Hi'   # 전역변수
#show()
# show1('Haha')
#show2()
# show3()


# 실습문제 : 결과는?
def sub(x, y):
    global a
    a = 7
    x, y = y, x   # swap
    b = 3
    print(a, b, x, y)
    print(id(a))
    print(id(x))

# a, b, x, y = 1, 2, 3, 4
# print('전역변수')
# print(id(a))
# print(id(x))
# sub(x, y)
# print(a, b, x, y)

def showList(mylist):
    mylist[0]=100
    print(mylist)
    print('in function ID :', id(mylist))

# mylist = [1,2,3,4]
# showList(mylist)
# print(mylist)
# print('out function ID :', id(mylist))

# 딕셔너리list를 dictionary로 변환

def getProduct(prdList):
    name = prdList['name']
    price = prdList['price']
    return {'name' : name, 'price': price}

productL = [ {'name': 'notebook', 'price': 12000000, 'Maker':'삼성'},
             {'name': 'smartPhone', 'price': 12000000, 'Maker':'삼성'},
             {'name': '냉장고', 'price': 51000000, 'Maker':'LG'},
             {'name': '에어콘', 'price': 35000000, 'Maker':'삼성'}]

for product in productL:
    prdInfo = getProduct(product)
    print(prdInfo)