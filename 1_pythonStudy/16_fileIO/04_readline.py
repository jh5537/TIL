""" 파일 읽어오기
readline() : 1개의 행씩 읽어오기, 행 끝에 '\n' 포함.
readlines() : 모든 행을 읽어 라인 단위로 잘라서 리스트를 생성. ['...\n', '...\n', '...\n', ... '...\n']
read(): 내용 전체를 한 문자열로 반환 ''' ... '''
"""
'''
# readline() 이용.
print('------첫번째 행 읽어오기------')
f = open('test.txt','r') # 윈도우에서: ANSI는 잘 읽어오는데, utf-8은 깨짐. => 인코딩 필요.
line = f.readline() # () 미입력시 첫째 줄 읽음.
print(line)
f.close()

# utf-8 형식으로 저장된 파일 읽기(인코딩). mac에서는 굳이 지정하지 않아도 잘 읽어옴.
f = open('test.txt','r', encoding='utf-8')
line = f.readline()
print(line)
f.close()

# 여러 줄 읽어오기
f = open('test.txt','r', encoding='utf-8')
line = f.readline()
print(line) # readline()에는 '\n'이 기본적으로 포함되어 있어서 이대로 출력하면 빈 행이 생김.
line = f.readline() # 지정하지 않았지만 자동으로 다음 줄을 읽음.
print(line)
f.close()
"""
안녕하세요. 홍길동입니다.

지금 파이썬을 공부하는 중이에요.
"""

# 수정
f = open('test.txt','r', encoding='utf-8')
line = f.readline()
print(line, end='')
line = f.readline()
print(line, end='') # end=''를 활용하여 빈 행이 출력되지 않도록 함.
f.close()
"""
안녕하세요. 홍길동입니다.
지금 파이썬을 공부하는 중이에요.
"""
'''
# 파일 전체 읽기
print("------파일 전체 읽기------")
f = open('test.txt','r', encoding='utf-8')
while True:
    line = f.readline()
    print(line, end='')
    if line == '':
        break
f.close()
