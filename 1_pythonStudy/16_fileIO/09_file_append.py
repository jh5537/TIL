# append mode를 사용하여 파일 끝에 내용을 추가.

f = open('test2.txt', 'a', encoding='utf-8')
data = '\n\nPython Programming'
f.write(data) # 변수 data에 해당하는 값을 해당 파일에 추가. - 실행할 때마다 추가됨.
f.close()

print("------파일 전체 읽기------")
f = open('test2.txt','r', encoding='utf-8')
print(f.read())
f.close()