'''

Fulfillment Stack - to track the order fulfillment process

Last In First Out

Once an order is processed, it moves to the fulfillment stage, 
where items are packed and readied for shipment. Use a Stack to simulate this "last-in, first-out" workflow. 
This can reflect a real-world scenario where the most recently packed items might be the first ready for shipping.

'''

class Stack:
    def __init__(self):
        self.stack = []


    def addToStack(self, order):
        self.stack.append(order)

    def removeFromStack(self):
        if self.isStackEmpty():
            return None
        
        return self.stack.pop(-1)

    def isStackEmpty(self):
        return len(self.stack) == 0

    def top(self):
        if not self.isStackEmpty():
            return self.stack[-1]
        
        return None

    def displayStack(self):
        # display in backwards motion, the last element is at the top of the stack

        if self.isStackEmpty():
            print("The Stack is Empty")

        else:
            for order in reversed(self.stack):
                order.displayOrderInformation()
   

