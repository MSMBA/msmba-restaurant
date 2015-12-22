class Order:
    
    def __init__(self, table, waiter):
        self.table = table
        self.waiter = waiter
        self.items = {}     #map MenuItem -> quantity
        self.picked_up = {} #map MenuItem -> quantity
        self.served_up = {} #map MenuItem -> quantity
        
    def addItem(self, menuItem, quantity):
        if (self.items.has_key(menuItem)):
            quantity += self.items[menuItem]
        self.items[menuItem] = quantity
    
    def getTable(self):
        return self.table
    
    def getWaiter(self):
        return self.waiter
    
    def getItems(self):
        return self.items
    
    def getTotal(self):
        total = 0
        for menuItem, quantity in self.items.iteritems():
            total += quantity * menuItem.getPrice()
        return total
    
    def pickedUp(self, item):
        if (item in self.picked_up):
            self.picked_up[item] = self.picked_up[item] + 1
        else:
            self.picked_up[item] = 1
        
    def served(self, item):
        if (item in self.served_up):
            self.served_up[item] = self.served_up[item] + 1
        else:
            self.served_up[item] = 1
  
    def checkPickUps(self):
        for item, quantity in self.items.iteritems():
            if(self.picked_up.has_key(item)):
                if quantity != self.picked_up[item]:
                    raise Exception("Order for " + str(quantity) + " only picked up " + str(self.picked_up[item]))
            else:
                raise Exception("Order for " + str(quantity) + " but never picked up any")

    def checkServed(self):
        for item, quantity in self.items.iteritems():
            if(self.served_up.has_key(item)):
                if quantity != self.served_up[item]:
                    raise Exception("Order for " + str(quantity) + " only picked up " + str(self.served_up[item]))
            else:
                raise Exception("Order for " + str(quantity) + " but never picked up any")
                        
    def show(self):
        print "\n*****"
        print "Order taken by server", self.waiter, "for table", self.table
        for menuItem, quantity in self.items.iteritems():
            print ("%-3s" % str(quantity)) + "\t@\t" + ("%-40s" % menuItem.getName())
        print "Order Total: $", self.getTotal()
        print "*****\n"

    def showForBill(self):
        print "Order taken by server", self.waiter, " for table", self.table
        for menuItem, quantity in self.items.iteritems():
            print ("%-3s" % str(quantity)) + "\t" + ("%-40s" % menuItem.getName()) + " @ " + ("%-6s" %  ("$"+ str(menuItem.getPrice()))) + " : " + "$" + str(menuItem.getPrice() * quantity)
        
    
    def merge(self,order):
        self.table = order.table
        self.waiter = order.waiter
        
        for menuItem, quantity in order.items.iteritems():
            if(self.items.has_key(menuItem)):
                self.items[menuItem] = self.items[menuItem] + quantity
            else:
                self.items[menuItem] = quantity
                
        for menuItem, quantity in order.picked_up.iteritems():
            if(self.picked_up.has_key(menuItem)):
                self.picked_up[menuItem] = self.picked_up[menuItem] + quantity
            else:
                self.picked_up[menuItem] = quantity

        for menuItem, quantity in order.served_up.iteritems():
            if(self.served_up.has_key(menuItem)):
                self.served_up[menuItem] = self.served_up[menuItem] + quantity
            else:
                self.served_up[menuItem] = quantity                