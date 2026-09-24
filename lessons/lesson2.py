#Родительский класс
class Hero:
 #Конструктор класса
    def __init__(self, name, lvl=1, hp=100):
        #Атрибуты экземпляра\объекта класса
        self.name = name
        self.lvl = lvl
        self.hp = hp
    #Метод класса
    def base_action(self):
        print(f'{self.name} this my base action!!')
    def method1(self):
        print("I`m method1")
#Дочерний класс
class MageHero(Hero):
    def cast_spell(self):
        return f"{self.name}  fireball!"
    def method1(self):
        return f"{self.name} {self.hp} {self.lvl}"
maks = MageHero('maks')
arthur = Hero('arthur')
# print(maks.cast_spell())
# print(arthur.base_action())
print(maks.method1())
print(arthur.method1())

# class Swim:
#     def swim(self):
#         print("Swim")
# class Fly:
#     def fly(self):
#         print("Fly")
# class Duck(Fly, Swim):
#     pass
# DonaldDuck = Duck()
# DonaldDuck.fly()
# DonaldDuck.swim()
