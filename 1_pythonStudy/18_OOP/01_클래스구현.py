# 클래스 선언: class 클래스이름 [(슈퍼클래스명)]: ;필드(속성)1 ;필드(속성)2 ;def method1(self): ;...
'''
# 빈 클래스 정의
class Car:
    pass

car1 = Car() # 인스턴스 생성
car2 = Car()
car3 = Car()
print(car1) # <__main__.Car object at 0x7fda60168130> : Car에 대한 객체임을 표시함.

# 메소드 추가
class Car:
    def show(self): # Car에 대한 메서드 정의.
        print('시험중입니다.')

car1 = Car() # 인스턴스 생성
car1.show() # 정의한 메서드 수행.

car2 = Car()
car3 = Car()
car2.show() # 같은 메서드 호출하여 수행 가능.
car3.show()

# 특정 클래스의 인스턴스인지 확인: isinstance(인스턴스명, 클래스명) - True/False로 반환
print(isinstance(car1, Car))
print(isinstance(car1, int)) # int는 내장 정수형 클래스(builtins/ Class Int)

x = 3
y = list([1,2,3,4])
print(isinstance(x, int))
print(isinstance(y, list)) # list도 클래스에 해당.

print(type(x)) # <class 'int'> - 이와 같은 형태로 이미 클래스를 사용 중. (int, float, bool, str, list, dict, set, tuple...)

a = True
print(isinstance(a, int)) # a는 불형(True)이지만, 불형은 값을 입력받을 때 True=1, False=0으로 처리하기 때문에 정수형 클래스 확인해도 True 반환.
# instance와 object: 클래스와 연관지어 언급할 때는 인스턴스, 단독으로 언급할 때에는 오브젝트라고 하지만 궁극적으로는 같은 것.

# 필드 추가: 메서드 내에서 사용.
class Car:
    def show(self): # 메서드 정의.
        print('시험중입니다.')

    def drive(self, speed):
        self.speed = speed # speed 필드.
        print('%d로 주행중입니다.' % self.speed)

# 메인: 인스턴스를 생성하고 이용.
car1 = Car()
car1.drive(60)
print(car1.speed) # self.speed라는 변수가 각 인스턴스에 맞게 생성(car1.speed).
car1.drive(100)

# 인스턴스.필드 를 사용하여 필드 생성.
car1.color = 'red'
print(car1.color)

# 클래스 내에서 필드 선언.
class Car:
    speed = 0
    color = ''

    def show(self):
        print('시험중입니다.')

    def drive(self):
        print('%d로 주행중입니다.' % self.speed)

mycar = Car()
print(mycar.speed)
mycar.drive()
mycar.speed = 60
mycar.drive()

# 생성자(constructor): 인스턴스를 생성해주는 함수(객체가 생성될 때 자동으로 호출되는 메서드).
class Car:
    def __init__(self): # 기본 생성자
        self.color = 'white' # 객체 생성할 때마다 해당하는 필드를 생성.
        self.speed = 0

    def showInfo(self):
        print('이 자동차의 색상은 %s입니다.' % self.color)

    def drive(self):
        if self.speed != 0:
            print('%d로 주행중입니다.' % self.speed)
        else:
            print('정차중입니다.')

mycar = Car() # 기본 생성자: 인스턴스 호출 => 인스턴스명.클래스이름()
print(mycar.color)
print(mycar.speed)
mycar.showInfo()
mycar.drive()
mycar.speed = 50
mycar.drive()

"""
_의 쓰임 
언더바 1개 _ : 변수에 특별한 이름을 부여하고 싶지 않을 때(변수명 대신 사용).
for _ in range(10):
    print('hi')

언더바 2개__: 특수한 예약 함수나 변수에 사용. 
    ex) __init__(): 생성자, __str__(): 클래스로 인스턴스를 생성했을 때, 그 인스턴스 자체를 print()로 출력하면 나오는 값.
    __변수명: 비공개 필드(속성)
    __메서드명(): 비공개 메서드
"""
# 매개변수가 있는 생성자 __init__(self, 매개변수1, 매개변수2, ...) => 필드의 초기값 지정.
class Car:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

    def showInfo(self):
        print('이 자동차의 색상은 %s입니다.' % self.color)

    def drive(self):
        if self.speed != 0:
            print('%d로 주행중입니다.' % self.speed)
        else:
            print('정차중입니다.')

mycar = Car('red', 10) # 필드의 초기값을 함께 입력해주어야 함.
print(mycar.color)
print(mycar.speed)
mycar.showInfo()
mycar.drive()
mycar.speed = 50
mycar.drive()

yourcar = Car('blue', 0)
yourcar.showInfo()
yourcar.drive()

# 디폴트 매개변수를 사용한 생성자.
class Car:
    def __init__(self, speed=0, color='white'): # 디폴트 지정.
        self.color = color
        self.speed = speed

    def showInfo(self):
        print('이 자동차의 색상은 %s입니다.' % self.color)

    def drive(self):
        if self.speed != 0:
            print('%d로 주행중입니다.' % self.speed)
        else:
            print('정차중입니다.')

car1 = Car()
car2 = Car(color = 'yellow') # 매개변수는 순서대로 인식하기 때문에 앞을 디폴트로 놔두고 뒤만 입력하려면 별도로 매개변수 이름을 지정해주어야 함.
car3 = Car(10, 'blue')
car4 = Car(10)

car1.showInfo()
print(car2.speed)
car2.showInfo()
car3.showInfo()
car4.drive()

# 비공개 필드, 메서드
class Car:
    def __init__(self, speed=0, color='white'): # 디폴트 지정.
        self.__color = color # 비공개필드 정의: __필드명 - 클래스 내부의 함수를 통해서만 변형 가능.
        self.speed = speed

    def __str__(self): # print() 사용시 반환값의 문자열을 출력.
        return '이 자동차의 색상은 %s이고,\n속도는 %d입니다.' % (self.__color, self.speed)

    # color 필드값을 반환하는 메서드.
    def getColor(self):
        return self.__color

    # color 필드값을 변경
    def setColor(self, color):
        self.__color = color

    def __showColor(self): # 비공개 메서드 정의.
        print('이 자동차의 색상은 %s이고,' % self.__color)

    def showInfo(self): # 클래스 내의 다른 메서드에서 비공개 메서드를 호출하여 사용.
        self.__showColor()
        print('속도는 %d입니다.' % self.speed)

car1 = Car()
print(car1.getColor())
car1.color = 'blue' # 인스턴스의 필드를 직접 변경. (현재 불가능)
# car1.__showColor() 는 외부에서 직접 접근하지 못하기 때문에 오류 출력.
car1.showInfo() # 비공개 필드(__color) 설정하면 외부에서 접근이 불가능해짐.
car1.setColor('red')
print(car1.getColor()) # 클래스 안에서 메서드를 통해 필드 변경은 가능.

# 연습문제
class Dog:
    def __init__(self, name, breed, age, color): # 디폴트 지정.
        self.__name = name
        self.__breed = breed
        self.__age = age
        self.__color = color

    def eat(self, food):
        print(food+'을 먹는다.')

    def sleep(self):
        print(self.__name+'가 잠들었다.')

    def play(self):
        print(self.__name+'가 놀고있다.')

dog1 = Dog('크고검은개', 'NeapolitanMastiff', 5, 'Black')
dog2 = Dog('작은흰개', 'Maltese', 2, 'White')
dog3 = Dog('중간갈색개', 'ChowChow', 3, 'Brown')

dog1.eat('개밥')
dog2.eat('고구마')
dog3.eat('초콜릿')
dog1.sleep()
dog2.sleep()
dog3.sleep()
dog1.play()
dog2.play()
dog3.play()
'''
#
class Car:
    def __init__(self, speed=0, color='white'):
        self.color = color
        self.speed = speed

    def drive(self):
        if self.speed != 0:
            print('%d로 주행중입니다.' % self.speed)
        else:
            print('정차중입니다.')

    def upSpeed(self, up):
        self.speed += up

    def downSpeed(self, down):
        self.speed -= down
        if self.speed < 0:
            self.speed = 0

car1 = Car()
car1.drive()
car1.upSpeed(10)
car1.drive()
car1.upSpeed(30)
car1.drive()
car1.downSpeed(20)
car1.drive()
car1.downSpeed(30)
car1.drive()
