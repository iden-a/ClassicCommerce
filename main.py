'''
Users interact with our system here!
Run 
`python main.py` OR `python3 main.py`
'''
from system.order_processing import OrderProcessingSystem
from models.product import Product
from structures.bst import Tree

def setupProductCatalog():
    # initialize a product catalog (binary search tree) and add some products
    product_catalog = Tree()
    products = [
        Product(372, "Organic Almonds", 12.99, 10),
        Product(163, "Whole Grain Bread", 4.99, 5),
        Product(605, "Cold Brew Coffee", 3.49, 20),
        Product(204, "Greek Yogurt", 1.49, 15),
        Product(563, "Quinoa", 6.99, 6),
        Product(166, "Mixed Berries", 5.99, 3),
        Product(521, "Avocado Oil", 9.99, 1)
    ]
    for product in products:
        product_catalog.insertIntoProductCatalog(product)

    return product_catalog

def main():
    # Initialize the order processing system
    product_catalog = setupProductCatalog()
    order_system = OrderProcessingSystem(product_catalog)

    print("\nWelcome to ClassicCommerce Online System!")
    print()
    for product in product_catalog.displayInOrder():
        product.displayProductInformation()

    
    while True:
        print("___________________________________________________________")
        print("\nPlease Enter Your Order Details:")

        # gathering user input for the orders
        customer_name = input("Enter your name: ")
        address = input("Enter your address: ")

        # store the order's product information
        order_items = []
        product_id = int(input("Enter Product ID: ")) 
        requested_quantity = int(input("Enter Quantity: "))
        
        # wrapping in a try except block, in the case where we may get an invalid product id from the user
        try:
            product = product_catalog.getProductInformation(product_id) # finding the product by ID
                # Append the item to the order
            order_items.append({
                "product_id": product_id,
                "product_name": product.product_name,
                "price": product.price,
                "requested_quantity": requested_quantity,
            })

        except:
            print("Error - Product Not Found!")
            if product == None:

                # Check if user wants to place another order
                another_order = input("Would you like to place another order? (y/n): ").lower()
                if another_order != 'y':
                    print("\nThank you for using ClassicCommerce!")
                    break
            


        # process the order in our system
        order = order_system.createOrder(
            customer_name,
            address,
            order_items
        )
        
        # displaying confirmation for successful orders
        if order:
            print(f"\nOrder placed successfully! Order ID: {order.order_id}")
            print("Order details:")
            print(f"Customer: {order.customer_name}, Address: {order.address}")
            print("Items ordered:")
            for item in order.products:
                print(f" - {item['product_name']} (ID: {item['product_id']}), "
                      f"Price: ${item['price']}, Quantity: {item['requested_quantity']}")
        else:
            print("\nOrder could not be processed due to insufficient stock or invalid product ID.")

        # check if user wants to place another order
        another_order = input("Would you like to place another order? (yes/no): ").lower()
        if another_order != 'y':
            print("\nThank you for using ClassicCommerce!")
            break
        

    order_system.displayPendingOrders() # showing the initial order queue
    order_system.displayFulfilledOrders() # showing the inital order stack

    order_system.processOrders() # processing orders from the queue to the stack

    order_system.displayPendingOrders() # all of the orders in the queue
    order_system.displayFulfilledOrders() # all of the orders in the stack

    order_system.shipOrdersInStack()
    order_system.displayFulfilledOrders() # showing the stack after all orders are shipped
    print("\n___________________________________________________________")


    print("\nProduct Catalog After Orders Have Been Placed & Fulfilled: ")
    for product in product_catalog.displayInOrder():
        product.displayProductInformation()


if __name__ == "__main__":
    main()
