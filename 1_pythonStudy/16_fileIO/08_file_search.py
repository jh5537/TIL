# read()함수 이용하여 원하는 내용이 파일에 있는지 검색

value = input('검색 값 입력: ')
f = open('test2.txt', 'r', encoding='utf-8')
data = f.read() # 데이터 차제가 문자열.
if value in data: # if 를 통해 문자열 안에 찾고자 하는 데이터가 있는지 확인 가능.
    print("있음",value)
else:
    print("없음")

f.close()


