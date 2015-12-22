import time
import sys

class Bill:
    
    
    def __init__(self, orders, taxrate = 0.05):
        self.orders = orders
        self.taxrate = taxrate

    def addOrder(self,order):
        self.orders.append(order)

    def getOrders(self):
        return self.orders
    
    def getSubTotal(self):
        total = 0
        for order in self.getOrders():
            total += order.getTotal()
        return total
    
    def getTax(self):
        return self.taxrate * self.getSubTotal()
    
    def getTotal(self):
        return self.getSubTotal() + self.getTax()
    
    def show(self):
        print "\n##########"
        print "Bill calculated at " + time.strftime("%a, %d %b %Y %H:%M", time.localtime())
        print "Goods and Services: "
        for order in self.getOrders():
            print "-----"
            order.showForBill()
        print "========="
        subtotal = self.getSubTotal()
        tax = self.getTax()
        total = self.getTotal()
        print ("%-60s" % "Pre-tax:")  + "$" + str(round(subtotal,2))    
        print ("%-60s" % "Tax:")   + "$" + str(round(tax,2))           
        print ("%-60s" % "Total:")  + "$" + str(round(total,2))    
        print "##########\n"
    
    def merge(self,bill):
        # According to test data available online the fastest method to merge two lists
        self.orders.append('')  
        self.orders[-1:] = bill.getOrders()
            
    # Verifies a bill to make sure the bill is only paid when all orders 
    # have been served
    def check_bill(self):
        for order in self.getOrders():
            try:
                order.checkPickUps()
            except:
                return False
            try:
                order.checkServed() 
            except:
                return False
        return True