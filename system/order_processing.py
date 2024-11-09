'''
This is where orders are processed
Orders need to be validated here 
Orders should be taken from the Queue and added to the Stack

Once an order is "processed" it means that it has gone through the BST, it has been checked for available stock, and it has been sent to the Stack for fullfillment

Queue - we will use this to add all of our incoming validated orders 
Stack - we will only be adding validated orders from our Queue onto the stack
BST - we will use this to make sure that the products that the customers are looking for exist and are available inside of our product catalog
'''
    
from models.order import Order
from structures.queue import Queue
from structures.stack import Stack
from system.fulfillment import Fulfillment

class OrderProcessingSystem:

    def __init__(self, product_catalog):

        self.order_queue = Queue()  # queue to process orders
        self.order_stack = Stack()   # stack for fulfilled orders
        self.fulfillment = Fulfillment(self.order_stack, product_catalog)  # the fulfillment system

        # set the product catalog, this represents the BST
        self.product_catalog = product_catalog 


    def createOrder(self, customer_name, address, order_items):
        order = Order(customer_name, address)
        for item in order_items:
            product_id = item['product_id']
            quantity = item['requested_quantity']
            if self.validateOrder(product_id, quantity):
                order.addProductToOrder(product_id, item['product_name'], item['price'], quantity)
            else:
                print(f"Order cannot be created for {customer_name}. Not enough stock for {item['product_name']}.")

        if order.products:  
            self.order_queue.addToQueue(order)
            print(f"Order ID: {order.order_id} created for {customer_name}")
            return order
        else:
            print(f"Order for {customer_name} is empty. No valid products added.")


    def validateOrder(self, product_id, req_quantity):
        # product represents the product quantity
        product = self.product_catalog.findProduct(product_id)
        return product >= req_quantity

    # processing the orders
    def processOrders(self):
        # we check our queue for orders, remove from the queue, send to fulfillment, then add to stack for shipment
        while not self.order_queue.isQueueEmpty(): 
            order = self.order_queue.removeFromQueue()
            print("______________________________________________________________________")
            print("\n*** Order is Processing (Order Queue - to -  Fulfillment Stack) ***")
            self.fulfillment.fulfillOrder(order)
            self.order_stack.addToStack(order)


    def displayPendingOrders(self):
        print("______________________________________________________________________")
        print("\nOrders in Queue:")
        self.order_queue.displayQueue()

    # this is how our orders are shipped, once in the stack we ship the orders at the top of the stack
    def shipOrdersInStack(self):
        while not self.order_stack.isStackEmpty():
            order = self.order_stack.top() 
            print(f"\n*** Order {order.order_id} Removed From Stack  ***")
            self.order_stack.removeFromStack() # after orders have been shipped they are officially removed from our system


    def displayFulfilledOrders(self):
        print("______________________________________________________________________")
        print("\nOrders in Stack:")
        self.order_stack.displayStack()




