# 함수 내에서 사용되는 변수: local variable(지역변수)
'''
def show():
    a = 'Hello' # 함수 내부에 사용된 a는 지역변수. 함수의 정의가 끝나면 초기화.
    print(a)

a = "Hi" # 전역변수
show()
print(a) # 함수에 사용된 변수a는 지역변수이기 때문에 출력되지 않고, 전역변수a가 출력됨.

def show2():
    print(a) # 매개변수(지역변수) 없이 바로 변수에 해당하는 값을 출력하도록 명령하면 전역변수를 활용.

show2() # 이전에 할당한 전역변수a를 출력함.

def show3(): # 함수 내에서 전역변수a를 이용하고자 할 때. - 함수 내부에서 전역변수를 입력, 수정(변경).
    global a # global을 사용하여 함수 내부의 변수a를 전역변수로 활용.
    a = a + 'bye'
    print(a)

show3()
print(a) # 함수에 의해 전역변수가 변경됨.

# 실습문제
def sub(x, y): # 지역변수(a, b, x, y 모두)
    global a # 전역변수a를 사용.
    a = 7 # 전역변수a의 값 변경.
    x, y = y, x # x와 y의 값을 바꿈(swap).
    b = 3
    print(a, b, x, y)

a, b, x, y = 1, 2, 3, 4 # 전역변수
sub(x, y)
print(a, b, x, y) # a는 함수에 의해 전역변수의 값이 수정되었으므로 수정된 값 출력, 나머지는 함수의 지역변수가 영향을 미치지 않으므로 전역변수를 그대로 출력.
'''
def showList(mylist):
    mylist[0] = 100 # 리스트는 전역변수에 해당하는 리스트가 지역변수에서 수정되었을 때, 그 값이 그대로 반영됨.
    print(mylist)

mylist = [1,2,3,4]
showList(mylist) # 지역변수의 리스트가 참조했던 원본 리스트와 동일한 주소를 가지게 됨.
print(mylist) # 결과적으로, 전역변수 리스트의 값도 변화.
# 함수 작성시에는 참조하는 리스트의 값이 변하지 않도록 주의해야 함. copylist를 생성하여 덮어쓰기를 피하는 방식을 활용.

# list를 dictionary로 변환하는 함수.
def getProduct(prdList): # list 입력.
    name = prdList['name']
    price = prdList['price']
    return {'name':name, 'price':price} # dictionary형으로 반환.

productL = [{'name': 'notebook', 'price':12000000, 'maker':'삼성'}, # dictionary를 요소로 하는 list
            {'name': '에어컨', 'price':11000000, 'maker':'LG'},
            {'name': '스마트폰', 'price':51000000, 'maker':'삼성'},
            {'name': '냉장고', 'price':35000000, 'maker':'삼성'},]

for product in productL: # 여러 정보를 가진 리스트에서 필요한 정보만 추출하여 딕셔너리 형태로 반환.
    prdInfo = getProduct(product)
    print(prdInfo)
