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

thor = Hero("Thor", 1, 10, 100)
loki = Hero("Loki", 2, 20, 200)
thor.greet()
thor.attack()
print(thor.strength)
thor.rest()
print(thor.health)
loki.greet()
loki.attack()
print(loki.strength)
loki.rest()
print(loki.health)
