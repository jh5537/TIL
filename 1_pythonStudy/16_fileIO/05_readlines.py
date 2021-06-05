# readlines()를 이용해 파일 읽기 - 모든 행을 읽어 라인 단위의 리스트를 생성
''''''
# 파일 전체 읽기
f = open('test.txt', 'r', encoding='utf-8')
lines = f.readlines()
print(lines)
f.close()
""" 리스트 형태로 출력. 행 뒤에 \n이 있음.
['안녕하세요. 홍길동입니다.\n', '지금 파이썬을 공부하는 중이에요.\n', '\n', '0. print\n', '1. 변수\n', 
'2. 연산자\n', '3. 자료형\n', '4. 조건문\n', '5. 반복문\n', '6. 문자열\n', '7. 리스트\n', '8. 튜플\n', 
'9. 딕셔너리\n', '10. 세트\n', '11. 함수\n', '12. 모듈\n', '13. 패키지']
"""

# readlines()는 readline()으로 파일 전체를 읽고, 그 내용을 리스트에 저장한 것과 같음.
print("------readline으로 리스트에 저장------")
f = open('test.txt','r', encoding='utf-8')
myL = []
while True:
    line = f.readline()
    if line == '':
        break
    myL.append(line)

f.close()
print(myL) # print(f.readlines())와 같은 결과.

# readlines()로 읽은 내용을 한 줄씩 출력하기.
print("------readlins를 한 줄씩 출력------")
f = open('test.txt','r', encoding='utf-8')
myL = f.readlines()
for i in range(len(myL)):
    print(myL[i], end='')

f.close()

