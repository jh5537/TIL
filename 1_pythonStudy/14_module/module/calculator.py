# calculator module. 계산기 함수: add(x, y), sub(x, y), mul(x, y), div(x, y)
def add(x, y):
    return x+y
def sub(x, y):
    return x-y
def mul(x, y):
    return x*y
def div(x, y):
    return x/y

# __name__ 변수 사용: '__main()__'

if __name__ == '__main__': # 메인으로 사용될 때만 실행되고 모듈로 사용될 때에는 실행되지 않도록 제어.
    print('Here is Calculator module')

