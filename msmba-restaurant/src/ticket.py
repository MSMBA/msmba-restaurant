class Ticket:
    
    def __init__(self, order, item):
        self.order = order
        self.item = item
        
    def getOrder(self):
        return self.order
    
    def getItem(self):
        return self.item

    def pickedUp(self):
        self.order.pickedUp(self.item)
