class Plate:
    
    def __init__(self, ticket):
        self.order = ticket.getOrder()
        self.item = ticket.getItem()
        
    def getOrder(self):
        return self.order
    
    def getItem(self):
        return self.item

    def served(self):
        self.order.served(self.item)
