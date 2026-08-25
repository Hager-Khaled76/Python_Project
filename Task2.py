#       Task2
#------------------------
from abc import ABC, abstractmethod

# Abstract Class
class Product(ABC):

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def discount(self):
        pass

    def final_price(self):
        return self.price - self.discount()


# Child Class 1: Electronics
class Electronics(Product):

    def discount(self):
        return self.price * 0.10


# Child Class 2: Clothing
class Clothing(Product):

    def discount(self):
        return self.price * 0.25


# Child Class 3: Food
class Food(Product):

    def discount(self):
        return 0


if __name__ == '__main__':
    cart = [
        Electronics("Laptop", 10000),
        Clothing("Shirt", 400),
        Food("Rice", 50),
    ]

    total = 0
    for product in cart:
        disc = product.discount()
        f_price = product.final_price()
        total += f_price

        # Format output as required: Laptop: 10000 - 1000 = 9000.0
        # If discount is 0, format discount as int (0) else floats
        disc_str = int(disc) if disc == 0 else int(disc)
        print(f"{product.name}: {product.price} - {disc_str} = {f_price}")

    print(f"Total = {total}")