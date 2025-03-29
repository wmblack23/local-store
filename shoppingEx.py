from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def buy_product(self):
        pass

    def __init__(self, name, price):
        self.name = name
        self.__price = price

    def get_price(self):
        return self.__price

class PhysicalProduct(Product):
    def __init__(self, name, price, stock_amt):
        super().__init__(name, price)
        self.__stock_amt = stock_amt

    def buy_product(self):
        if self.__stock_amt > 0:
            self.__stock_amt -= 1
            return f"Purchase confirmed. There are now {self.__stock_amt} {self.name}'s available."
        else:
            return f"This item '{self.name}' is currently out of stock."

    def get_stock_amt(self):
        return self.__stock_amt

class DigitalProduct(Product):
    def buy_product(self):
        return f"Purchase of {self.name} confirmed."

p1 = PhysicalProduct("iPhone", 1200.00, 5)
p2 = DigitalProduct("Gift Card", 50.00)

print(p1.get_stock_amt())
print(p1.buy_product())
print(p1.buy_product())
print(p1.buy_product())
print(p1.buy_product())
print(p1.buy_product())
print(p1.buy_product())
print(p2.buy_product())