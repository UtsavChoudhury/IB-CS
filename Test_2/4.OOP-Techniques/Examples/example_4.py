class Product:
    def __init__(self, model, price):
        self.model = model
        self.price = price 

class Laptop(Product):
    def __init__(self, model, price):
        super().__init__(model, price)

class Router(Product):
    def __init__(self, model, price):
        super().__init__(model, price)

class Order:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def __str__(self):
        return f"Order: {[f'{p.model} (${p.price})' for p in self.products]}" # Since we have an object of class Product here, we can access its attributes.

class Warehouse:
    def __init__(self, laptops, routers):
        self.laptops = laptops
        self.routers = routers

warehouse = Warehouse([Laptop('mac', 1999)], [Router('netgate', 600)])
order = Order()
order.add_product(warehouse.laptops[0])
order.add_product(warehouse.routers[0])
print(order)