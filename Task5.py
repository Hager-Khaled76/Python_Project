# Task 5: Product Comparison (Magic Methods)

class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} ({self.price})"

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.price == other.price
        return False

    def __lt__(self, other):
        if isinstance(other, Product):
            return self.price < other.price
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Product):
            return self.price > other.price
        return NotImplemented


# --- Execution and Testing ---
if __name__ == '__main__':
    products = [
        Product("Mouse", 250),
        Product("Laptop", 15000),
        Product("Keyboard", 700),
    ]

    # Automatic sorting thanks to __lt__
    products.sort()

    for p in products:
        print(p)