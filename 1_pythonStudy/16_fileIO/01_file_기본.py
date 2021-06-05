''''''
f = open("file1.txt", "w") # 쓰기모드로 파일 열기. - 기존 파일 없으면 새로 생성. 생성된 file1.txt 파일은 비어있는 파일.
f.close() # 데이터를 추가하지 않고 종료.

# 경로 수정 - 파일의 절대경로
f = open("/Users/kimjihun/Documents/pythonStudy/file1.txt", "w")
f.close()
# 디렉토리 경로 설정 시 \ 사용하면 오류 발생. => \\ 또는 / 사용하여 해결.

# 상대경로 표현
f = open("../file2.txt","w") # 현재 파일이 속한 폴더에서 하나 상위의 폴더를 경로로 설정.
# /Users/kimjihun/Documents/pythonStudy/file2.txt 에 생성.
