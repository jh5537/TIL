class Car:
    number = 0
    def __init__(self, speed=0, color='white'): # 디폴트 지정.
        self.color = color # 비공개필드 정의: __필드명 - 클래스 내부의 함수를 통해서만 변형 가능.
        self.speed = speed
        Car.number += 1 # 클래스 변수: 클래스 안의 모든 인수들이 공유하는 변수.

    def __str__(self):
        return '이 자동차의 색상은 %s이고,\n속도는 %d입니다.' % (self.color, self.speed)

    # color 필드값을 반환하는 메서드.
    def getColor(self):
        return self.color

    # color 필드값을 변경
    def setColor(self, color):
        self.color = color

    def __showColor(self):
        print('이 자동차의 색상은 %s이고,' % self.color)

    def showInfo(self):
        self.__showColor()
        print('속도는 %d입니다.' % self.speed)

# 인스턴스 변수(필드)
car1 = Car()
print(car1.speed)
print(car1.color)
print(Car.number)

car2 = Car(10, 'Blue')
print(Car.number)
