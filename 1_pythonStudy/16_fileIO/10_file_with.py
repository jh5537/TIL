# with문

with open('test3.txt', 'w') as f:
    f.write('hello') # 자동으로 파일을 만들고 연 다음 'hello'를 입력하고 닫음.

filename = 'text4.txt'
data = '''나는 파이썬을 배우고 있어요.
쉽지는 않지만
하나씩 해내니 성취감이 느껴져 좋네요.'''

with open(filename, 'w', encoding='utf-8') as f:
    f.write(data)

