'''
Each node that exists in the BST will be a product object.
Each node in the BST contains details like product ID, name, price, and stock quantity.

        Visualizing the product object:

        product_id : 111,
        product_name : Product1,
        price: 99.99,
        quantity: 99


Each product in the BST will be represented as an object rather than a hashmap

'''
class Product:
    def __init__(self, product_id, product_name, price, quantity):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.quantity = quantity 


    def setProductId(self, id):
        self.product_id = id

    def setProductName(self, name):
        self.product_name = name

    def setPrice(self, price):
        self.price = price

    def setQuantity(self, quantity):
        self.quantity = quantity 


    def displayProductInformation(self):
        print("Product Information:")
        print(f"   ID: {self.product_id} | Item: {self.product_name}")
        print(f"   Quantity Available: {self.quantity}")
        print(f"   Price: ${self.price}")
        print()



