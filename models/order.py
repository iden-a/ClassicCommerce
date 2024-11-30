'''
Each order includes details such as customer information, list of products, and quantity requested.
    Visualizing the order object:

    order_id: 1,
    customer_name: Alice Smith
    customer_address: 123 Main St 
    products: [
        {"product_id": 101, "name": "Laptop", "quantity": 1},
    ]
    status: pending
'''
from structures.bst import Tree

class Order:

    order_id_counter = 0

    def __init__(self, customer_name, address):

        self.product_catalog = Tree()

        Order.order_id_counter  += 1 # autogenerating order ids
        self.order_id = Order.order_id_counter # assigning the order id to the auto generated order id 
        self.customer_name = customer_name
        self.address = address
        self.products = [] 
        self.status = "pending"

    def setCustomerName(self, name):
        self.customer_name = name

    def setAddress(self, address):
        self.address = address

    def addProductToOrder(self, product_id, product_name, price, quantity):
        product = {
            "product_id": product_id,
            "product_name": product_name,
            "price": price,
            "requested_quantity": quantity,
        }
        self.products.append(product)

    def setStatus(self, status):
        self.status = status

    def displayOrderInformation(self):
        print("Order ID:", self.order_id)  
        print("Customer Name:", self.customer_name)
        print("Address:", self.address)
        print("Products:")
        for product in self.products:
            print(f"  - {product['requested_quantity']}x {product['product_name']} (ID: {product['product_id']}, Price: {product['price']})")
        print("Order Status:", self.status)
        print()

        

    
        
