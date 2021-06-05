# main Example

name = '' # 전역변수 설정.

def inputName():
    global name # 전역변수를 사용한 함수.
    name = input('이름 입력: ')
    # return은 필요 없음. 전역변수를 직접 변경하기 때문.

def getName():
    if name == '':
        return '무명씨'
    else:
        return name # 함수 내에 설정된 인수가 없으므로 전역변수를 설정하여 사용.

def main():
    inputName()
    print(getName())

if __name__ == '__main__': # 함수의 매커니즘 확인을 위해 모듈 안에서만 실행.
    main()

