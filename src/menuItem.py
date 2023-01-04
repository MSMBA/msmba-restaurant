class MenuItem(object):
    
# Constructor which initializes name, price and type of the item
    def __init__(self,name,price,type):
        self.name = name
        self.price = price
        self.type = type

# Returns the name    
    def getName(self):
        return self.name

# Returns the price
    def getPrice(self):
        return self.price

# Return the type
    def getType(self):
        return self.type
        