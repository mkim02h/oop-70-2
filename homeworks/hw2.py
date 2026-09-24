import random
class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength
    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level} ")
    def attack(self):
        print(f"{self.name} наносит удар!")
        self.strength -= 1
    def rest(self):
        print(f"{self.name} отдыхает...")
        self.health += 1

class Warrior(Hero):
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina
    def attack(self):
        self.stamina -= 30
        return f"{self.name} атакует мечом!"
    def beats(self, other):
        return isinstance(other, Assasin)
class Mage(Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana
    def attack(self):
        self.mana -= 50
        return f"{self.name} кастует заклинание!"
    def beats(self, other):
        return isinstance(other, Warrior)
class Assasin(Hero):
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth
    def attack(self):
        self.stealth -= 100
        return f"{self.name} атакует из-под тишка!"
    def beats(self, other):
        return isinstance(other, Mage)

warrior = Warrior('Warrior', 1, 10, 100, 50)
mage = Mage("Mage", 1, 10, 100, 300)
assasin = Assasin("Assasin", 1, 10, 100, 150)

class Game:
    Heroes = {"Warrior": warrior, "Mage": mage, "Assasin": assasin}
    def choose_hero(self):
        while True:
            choice = input("Выберите героя Warrior/Mage/Assasin: ")
            if choice in self.Heroes:
                return self.Heroes[choice]
            else:
                print("Некорректный выбор. Попробуйте еще раз.")
    def choose_enemy(self):
        hero_class = random.choice(list(self.Heroes.values()))
        return hero_class()
    def battle(self, player, enemy):
        print(f"Вы выбрали {player}")
        print(f"Противник выбрал {enemy}")
        if player.beats(enemy):
            print(f"{player} победил!")
        elif enemy.beats(player):
            print(f"{enemy} победил!")
        else:
            print("Ничья!")
    def start(self):
        player = self.choose_hero()
        enemy = self.choose_enemy()
        self.battle(player, enemy)

game = Game()
game.start()
# Heroes = {warrior, mage, assasin}
# player = input(f"Выберите персонажа (Warrior/Mage/Assasin): ").lower()
# enemy = random.choice(list(Heroes))
#
# if player in Heroes:
#     print(f"Вы выбрали {player}")
#     print(f"Противник: {enemy}")
# else:
#     print("Некорректный выбор, попробуйте еще раз.")
# if player == warrior and enemy == mage:
#     print("Вы проиграли!")
# elif player ==