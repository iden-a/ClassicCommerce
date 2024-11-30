'''
Once the orders are added to the stack, inside here we will update the status from pending to completed

Stack - orders that are ready for shipment will be placed here
BST/product catalog - we need to have the BST here because we need to update the catalog 
once an order has been completed we need to update our product quantity because we will have less of a specific product
'''

class Fulfillment:
    def __init__(self, order_stack, product_catalog):
        self.order_stack = order_stack  # Stack for fulfilled orders
        self.product_catalog = product_catalog  # Reference to the product catalog (BST)

    def fulfillOrder(self, order):
        # Process each item in the order
        for item in order.products:
            product_id = item['product_id']
            req_quantity = item['requested_quantity']
            
            # Find the product in the catalog
            product = self.product_catalog.getProductInformation(product_id) 
            

            try:
                if product.quantity >= req_quantity:
                    
                    # Fulfill the requested quantity, the remove function also updates, it will remove if necessary
                    self.product_catalog.removeFromProductCatalog(product.product_id, req_quantity)
                else:
                    print(f"Insufficient stock for {product.product_name}. Order cannot be processed successfully!")
                    print(f"Product Quantity: {product.quantity} ")

                    print(f"Requested Quantity: {req_quantity} ")
                    self.order_stack.removeFromStack()
                    return  # Stop processing this order since it can't be fulfilled
                
            except:
                print(f"Error Processing! Product ID: {product_id} for Order: {order.order_id}")
                print("Either ID invlaid, or Product out of Stock!")
                self.order_stack.removeFromStack()
                return  # Stop processing this order since the product doesn't exist

        # If all items are fulfilled, mark the order as fulfilled and display the details
        order.setStatus("fulfilled")
        print("\nFulfilled Order Details:")
        order.displayOrderInformation()


