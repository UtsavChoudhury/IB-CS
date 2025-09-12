class Product:
    next_id = 0 # class / static variables
    def __init__(self, description, price): # parameters
        self.description = description # instance variables
        self.id_num = Product.next_id
        Product.next_id += 1
        self.price = price
        
    def __str__(self):
        return f'{self.description} ({self.id_num}) @ {self.price}'
    
pc = Product('PC', 199.95) # constructor that automatically calls __init__()
mac = Product('macmac', 2999.95) 

print(pc)
print(mac)