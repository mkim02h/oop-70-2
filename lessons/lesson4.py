# class Test():
#     def __init__(self, value):
#         self.value = value
#     def __str__(self):
#         return self.value
#     # def __add__(self, other):
#     #     return self.value + other.value
#     # def __getitem__(self, item):
#     #     return self.value[item]
#     def __call__(self, *args, **kwargs):
#         self.value += 1
#         print(self.value)
#         print("+1 call")
#
# test_view = Test(0)
# test_view()


# my_list = Test([1,2,3,4,5])
# print(my_list[0])
# my_obj = Test('Hello')
# my_str = "My STR"
# my_int = Test(123)
# my_int_2 = Test(123)
# my_int_3 = my_int + my_int_2
# print(my_obj.value)
# print(my_str)
# print(my_int_3)

# class Money:
#     def __init__(self, value, currency):
#         self.value = value
#         self.currency = currency
#     def __add__(self, other):
#         if self.currency == other.currency:
#             return Money(self.value + other.value)
#         else:
#             return "error"
#
# usd = Money(100, 'USD')
# som = Money(200, 'SOM')
# total_money = usd + som
#
# class Math:
#     def __init__(self, value):
#         self.value = value
#     @staticmethod      #Не нуждается в создании объекта
#     def add_two_nums(a, b):
#         return a + b
# # test_obj = Math(5)
# print(Math.add_two_nums(3, 4))

class Bank:
    #Атрибуты класса
    bank_name = "Kompanion"
    def __init__(self, capital):
        #Атрибуты экземпляра класса
        self.capital = capital
    def get_capital(self):
        return self.capital
    @classmethod
    def get_bank_name(cls):
        return cls.bank_name
test = Bank(43434654)
print(test.get_capital())
print(Bank.get_bank_name())