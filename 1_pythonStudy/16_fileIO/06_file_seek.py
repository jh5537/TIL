# seek(offset, whence): 파일 내에서 위치로 검색

print('------파일 내에서 검색: seek()------')
f = open('test2.txt', 'r', encoding="utf-8")
f.seek(0,0) # 시작위치는 0행, 0열
lines = f.readlines()
print(lines)

f = open('test2.txt', 'r', encoding="utf-8")
f.seek(1,0) # 시작위치는 0행, 1열
lines = f.readlines()
print(lines)

f = open('test2.txt', 'r', encoding="utf-8")
f.seek(8,0) # 시작위치는 1행, 2열 -> offset에 입력한 값에 해당하는 바이트만큼 넘겨서 검색.
lines = f.readlines()
print(lines)

f = open('test2.txt', 'r', encoding="utf-8")
f.seek(15,0) # 시작위치는 2행, 1열 - 이때, offset에 13,14,16,17,19,20 등은 입력하면 오류가 발생하는데,
# 이는 utf-8에서 한글이 3바이트를 차지하기 때문에 한글이 나오는 부분에서는 3바이트씩 묶여있기 때문. / utf-16에서는 한글을 2바이트로 인식.
lines = f.readlines()
print(lines)
f.close()