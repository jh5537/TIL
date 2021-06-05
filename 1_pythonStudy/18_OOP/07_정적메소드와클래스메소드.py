# 정적 메소드(static method)
# @staticmethod
'''
class Calc:
    @staticmethod
    def add(a, b):
        return a+b

    @staticmethod
    def sub(a, b):
        return a-b

    @staticmethod
    def mul(a, b):
        return a*b

    @staticmethod
    def div(a, b):
        return a/b

'''
# 클래스메소드(class method): self를 통하지 않고 바로 클래스가 메소드를 호출 - 클래스 변수를 이용하는 메소드를 정의할 때 주로 사용.
# @classmethod: 클래스메소드임을 표시
class Person:
    count = 0 # 클래스변수

    def __init__(self, name):
        Person.count += 1
        self.name = name

    @classmethod
    def showCount(cls): # ()안에 self 대신 cls 입력.
        print('%d명 태어났습니다.' % cls.count) # cls로 클래스 속성에 접근.

    def greeting(self):
        print('%s가 인사해요.' % self.name)

kim = Person('Kim')
Person.showCount()
lee = Person('Lee')
Person.showCount()
kim.greeting()
lee.greeting()

# 교재 p. 137