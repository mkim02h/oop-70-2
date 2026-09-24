class BankAccount:
    def __init__(self, login, password, balance):
        self.login = login
        self.__password = password
        self._balance = balance
    def login_method(self, login, password):
        if self.login == login and self.__password == password:
            print(f"My balance is {self._balance}")
        else:
            print("Wrong login or password!!!")

mask = BankAccount("Mask", 2345, 5000)
mask.login_method("Mask", 2345)
# print(mask._balance)
# print(mask.login)
# print(mask.__password)

from abc import ABC, abstractmethod
#Абстрактный класс
class Animal(ABC):
    #Абстрактный метод
    @abstractmethod
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        print('Gaf gaf')
gufi = Dog()
gufi.make_sound()
class Cat(Animal):
    def make_sound(self):
        print('Meow meow')
tom = Cat()
tom.make_sound()
