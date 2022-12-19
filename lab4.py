class Driver:
    experience: int

    def toString(self) -> str:
        return f'{self.experience}'

class Engine:
    power: float
    company: str

    def toString(self) -> str:
        return f'{self.power} {self.company}'

class Car:
    carClass: str
    engine: Engine
    driver: Driver
    marka: str

    def toString(self) -> str:
        return f'{self.carClass} {self.driver} {self.engine}'

    @staticmethod
    def stop() -> None:
        print('Останавливаемся')

    @staticmethod
    def start() -> None:
        print('Поехали')

    @staticmethod
    def turnRight() -> None:
        print('Поворот направо')
    
    @staticmethod
    def turnLeft() -> None:
        print('Поворот налево')

class Lorry(Car):
    carrying: int

    def toString(self) -> str:
        return f'{self.carrying}'

class SportCar(Car):
    speed: float

    def toString(self) -> str:
        return f'{self.speed}'

class Person(Driver):
    __age: int
    fullName: str

    def toString(self) -> str:
        return f'{self.fullName} {self.__age}'