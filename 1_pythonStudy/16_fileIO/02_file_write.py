# 파일에 쓰기 : 파일을 쓰기 모드(w)로 열고, 파일객체 write() 함수를 이용하여 파일에 출력(기록).

data = 'hello'
f = open('file2.txt', 'w') # 경로 설정을 하지 않으면 현재 파일이 존재하는 폴더에 생성. / f는 파일객체
f.write(data) # 변수 data의 값 'hello'를 file2.txt에 기록
f.close() # 파일 닫음. 파일 저장형태 UTF-8
# 해당 파일의 저장형태 확인하여 ANSI 등 다른 형식인지 확인. 가능하면 UTF-8 형식으로 저장하여 활용. mac에서는 기본적으로 utf-8. ANSI는 미지원(?)
# 다른 형식일 경우 한글이 깨지는 상황이 발생.
""" * 현재 깨지지 않긴 하는데, 강사 화면에서는 깨진다고 함.
data = '안녕하세요'
f = open('file2.txt', 'w')
f.write(data)
f.close()
"""
# 한글 깨짐 수정을 위해 언어코드 지정
data = '안녕하세요'
f = open('file2.txt', 'w', encoding='utf-8')
f.write(data) # 덮어쓰기 형식이기 때문에 위의 'hello'는 삭제됨.
f.close()