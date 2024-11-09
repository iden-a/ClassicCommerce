'''
Order Queue - to manage incoming orders,

Use a Queue to handle the incoming orders. 
Orders are processed on a "first-come, first-served" basis, making Queue an ideal structure for this. 
New orders are added to the back of the Queue, and processing always occurs at the front.

'''

class Queue:
    def __init__(self):
        self.queue = []

    # enqueue function, adding to the end of the order 
    def addToQueue(self, order):
        self.queue.append(order)

    # dequeue function, removing an order from the top of the queue 
    def removeFromQueue(self):
        if self.isQueueEmpty(): # first we need to check if the queue is empty 
            return None
        
        return self.queue.pop(0)

    # check if queue is empty
    def isQueueEmpty(self): 
        return len(self.queue) == 0 

    # check the front of the queue
    def front(self):
        if not self.isQueueEmpty():
            return self.queue[0]
        return None

    # display the queue 
    def displayQueue(self):
        if self.isQueueEmpty():
            print("The Queue is Empty")

        else:
            for order in self.queue:
                order.displayOrderInformation()
                