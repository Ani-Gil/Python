# 051.py - 클래스 메소드 이해하기

class MyClass:
    def sayHello(self):
        print('안녕하세요')

    def sayBye(self, name):
        print('%s! 다음에 보자!' % name)

obj = MyClass()
obj.sayHello()          # '안녕하세요'가 출력됨
obj.sayBye('철수')      # '철수! 다음에 보자!'가 출력됨