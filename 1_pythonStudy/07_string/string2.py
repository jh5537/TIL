# 문자열을 찾는 함수 : count(), find(), rfind(), index(), rindex(), startswith(), endswith()
# rfind와 rindex는 오른쪽(뒤)부터 find와 index를 실행.
'''
crawling = "Data crawling is fun"

# split(): 문자열 분리. 분리의 기준이 되었던 공백(이나 , 등)은 사라짐.
token = crawling.split() # 공백을 기준으로 문장을 분리하여 리스트로 표현.
print(token) # ['Data', 'crawling', 'is', 'fun']

names = 'Lee,Kim,Choi,Kang'
print(names.split()) # 해당 문자열에 공백이 없어서 분리되지 않아 하나의 문자열 그대로 출력. ['Lee,Kim,Choi,Kang']
print(names.split(',')) # ','를 기준으로 분리. ['Lee', 'Kim', 'Choi', 'Kang']

nameList = names.split(',') # 분리과정을 파싱, 토크나이징 등으로 부름.
for n in nameList:
    print(n)

for i in range(len(nameList)): # len()을 이용해 리스트의 항목 수만큼 for에 입력하여 해당 값을 출력.
    print(nameList[i])

# 문자열의 요소 하나씩 출력하고자 할 때
for c in crawling:
    print(c)

# 연습문제 - 생일 입력(연/월/일)
"""
bd = input("생일 입력(연/월/일): ")
Birthday = bd.split('/')
year = Birthday[0]
month = Birthday[1]
day = Birthday[2]
print("당신은 %s년에 태어나셨군요" % year)
print("생일은 %s월 %s일이네요" % (month,day))
"""
# 모범답안
birthday = input('생일 입력(연/월/일) : ')
birth_split = birthday.split('/')
print("당신은 %s년에 태어나셨군요" % birth_split[0] + '\n' + "생일은 %s월 %s일이네요" % (birth_split[1], birth_split[2]))

# 주어진 데이터에서 점수만 추출하여 숫자화하고 총점과 평균을 구하시오.
data = "{a1:30},{a2:50},{a3:20},{a4:70},{a5:40}"
"""
score = data.split(',')
sum = 0
for i in range(5):
    s = score[i][4:6] # 단, 이 경우 개별 데이터가 불규칙하게 기입되어 있을 경우 정확한 결과를 도출하지 못함.
    print(s)
    sum += int(s)
print(sum)
avg = sum / len(score)
print(avg)
"""
# 모범답안
split_data = data.split(',')
score = n = total = 0
for d in split_data:
    item = d.split(':') # {a1:30} -> ['{a1', '30}']
    item2 = item[1].split('}') # 30} -> ['30']
    score = int(item2[0]) # 윗줄과 이 줄을 합쳐서 score = int(item[1].split('}')[0])으로도 표현 가능.
    print(score)
    total += score
    n += 1
print('총점 : %d, 평균 : %f' % (total, total/n))

# join(): 문자열의 결합(삽입)
a = 'aa'
print(a.join('bbb')) # b의 각 사이에 aa가 삽입됨 'baabaab'

b = '-'
print(b.join('1234')) # 1-2-3-4

numbers = ['10', '20', '30', '40', '50']
sep = ','
result = sep.join(numbers)
print(result) # split을 역으로 행한 결과가 나옴.

date = ['1990', '01', '01']
sep = '-'
print(sep.join(date))

# replace(): 지정한 문자열을 다른 문자열로 대체.
text = 'Java Programming'
text2 = text.replace('Java', 'Python')
print(text2)

# 대문자/소문자 변환: upper(), lower(), capitalize(), title(), swapcase()
text = 'java programming is Fun'
print(text.upper()) # 모든 문자를 대문자로.
print(text.lower()) # 모든 문자를 소문자로.
print(text.capitalize()) # 전체 문장에서 가장 첫 문자 하나만 대문자로.
print(text.title()) # 각 단어의 첫 문자를 대문자로.
print(text.swapcase()) # 대문자는 소문자로, 소문자는 대문자로.

# 공백문자 제거: strip(), lstrip(), rstrip()
text = '   java programming is Fun   '
print(text.strip()) # 모든 공백 제거 'java programming is Fun'
print(text.lstrip()) # 왼편 공백만 제거 'java programming is Fun   '
print(text.rstrip()) # 오른편 공백만 제거 '   java programming is Fun'

# 문자열의 구성요소 판단
""" 판별 대상은 문자열도 가능하고, 하나의 문자도 가능.
isalpha() : 문자여부를 판단하여 True, False 반환.
isdigit() : 숫자인지
isspace() : 공백인지
isalnum() : 영문과 숫자인지
isupper() : 대문자 판단
islower() : 소문자 판단 """
text = '123457num'
print(text.isdigit())
print(text.isalpha())
print('    '.isspace())
print(text.isalnum())
print('Abc'.islower())
print('AAA'.isupper())

# 연습문제 - 문장을 입력하여 문자, 숫자, 공백, 그외 문자의 개수를 계산하여 출력 - '나의 email 주소는 imlkm70@daum.net 입니다'
text = input("문장을 입력하세요 : ")
alp = num = spc = etc = 0
for a in range(len(text)):
    if text[a].isalpha():
        alp += 1
    elif text[a].isdigit():
        num += 1
    elif text[a].isspace():
        spc += 1
    else:
        etc += 1
print('해당 문장의 문자는 %d개, 숫자는 %d개, 공백은 %d개, 그 외는 %d개 입니다.' % (alp, num, spc, etc))

# formatting : %d 정수, %f 실수, %s 문자열, %c 문자 1개
# %3d-세 자리 정수. %5.2f-다섯 자리 실수의 소숫점 두번째 자리까지.
alp = 20; num = 30
height = 179.33
string = 'python'
print('문자 : %d개' % alp)
print('문자 : ', format(alp, 'd'), '개')
print('문자 : {0}개, 숫자 : {1}개'.format(alp,num))
print('문자 : {a}개, 숫자 : {n}개'.format(a=alp, n=num))
print('키는 {0:5.1f}'.format(height)) # format의 {} 안에 :를 활용하여 자릿수 지정하거나 정렬이 가능.
print('{0:<10}'.format(string)) # (10칸을 기준으로) 왼쪽 정렬
print('{0:>10}'.format(string)) # 오른쪽 정렬
print('{0:^10}'.format(string)) # 가운데 정렬
print('{0:-^10}'.format(string)) # -를 사용하여 가운데 정렬
print(string.ljust(10)) # (10칸을 기준으로) 왼쪽 정렬
print(string.rjust(10)) # 오른쪽 정렬
print(string.center(10)) # 가운데 정렬
'''
# 날짜, 시간 출력 포맷
from datetime import date, datetime, timedelta

today = date.today() # 연, 월, 일
print(today)
print(today.year)
print(today.month)
print(today.day)

cur_time = datetime.now() # 연, 월, 일, 시, 분, 초
print(cur_time)
time = datetime.now().time() # 시, 분, 초
print(time)
print(time.hour)
print(time.minute)
print(time.second)
print(time.microsecond)

print(today + timedelta(days=-1)) # 하루 전 날짜를 계산
print(today + timedelta(days=8)) # 8일 후의 날짜를 계산
print(cur_time + timedelta(days=1, hours=2)) # 하루 뒤, 두 시간 뒤의 시점을 계산

print(cur_time.strftime('%Y-%m-%d-%H:%M:%S')) # 각 출력 단위 표시를 지정할 수 있음.

