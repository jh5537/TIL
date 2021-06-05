# 팩토리얼 계산 함수 factorial() : n! = n*(n-1)*(n-2)*...*2*1
'''
def factorial(n):
    nf = 1
    for k in range(1, n+1):
        nf *= k
    return nf

# 재귀함수 - 코드가 더 간단해지지만, 메모리를 많이 차지함. 무한루프가 되지 않도록 종료조건에 주의.
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1) # 결과값에 함수를 다시 인용.
""" 위 함수의 연산 처리
f(4) : 4 * f(3) = 4 * 3 * 2 * 1
f(3) : 3 * f(2) = 3 * 2 * 1
f(2) : 2 * f(1) = 2 * 1
f(1) : 1 """

print(factorial(7))

# 내장함수 : https://docs.python.org/ko/3/library/functions.html 참조.
"""
all(): 모두 참이면 True, 하나라도 거짓이면 False. - 0은 거짓, 나머지 정수는 참. ()에는 리스트, 튜플 등.
any(iterable): 하나라도 참이면 Ture, 모두 거짓이면 False.
chr(x): 유니코드값(<=> ascii code value)
ord(c): 해당 문자열의 유니코드를 반환.
eval(expression): 표현식을 평가하여 반환. - 문자열로 된 숫자를 제시하면 실수형으로 변환하여 반환. / 식을 입력하면 연산하여 실수형으로 반환.
help(): 해당 함수에 대한 도움말 출력.
enumerate(iterable, start=0): 시퀀스(리스트, 튜플, 문자열, range)를 인덱스 값을 포함하는 enumerate(열거형) 객체로 반환.
filter(function, iterable): 반복가능한 자료형 요소(시퀀스)에 함수를 적용하여 반환값이 참(True)인 결과만 선별하여 반환.
next(): for문이 수행하는 루프 중 하나의 역할을 수행.(특정 iterable 내 요소의 다음 값을 반환)
map():
int(x, k): x를 정수로 변환(k가 입력되지 않을 경우 10진수). k진수로 변환
list(iterable): iterable을 list로 변환.
sorted(iterable, key=None, reverse=False): iterable 요소들을 정렬한 후 리스트로 반환.
len()
range()
open(filename, [mode]): mode로 파일 열기. mode(읽기 방법) 생략 시 읽기전용 모드(r)가 기본.
zip(*iterable): 각각의 iterable에서 동일한 인덱스 요소를 추출해 결합하여 반환.

- 계산과 관련된 내장 함수
abs(x): x의 절댓값 반환.
min(iterable): 항목 또는 인자 중 최솟값 반환.
max(iterable): 항목 또는 인자 중 최댓값 반환.
pow(base, exp): x**y. base의 exp거듭제곱을 반환.
divmod(a, b): a를 b로 나눈 것의 몫과 나머지를 튜플 형태로 반환(몫//, 나머지%).
sum(iterable): 주어진 값들의 합을 반환. max,min과 달리 인자만을 넣을 수는 없음.
round(x, k): 실수 x를 소숫점 이하 k자리까지 반올림. k를 비우면 정수로 표현.

"""
# enumerate(): 시퀀스(리스트, 튜플, 문자열, range)를 인덱스 값을 포함하는 enumerate(열거형) 객체로 반환.
enum = enumerate(['apple', 'banana', 'melon', 'strawberry', 'kiwi', 'watermelon'])
print(enum) # enumerate만 하고 나서는 값을 출력할 수 없음.

for i, item in enum: # for문 등으로 짝을 출력하여 표현.
    print(i, item) # enumerate 객체 주소는 next()(또는 for)나 iter() 등을 통해 구성요소를 참조할 때마다 삭제되는 1회용 주소.

seasons = ['spring', 'summer', 'fall', 'winter']
enumSeason = list(enumerate(seasons, 1)) # 또는 리스트로 변경하여 표현 가능. - 리스트 내에 인덱스와 시퀀스는 튜플로 묶여 있음.
print(enumSeason) # enumerate 주소는 1회용이므로, 이전에 for문 등으로 이미 참조한 경우, 빈 리스트가 출력됨.

# filter(function, iterable): 반복가능한 자료형 요소(시퀀스)에 함수를 적용하여 반환값이 참(True)인 결과만 선별하여 반환.
def positive(x): # x가 양수일 경우에 참, 이외엔 거짓을 반환하는 함수.
    return x > 0

num = [-10, 1, 3, 5, -3, 0, -4]
result = filter(positive, num)
print(type(result)) # filter 자료형이기 때문에 값을 제대로 확인하기 위해서는 리스트형으로 변환이 필요함.
print(list(result)) # 함수의 값이 참인 결과(=양수)만을 반환.

# 실습문제: 짝수인지를 판별하는 함수 even(x)를 정의하고, filter를 이용하여 주어진 리스트의 짝수만 걸러내는 코드 작성.
def even(x):
    return x % 2 == 0

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filter(even, lst)
print(list(result))

# sorted(iterable, key=None, reverse=False): iterable 요소들을 정렬한 후 리스트로 반환.
a = [10, -4, 5]

print(sorted(a))
print(sorted(a, reverse=True)) # 역순으로 정렬.
print(sorted("flower")) # 문자열의 각 문자를 알파벳 순으로 정렬.
print(sorted("SunFlower", key=str.lower)) # 소문자 우선으로 정렬.

# zip(*iterable): 각각의 iterable에서 동일한 인덱스 요소를 추출해 결합하여 반환.
q = zip([1,3,5],['cat','dog','horse'])
print(q)
print(list(q)) # 리스트 형태로 출력해야 보기 편함. 튜플로도 가능.
print(zip([1,3,5],['cat','dog','horse', 'lion'])) # 동일한 인덱스 요소가 있는 경우만 반환하기 때문에, 길이 차이가 나는 부분은 생략됨.
print(dict(zip([1,3,5],['cat','dog','horse']))) # 딕셔너리 형태로도 출력 가능.

# map(함수, iterable): 리스트나 튜플, 문자열 등(iterable object)을 지정된 함수로 처리해주는 함수. 원본은 변경하지 않고 새 리스트나 튜플을 생성.
# list(map(함수, 리스트)), tuple(map(함수, 튜플))

# 재귀함수 - 자연수를 입력받으면 해당하는 자연수까지 출력.
def count(num):
    if num == 0: # num이 0인지 확인하는 이유- 재귀함수를 끝내는 조건으로 사용.
        print()
        return
    else:
        print(num, end=' ')
        return count(num-1)

count(24)

# 내부함수: 함수 안에 정의된 함수. 함수 내부에서만 호출할 수 있기 때문에 외부에서는 호출할 수 없음.
def outFunc(x, y):
    def inFunc(a, b):
        return a + b
    return inFunc(x, y)

print(outFunc(10,20)) # print(inFunc(10,20))은 사용할 수 없음. 내부함수는 호출할 수 없음.

# lambda 식- (lambda 매개변수: 식)(인수) 또는 객체명=lambda 매개변수 식 ; 객체명(인수)
def hap(x, y): # 함수가 간결할 경우 람다식 이용 가능.
    return x+y

print(hap(10, 50))

hap2 = (lambda x, y: x + y)(10, 50) # 함수 이름을 정의한 것도 아니지만 함수와 유사한 용도로 사용 가능. 콜론: 이후가 계산하고자 하는 식.
print(hap2)

# 람다표현에서 디폴트 설정
lam = lambda x=10, y=20: x + y # 함수 정의할 때와 마찬가지로 디폴트 설정 가능.
print(lam) # 설정한 람다를 불러와서 계산 가능.
print(lam(10,9))
# 단, 람다식에서는 새로운 변수(지역변수)를 생성할 수는 없음. 인수로 지정된 변수들만 활용 가능. 단, (함수 외부의) 전역변수는 사용 가능.
'''
# 람다함수에서 리스트 이용
lst = [1, 3, 4]
def addTen(x):
    return x + 10

print(list(map(addTen,lst))) # 단일인수를 입력받는 함수를 map을 활용하여 리스트에 적용.

print(list(map(lambda x:x+10, lst))) # 람다에 리스트를 적용하기 위해 map을 활용.

# 람다함수 이용실습: 두 개의 리스트의 같은 요소의 값들을 더해서 하나의 리스트로 반환.
list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]

# def 함수 정의
def addList(x, y):
    return x + y

resultFunc = list(map(addList,list1,list2))
print(resultFunc)

# lambda 표현식 정의
adding = lambda x, y: x + y

resultLamb = list(map(adding,list1,list2))
print(resultLamb)

# 재귀함수의 무한루프 탈출
