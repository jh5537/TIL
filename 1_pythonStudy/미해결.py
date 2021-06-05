# *args : arguments 를 1개 이상 지정
def mySum(*args): # args를 사용해 여러개의 인수를 등록할 수 있음.
    total = 0
    for x in args:
        total += x
    return total

print(mySum(1, 3, 5))
print(mySum(3, 4))
print(mySum(1,2,3,4,5,6,7))

# ?
def calculator(operator, *args):
    pass

# *kwargs : keyword argument key=value
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

# 재귀함수의 무한루프 탈출

