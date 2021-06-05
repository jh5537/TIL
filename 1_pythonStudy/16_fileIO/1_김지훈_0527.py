# 1번
print("1번)------------------------------")
with open('yesterdat.txt','r', encoding='utf-8') as f:
    yesT = f.read().lower() # 문자열로 나열, 소문자 변환
yesL = yesT.split() # 단어별로 리스트화
yesS = sorted(set(yesL)) # 알파벳순 정렬, 집합형 변환
# 딕셔너리 사용
# dd = dict()
for w in yesS:
    q = yesL.count(w) # 개별 단어의 수 세서 표현
    # dd[w] = q # 개별 단어와 그 수를 짝지어 입력. - 딕셔너리를 출력하도록 코딩하는 것도 가능.
    print("'%s': %d" % (w, q))

# 2번
print("2번)------------------------------")
with open('dbnum.txt', 'r', encoding='utf-8') as f:
    numT = f.read() # 문자열로 나열
numL = numT.split() # 각 숫자별로 리스트화
resL = [] # 계산결과를 담을 리스트 생성
for i in range(len(numL)):
    if i % 2 == 0: # 숫자 두개씩 묶어서 시행
        a = numL[i]
        b = numL[i+1]
        c = int(a) + int(b) # 첫 번째 숫자, 두 번째 숫자, 합에 변수 할당
        d = "%s + %s = %.1f" % (a, b, c) # 개별 시행의 결과
        resL.append(d) # 전체 결과에 추가
    else:
        continue
data = '\n'.join(resL) # 결과리스트 문자열화
print(data) # 확인
with open('outnum.txt', 'w', encoding='utf-8') as f: # 파일로 내보내기
    f.write(data)

# 3번
print("3번)------------------------------")
# 명단을 입력받아 파일로 저장하는 함수
def input_member(input_fileName):
    while True:
        q = input("멤버를 입력하세요.(종료는 q) : ")
        if q == "q":
            break
        else:
            pq = q+"\n"
            with open(input_fileName, 'a', encoding='utf-8') as f:
                f.write(pq)
    print("저장되었습니다.")

# 입력한 파일을 열어서 출력해주는 함수
def output_member(output_fileName):
    with open(output_fileName, 'r', encoding='utf-8') as f:
        data = f.read()
    print(data)

# 수행
while True:
    say = input("저장 1, 출력 2, 종료 q : ")
    if say == 'q':
        break
    elif say == '1':
        inp = input("멤버 명단을 저장할 파일명을 입력하세요. : ")
        input_member(inp)
    elif say == '2':
        oup = input("멤버 명단이 저장된 파일명을 입력하세요. : ")
        output_member(oup)
print("끝")
