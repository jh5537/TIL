# 예외 발생 상황
"""
print(10/0) => ZeroDivisionError: division by zero(0으로 나눴을 때)

print('age=' + 23) =>TypeError: can only concatenate str (not "int") to str(문자열과 숫자열 사이에 연산자를 쓰려고 할 때)

print(x) => NameError: name 'x' is not defined(변수가 정의되지 않았을 때)

a = 100
print("%d" % a) => ValueError: incomplete format(형식이 잘못 지정되었을 때)

if x>10
    print('kim') => SyntaxError: invalid syntax(문법에 맞지 않는 명령을 할 때)

a = [1, 2, 3]
print(a[5]) => IndexError: list index out of range(잘못된 인덱스를 지정했을 때)

def add():
    a += 1 => UnboundLocalError: 지역변수를 할당하지 않았을 때.

import modd => ModuleNotFoundError: No module named 'modd'(잘못된 이름의 모듈을 불러왔을 때)

f = open('readfile.txt', 'r') => FileNotFoundError: No such file or directory:(잘못된 이름의 파일을 불러왔을 때)

f = open('d:\readfile.txt','r') => OSError: Invalid argument:(잘못된 경로를 입력했을 때)

...
"""
'''
try:
    print(2/1) # 우선 try를 실행해 보고,
    print(10/0)
except Exception: # 예외처리 클래스 지정: 비울 경우 모든 오류에 대해 실행하지만, 어떤 예외를 처리할 것인지 구체적으로 지정해주는 것이 바람직함.
# 또는 except ZeroDivisionError: 도 사용 가능. 가능한 하위의 클래스로, 구체적으로 지정하는 것이 바람직.
    print("오류가 발생되었습니다.") # 오류 발생시 except를 실행.
finally: # finally는 오류 여부(try, except)와 상관 없이 항상 실행.
    print('나누기')

try:
    print('age=' + 23)
except TypeError as e: # as를 통해 다른 이름으로 호출할 수 있음.
    print(e, "발생") # 그대로 표시하여 발생한 에러를 구체적으로 표시할 수 있음.

# 에러 처리를 여러 개 지정할 수 있지만, 에러가 처음 발생했을 때 해당 except로 바로 이동하고 그 뒤는 무시됨.
try:
    print("아직까지는 문제가 없음.")
    print(10/0)
    print('age=' + 23)
except TypeError as e: # 세 번째 줄은 실행되지 않았으므로 해당 except는 실행되지 않음.
    print(e, "발생")
except Exception: # 두 번째 줄에서 에러 발생하여 except 실행. 이후 종료.
    print("exeption error")

# try-else
try:
    num = int(input('input number: '))
except ValueError:
    print('정수가 아닙니다.')
else: # except를 거치지 않았을 경우(오류가 발생하지 않았을 경우) 해당 명령 실행.
    print(num)
finally:
    print("end") # 오류 유무 상관없이 항상 실행.
'''
#
try:
    f = open('testex.txt', 'r')
except FileNotFoundError: # 예외처리.
    pass
else:
    data = f.read()
    print(data)
    f.close()
finally:
    print('종료')