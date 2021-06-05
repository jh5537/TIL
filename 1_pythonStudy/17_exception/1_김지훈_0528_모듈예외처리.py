# 1번
print('===1번)===========================')
"""
def f(x,y):
    return x ** y
"""
f = lambda x, y: x ** y
print("f = lambda x, y: x ** y")

# 2번
print('===2번)===========================')
ex = [1, 2, 3, 4, 5]
# [value ** 2 for value in ex]
list(map(lambda x: x ** 2, ex))
print("list(map(lambda x: x ** 2, ex))")

# 3번
print('===3번)===========================')
print("정답 : 3번")

# 4번
print('===4번)===========================')
print("정답 : 3번")

# 5번
print('===5번)===========================')
print("정답 : 2번")

# 6번
print('===6번)===========================')
print("import fah_converter as fah")

# 7번
print('===7번)===========================')
print("'game' 디렉토리 경로참조 설정\nimport game.graphic.render as rd\nrd.render_test()")

# 8번
print('===8번)===========================')
"""
f = open("hello_python.txt", 'a')
f.write('hello, python!')
"""
print("(가): a\n(나): write")

# 9번
print('===9번)===========================')
print("(가): w\n(나): a\n(다): r")

# 10번
print('===10번)===========================')
print("from calculator_input import *")

# 11번
print('===11번)===========================')
# 예측
print("예측")
print("7\n3\n2\n1\n1\n1\n종료되었습니다.")
# 결과
print("결과")
try:
    for i in range(1, 7):
        result = 7 // i
        print(result)
except ZeroDivisionError:
    print("Not divided by 0")
finally:
    print("종료되었습니다.")

# 12번
print('===12번)===========================')
# 예측
print("예측")
print("pop from empty list\n정답 : 5번")
# 결과
print("결과")
sentence = list("Hello Gachon")
while (len(sentence) + 1):
    try:
        print(sentence.pop(0))
    except Exception as e:
        print(e)
        break

# 13번
print('===13번)===========================')
print("(가): IndexError, (나): ValueError\n정답 : 4번")

# 14번
print('===14번)===========================')
print("SyntaxError: invalid syntax\n정답 : 4번")
# SyntaxError는 조건문이나 변수에 오탈자가 아닌, 문법 자체의 오류일 때 발생.

# 15번
print('===15번)===========================')
print("정답 : 2번")
# 정답 4번. 텍스트 파일 그대로 처리 불가능.

# 16번
print('===16번)===========================')
# 예측
print("예측")
print("숫자가 아닙니다.")
# 결과
print("결과")
import random
answer = random.randint(1,10)
def guess_number(answer):
    try:
        guess = int(input("숫자를 넣어 주세요: "))
        if answer == guess:
            print("정답!")
        else:
            print("틀렸습니다.")
    except ValueError:
        print("숫자가 아닙니다.")

guess_number(answer)

# 17번
print('===17번)===========================')
print("1) NameError\n2) FileNotFoundError\n3) RuntimeError\n4) KeyError")
"""
1 - NameError
2 - IOError
3 - RuntimeError
4 - KeyError
"""
# 18번
print('===18번)===========================')
# 예측
print("예측")
print("Not divided by 0\n3\n1")
# 결과
for i in range(3):
    try:
        print(i, 3//i)
    except ZeroDivisionError:
        print("Not divided by 0")

# 19번
print('===19번)===========================')
"""
f = open("i_have_a_dream.txt", "r")
contents = f.read()
print(contents)
f.close()
"""
print("""with open('i_have_a_dream.txt', 'r') as f:
    contents = f.read()
print(contents)
""")