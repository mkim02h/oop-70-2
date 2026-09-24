rates = {
    "KGZ":1,
    "USD":89,
    "EUR":96,
    "RUB":1.2
    }
class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
    def convert_to_kgz(self):
        return self.amount * rates[self.currency]
    def __add__(self, other):
        total_kgz = self.convert_to_kgz() + other.convert_to_kgz()
        return Money(total_kgz, 'KGZ')
    def __sub__(self, other):
        diff_kgz = self.convert_to_kgz() - other.convert_to_kgz()
        return Money(diff_kgz, 'KGZ')
    def __mul__(self, number):
        return Money(self.amount * number, self.currency)
    def __truediv__(self, number):
        return Money(self.amount / number, self.currency)
    def __str__(self):
        return f'{self.amount} {self.currency}'
money1 = Money(100, "USD")
money2 = Money(5000, "KGZ")
total = money1 + money2
print(total)
print(money1-money2)
print(money1*2)
print(money1/2)





