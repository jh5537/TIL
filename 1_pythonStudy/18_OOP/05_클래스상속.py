# 클래스 상속(inheritance)
'''
class Car(): # 슈퍼클래스(상위) 생성. ()는 (object)가 축약된 것.
    def __init__(self, speed=0, color='white'):
        self.color = color
        self.speed = speed

    def __str__(self):
        return '이 자동차의 색상은 %s이고,\n속도는 %d입니다.' % (self.color, self.speed)

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def __showColor(self):
        print('이 자동차의 색상은 %s이고,' % self.color)

    def showInfo(self):
        self.__showColor()
        print('속도는 %d입니다.' % self.speed)

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

class Truck(Car): # 서브클래스(하위) 생성. ()안에는 상위클래스 입력.
    def __init__(self, speed, color, load):
        super().__init__(speed, color) # 부모 객체를 그대로 사용.
        self.load = load # 하위클래스만의 고유한 필드 추가.

    # 메서드를 재정의: 오버라이딩(overriding)
    def showLoad(self):
        print(self.load)

    def upLoad(self,up):
        self.load += up

    def showInfo(self): # 상위클래스에 있는 메서드를 새로 재정의할 수도 있음.
        print('트럭... 속도는 %d이고, 적재량은 %d입니다.' % (self.speed, self.load))

car1 = Car()
car2 = Truck(0, 'Blue', 1000)

car1.showInfo()
car2.upSpeed(20) # Truck() 자체의 내부에는 upSpeed()가 없지만, Car()에서 상속받았으므로 사용할 수 있음.
car2.showInfo()  # showInfo()를 새로 정의하면 새로운 정의대로 나옴.
car2.upLoad(10)
car2.showInfo()

print(isinstance(car2, Car)) # 하위클래스의 인스턴스도 상위클래스에 속하는 것으로 취급.
print(issubclass(Truck, Car)) # 상위클래스와 하위클래스의 관계 확인도 가능.

class SportCar(Car):
    def __init__(self, speed, color, seats):
        super().__init__(speed, color)
        self.seats = seats

    def showInfo(self): # 같은 이름의 메서드지만 실제 수행하는 기능이 다름 - 다형성(polymorphism).
        print('Sport Car : 색상은 %s, 좌석수는 %d' % (self.color, self.seats))

car3 = SportCar(0, 'Red', 2)
car3.showInfo()

carL = [car1, car2, car3]
for car in carL:
    car.showInfo() # 각 인스턴스가 가지고 있는 다형성을 반영하여 메서드 수행.

# 연습문제
class Dog:
    def __init__(self, name, breed, age, color):  # 디폴트 지정.
        self.__name = name
        self.__breed = breed
        self.__age = age
        self.__color = color

    def __str__(self):
        return "이 강아지의 이름은 %s이고, %d살이며, 종은 %s입니다." % (self.__name, self.__age, self.__breed)

    def __lt__(self, other):
        return self.__age < other.__age

    def __eq__(self, other):
        return self.__age == other.__age

    def eat(self, food):
        print(food + '을 먹는다.')

    def sleep(self):
        print(self.__name + '가 잠들었다.')

    def play(self):
        print(self.__name + '가 놀고있다.')


dog1 = Dog('크고검은개', 'NeapolitanMastiff', 5, 'Black')
dog2 = Dog('작고흰개', 'Maltese', 2, 'White')
dog3 = Dog('중간갈색개', 'ChowChow', 3, 'Brown')

print(dog1)
print(dog2)
print(dog3)
dog1.eat('개밥')
dog2.sleep()
dog3.play()
print(dog2 < dog3)
print(dog1 == dog2)
'''
# 상속 연습문제: 사람 클래스 Person(슈퍼클래스) -> 학생 클래스 Student(서브클래스)

class Person:
    def __init__(self, age, sex, name):
        self.age = age
        self.name = name
        self.sex = sex

    def greeting(self):
        print('안녕하세요.')

class Student(Person): # 학교, 학과, 학번, 공부하다(), 시험보다()
    def __init__(self, age, sex, name, univ, dept, stnum):
        super().__init__(age, sex, name)
        self.univ = univ
        self.dept = dept
        self.stnum = stnum

    def study(self):
        print(self.name+'은 '+self.univ+'에서 '+self.dept+'를 공부합니다.')

    def exam(self):
        print(self.name+'은 '+self.dept+'의 전공시험을 봤습니다.')
        from random import randint
        g = randint(1,100)
        if g >= 90:
            gd = 'A'
            print("그리고 학점 %s를 받았습니다. 축하해요." % gd)
        elif g >= 70:
            gd = 'B'
            print("그리고 학점 %s를 받았습니다. 고생하셨어요." % gd)
        elif g >= 40:
            gd = 'C'
            print("그리고 학점 %s를 받았습니다. 그럭저럭." % gd)
        else:
            gd = 'F'
            print("그리고 학점 %s를 받았습니다. 다음에 또 만나요." % gd)

std1 = Student(23, 'M', 'Kim', "K", 'E', 14)
std1.greeting()
std1.study()
std1.exam()