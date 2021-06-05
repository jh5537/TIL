# read(): 파일전체를 읽어서 문자열 반환

f = open('test2.txt', 'r', encoding='utf-8')
data = f.read()
print(data) # 파일 전체의 내용을 문자열로 반환.
print(type(data)) # 자료형: 문자열
print(len(data)) # 문자열의 길이 확인

for ch in data:
    print(ch)

f.close()