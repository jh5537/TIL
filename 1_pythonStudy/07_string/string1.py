# 문자열의 기본 형식과 이해
'''
crawling = "Data crawling is fun"
parsing = "Data parsing is also fun"

print(crawling)
print(parsing)

print(type(crawling))
print(type(parsing)) # <class 'str'> - 해당 값의 type은 문자열.

# 문자열과 문자열 연결은 + 연산자를 사용

# 문자열과 숫자를 연결하려면 숫자를 문자열로 형변환하여(str()) + 연산자로 연결
PI = 3.1415
r = 10
result = "반지름 " + str(r) + "인 원의 넓이는 " + str(PI*r*r)
print(result)

# 문자열에 곱연산 *을 사용하면 반복하여 표시.

# 문자열 인덱싱(indexing): 인덱스로 문자의 위치를 나타내는 것. - 인덱스(첨자)는 문자의 위치로, 0부터 시작.

# slicing: 문자열의 일부분을 추출.
# string[0]: 인덱스 0번 문자(첫 번째 문자) 추출 / string[-1]: 인덱스 마지막 문자(뒤부터 셈) 추출 - 대괄호로 표현, 시작은 0. 공백도 문자로 포함.
"""문자열의 범위 설정 개념
| p | y | t | h | o | n |
0 - 1 - 2 - 3 - 4 - 5 - 6 -> 해당 숫자를 기준으로 범위 설정하여 그 안의 문자를 반환.
"""
print(crawling[0]) # 첫 번째 문자 - 인덱스 n번째 문자
print(crawling[-1]) # 마지막 문자
print(crawling[1:6]) # 두 번째 문자(1)부터 6번째 문자까지 - k부터 n-1번째까지의 문자열
print(crawling[:-1]) # 처음부터 마지막 문자(-1)의 전까지 - 0부터 n까지
print(crawling[-1:]) # 마지막 문자(부터 끝까지) - n부터 끝까지
print(crawling[:]) # 문자열 전체
print(crawling[0:10]) # 첫 번째 문자부터 10 번째 문자까지

# in : 문자열 존재 여부 확인. / not in은 없으면 True
string = 'Python programing'
print('python' in string) # in은 주어진 문자열에 해당 문자열이 존재하는지 확인하여 반환. True, False의 값을 가짐.

# 활용
if 'python' in string:
    print('있습니다.')
else:
    print('없습니다.')

names = ["홍길동", "변학도", "성춘향", "이몽룡"]
name = input('input name: ')
if name in names:
    print('있다.')
else:
    print('없다.')

# https://docs.python.org/3/ 참고하여 세부 기능 확인.

# string 관련 함수들
# len(): 문자열의 length
string = 'Python Programming'
n = len(string)
print(n)

# count(): 찾고자 하는 문자(열)의 개수
print(string.count('ing'))

# find(): 특정 문자열이 존재하면 그 위치를 반환, 존재하지 않으면 -1 반환. 필요한 문자열만 추출할 수 있도록 필터링하거나 검사할 때 주로 사용.
print(string.find('ing'))
print(string.find('ong'))

crawling = "Data crawling is fun"
print(crawling.find("f"))
print(crawling.rfind("f")) # 뒤(오른쪽)부터 해당 문자를 찾음.
print(crawling.find("f", 1, 9)) # 1(두 번째 문자)부터 9(아홉 번째 문자)까지 범위 내에서 해당 문자를 찾음.

# index(): 특정 문자열의 위치를 반환. 존재하지 않으면 오류.
print(string.index('ing'))
# print(string.index('ong')) 존재하지 않아 오류 발생.

print(crawling.index("f"))
print(crawling.rindex("f")) # 뒤(오른쪽)부터 해당 문자를 찾음.
# print(crawling.index("f", 1, 9)) # 1(두 번째 문자)부터 9(아홉 번째 문자)까지 범위 내에서 해당 문자를 찾음. 존재하지 않으면 오류 발생.
'''
# 연습문제 - 이메일 주소를 입력받아서, 이메일 형식이 아니면 "이메일 형식이 아닙니다." 출력
email = input("이메일 입력 : ")

if(email.find("@") == -1 or # @ 없는 경우
   email.find(".") == -1 or # . 없는 경우
   email.index("@") > email.index(".") or # @과 . 위치가 바뀐 경우 - @의 위치값이 .의 위치값보다 크면 @가 더 뒤에 있으므로 이메일 형식이 아님.
   email.index(".") - email.index("@") < 2 or # @과 . 사이에 문자가 없는 경우 - .의 위치값에서 @의 위치값을 뺐을 때 차가 1이면 붙어있는 것.
   email.index("@") == 0 or # @ 앞에 문자가 없는 경우 = @이 첫 번째 문자일 경우
   len(email) - email.index(".") <= 1 or # . 뒤에 문자가 없는 경우 - 입력값의 길이와 .의 위치값 차이가 1이라면 . 뒤에는 문자가 없음.
   email.count("@") >= 2 or # @ 두 번 이상 있는 경우
   email.count(".") >= 2): # . 두 번 이상 있는 경우

    print("이메일 형식이 아닙니다.") # 위 조건 중 하나라도 해당하면 이메일 형식이 아님.(or)

print("입력한 이메일 : ", email)