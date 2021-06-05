# 파일에 쓰기 w; write()
''''''
# 여러 줄 단위로 data를 저장.
f = open('file3.txt','w',encoding='utf-8')

for i in range(1, 11):
    data = '%d행' % i
    f.write(data)

f.close() # 파일 내용: 1행2행3행4행5행6행7행8행9행10행 => 줄이 띄워지지 않음.

# 줄을 띄워서 저장(한 줄 단위로 출력).
f = open('file3.txt','w',encoding='utf-8')

for i in range(1, 11):
    data = '%d행\n' % i
    f.write(data)

f.close()

# ','를 포함하여 출력
f = open('file4.txt','w',encoding='utf-8')

for i in range(1, 11):
    data = '%d행,' % i
    f.write(data)

f.close()
# 파일 내용: 1행,2행,3행,4행,5행,6행,7행,8행,9행,10행, => 쉼표, 사용할 경우 csv파일 형태로 저장하기 용이.
"""
# ','를 이용하여 csv 파일 생성: 데이터 저장 형식으로 자주 사용됨. 메모장, 엑셀 등 여러 프로그램에서 열 수 있음. 파이참은 지원 x.
f = open('file4.csv','w',encoding='utf-8')

for i in range(1, 11):
    data = '%d행,' % i
    f.write(data)

f.close()
"""
# 정교화된 csv 파일 생성
f = open('file4.csv','w',encoding='utf-8')

for i in range(1, 11):
    if i == 10:
        data = '%d행' % i
    else:
        data = '%d행,' % i
    f.write(data)

f.close()
# csv는 덮어쓰기 안 되나? 위 코드 주석처리 안하면 ','포함된 파일 생성된 채로 바뀌지 않음.