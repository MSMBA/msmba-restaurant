class menu:

    def __init__(self,title="Menu"):
        self.title = title
        self.items = []
    
# Displays all menu items in a user friendly way        
    def show(self):
        print "   " + self.title
        print "   " + "-" * len(self.title)
        i = 1
        for item in self.items:
            print ("%-2s" % str(i)) + " " + ("%-40s" % item.getName()) + " $" + str(item.getPrice())
            i = i + 1

# Returns the title    
    def getTitle(self):
        return self.title

# Return all menu items            
    def getItems(self):
        return self.items

# Merge menu
    def merge(self,menu):
        for item in menu.getItems():
            if (item not in self.items):
                self.items.append(item)
            
                
                
            