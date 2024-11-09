'''
Product Catalog with BST
Binary Search Tree (BST) - manage the product catalog for efficient searching and updating of products.

The catalog should store all products in a BST based on product IDs or names for fast lookup, 
insertion, and deletion. Each node in the BST contains details like product ID, name, price, and stock quantity.

Search: Quickly find products by ID or name. 
Add/Remove: Efficiently add new products to the catalog or remove out-of-stock items.
Update: Adjust stock quantities as items are packed for orders.

'''

class Tree:
    def __init__(self, val=None):
        self.value = val # start off empty, None
        if self.value: # if given a value, we are defining the left most part as a tree and the right as a tree
            self.left = Tree()
            self.right = Tree()
        else:
            self.left = None
            self.right = None


    def isProductCatalogEmpty(self):
        return (self.value == None)
    
    # this is adding into the Tree
    def insertIntoProductCatalog(self, product):
        # first, lets check to see if the tree is empty 
        # if the tree is empty we take the given data and add it to the top of the tree making that given data our root
        if self.isProductCatalogEmpty():
            self.value = product

            # we need to create the left and the right children for the given node data
            self.left = Tree()
            self.right = Tree()
            print(f"{self.value.product_name} is inserted successfully")

        # if it is not emptty 
        elif product.product_id < self.value.product_id:
            self.left.insertIntoProductCatalog(product)
            return 
        
        elif product.product_id > self.value.product_id:
            self.right.insertIntoProductCatalog(product)
            return 

        elif product.product_id == self.value.product_id:
            return 
        
    def isLeaf(self):
        # a leaf is a node that does NOT have children 
        # this means that the left is empty AND the right is empty 
        if self.left == None and self.right == None:
            return True
        
        return False
    
    def maxValue(self):
        # we are looking at the right side because all of the values on the right are > than the left
        # eventually, we will reach a node that does NOT have any children on it's right, this will be our larges value
        if self.right.right == None:
            return (self.value)
        
        else:
            return (self.right.maxValue()) # we will keep calling the maxVal function until our given condition is satisifed
        

    # this function incorporates the update helper function
    # it allows us to update the quantity AND remove the product from the BST if necessary
    def removeFromProductCatalog(self, product_id, requestedQuantity):

        if self.isProductCatalogEmpty():
            return
    
        
        if product_id < self.value.product_id:
            self.left.removeFromProductCatalog(product_id, requestedQuantity)
            return 
        elif product_id > self.value.product_id:
            self.right.removeFromProductCatalog(product_id, requestedQuantity)
            return
        
        elif product_id == self.value.product_id:
            # Update quantity based on order request
            self.updateProductQuantity(requestedQuantity)

        # If quantity becomes 0, remove product from catalog
            if self.value.quantity == 0:
                print(f"Product {product_id} is out of stock and being removed from catalog.")

                if self.isLeaf():
                    self.value = None
                    self.right = None
                    self.left = None
                    return
                elif self.left.isProductCatalogEmpty():
                    self.value = self.right.value
                    self.left = self.right.left
                    self. right = self.right.right
                    return 
                
                else: 
                    max_product = self.left.maxValue()
                    self.value = max_product
                    self.left.removeFromProductCatalog(max_product.product_id, 0)
                    return
                
    # this is our helper function to update the available quantity when an order has been placed, used in our remove function
    def updateProductQuantity(self, requestedQuantity):
        # first we should check if the reqQ is greater than the current 
        if self.value.quantity >= requestedQuantity:
            self.value.quantity -= requestedQuantity
            print(f"{requestedQuantity} units of {self.value.product_name} have been fulfilled. Remaining stock: {self.value.quantity}")

        else:
            print(f"Insufficient stock for {self.value.product_name}. Available: {self.value.quantity}, Requested: {requestedQuantity}")


    # this is only returning the id
    def findProduct(self, product_id):
        if self.isProductCatalogEmpty():
            return False
        
        if self.value.product_id == product_id:
            # print (f"Product: {self.value.product_name} - {product_id}, is found in product catalog!")
            return self.value.product_id
        
        if product_id > self.value.product_id:
            return self.right.findProduct(product_id)
        else:
            return self.left.findProduct(product_id)
        
    # this is returning the entire object
    def getProductInformation(self, product_id):
        if self.isProductCatalogEmpty():
            return None

        if self.value.product_id == product_id:
            print(f"Product: {self.value.product_name} - {product_id} is found in product catalog!")
            return self.value  # Return the entire product object
        
        if product_id > self.value.product_id:
            return self.right.getProductInformation(product_id)
        else:
            return self.left.getProductInformation(product_id)
 
        
    # Traverse the Tree in inorder (left-root-right) 
    def displayInOrder(self):
        # display the elements recursively
        if self.isProductCatalogEmpty():
            return ([])
        
        else:
            return (self.left.displayInOrder() + [self.value] + self.right.displayInOrder())
        

            
