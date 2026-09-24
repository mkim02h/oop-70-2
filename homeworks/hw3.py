from abc import ABC, abstractmethod
class Hero(ABC):
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.__health = health
        self.strength = strength
    def greet(self):
        print(f'Привет, я {self.name}, мой уровень: {self.level}')
    def rest(self):
        print(f'{self.name} отдыхает..')
        self.__health += 1
    @abstractmethod
    def attack(self):
        pass

class Warrior(Hero):
    def attack(self):
        print("Атакует мечом!")
class Mage(Hero):
    def attack(self):
        print("Использует магию!")
class Assasin(Hero):
    def attack(self):
        print("Атакует из-под тишка!")

aaragorn = Warrior('Aaragorn', 1, 100, 100)
gandalf = Mage('Gandalf', 1, 100, 100)
legolas = Assasin('Legolas', 1, 100, 100)

aaragorn.greet()
aaragorn.attack()
aaragorn.rest()
gandalf.greet()
gandalf.attack()
gandalf.rest()
legolas.greet()
legolas.attack()
legolas.rest()
