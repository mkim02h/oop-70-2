class Hero:
 #Конструктор класса
    def __init__(self, name, lvl, hp):
        #Атрибуты экземпляра\объекта класса
        self.name = name
        self.lvl = lvl
        self.hp = hp
    #Метод класса
    def base_action(self):
        print(f'{self.name} this my base action!!')

kirito = Hero("Kirito", 100, 1000)
asuna = Hero("Asuna", 90, 900)
kirito.base_action()
asuna.base_action()
print(kirito.name)
print(asuna.name)
print(kirito.hp)