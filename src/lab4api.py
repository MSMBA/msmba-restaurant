# this is the api for the restaurant system described
# in lab 4.  to use this you need to import functions into your 
# file by using
#
# from lab4api import *

import menu
import menuItem
import order
import bill
import ticket
import plate
import csv
import time 
import sys


def show_logo(restaurant_name):
    """
    Displays restaurant name in an ascii formatted box.
    """
    stars = '*' * (len(restaurant_name)+4)
    print(stars)
    print('* ' + restaurant_name + ' *')
    print(stars)
    
# Note: eventually this could also pop up a nice colorful display
def start_meal(restaurant_name, greeting):
    """
    sets up the system for a new group of diners
    by displaying a friendly greeting.
    
    Parameters
    ----------
    restaurant_name : string
    greeting : string
        text of greeting message
    """
    show_logo(restaurant_name)
    print(greeting)
    print()
    
def end_meal(restaurant_name, message):
    """
    closes out the session for current diners.
    displays restaurant name and message.
    
    Parameters
    ----------
    restaurant_name : string
    message : string
    """
    print
    print(message)
    show_logo(restaurant_name)
    print

# this function creates a menu object from a csv file
def get_menu(file, title="Menu"):
    csvfile = open(file, "rU")
    dialect = csv.Sniffer().sniff(csvfile.read(1024))
    csvfile.seek(0)
    menuReader = csv.reader(csvfile, dialect)
    myMenu = menu.menu(title)
    for row in menuReader:
        myMenuItem = menuItem.MenuItem(row[0], float(row[1]), row[2])
        myMenu.items.append(myMenuItem)
    return myMenu

# Display a menu on the screen
def show_menu(menu):
    menu.show()

# Merge menus
def merge_menus(menu1,menu2):
    newMenu = menu.menu()
    newMenu.merge(menu1)
    newMenu.merge(menu2)
    return newMenu

# Create a new Order and return it
def create_order(waiter, table):
    return order.Order(table, waiter)

# Ask the user to choose one or more items from the 
# menu and adds them to the order
def get_choice(menu, order):
    gettingData = True 
    while gettingData:
        choice = input("Enter item number to order, (return for done): ")
        if choice == "":
            gettingData = False        # if user didn't enter anything we are done collecting numbers
        else :
            try:
                choiceInt = int(choice)
            except:
                print("The choice is not a valid number")
                continue
            if int(choice) > len(menu.getItems()) or int(choice) < 1:
                print("This item number is invalid!")
            else:
                quant = input("How many? (return for 1)")
                if quant == "":
                    quant = "1"
                try:
                    quantInt = int(quant)
                except:
                    print("The quantity has to be a number")
                    continue
                menuItem = menu.getItems()[choiceInt - 1]
                order.addItem(menuItem, quantInt)
    return order

# Print out an Order on the display
def show_order(order):
    order.show()

# Merge two orders and returns the merged order
def merge_orders(order1, order2):
    if (order1.getTable() != order2.getTable()):
        raise Exception("Tables must match")
    newOrder = order.Order(order1.getTable(), order1.getWaiter())
    newOrder.merge(order1)
    newOrder.merge(order2)
    if (order1.getWaiter() != order2.getWaiter()):
        newOrder.waiter = order1.getWaiter() + " & " + order2.getWaiter()
    return newOrder

def prepare_food(order):
    print("~~~~~~~~~~\nOrder received by kitchen\nPreparing")
    
    tickets = []
    for item, quantity in order.items.items():
        for q in range(quantity):
            tick = ticket.Ticket(order, item)
            tickets.append(tick)
            for step in range(5):
                time.sleep(.1)
                sys.stdout.write('.')
    print("\n~~~~~~~~~~\n")

    return tickets


# Pick up a new Plate of food for a given ticket
def pickup_food(ticket):
    ticket.pickedUp();
    print("Picked up:", ticket.getItem().getName())
    p = plate.Plate(ticket)
    return p 

# Serve a Plate of food, returns nothing
def serve_food(plate):
    plate.served()
    print("Served:", plate.getItem().getName())

# Creates a new bill
def new_bill():
    myBill = bill.Bill([])
    return myBill

# Add an order to a bill
def add_to_bill(bill, order):
    bill.addOrder(order)
   
# Display a bill
def show_bill(bill):
    bill.show()

# this function merges two bills and returns a NEW merged bill
def merge_bills(bill1, bill2):
    newBill = new_bill()
    newBill.merge(bill1)
    newBill.merge(bill2)
    return newBill

# Verifies a bill to make sure the bill is only paid when all orders 
# have been served
def check_bill(bill):
    return bill.check_bill();

# Complains if the bill contains an order that hasn't been served
def complain_if_bill_bad(bill):
    if (not check_bill(bill)) :
        print("ERROR: I WON'T PAY!!  I haven't gotten all my food!!\n\n")
        print("==>> You need to fix your touch screen system --")
        print("     If customers don't get their food, its going to be rejected by the restaurant owner...")
        sys.exit()

def get_amount(prompt="Enter amount:  "):
    """
    Prompts user for dollar amount and returns as float.
    
    If invalid number, negative number or no number 
    entered then prompts user to re-enter value.
    Empty response is treated as 0.
    """
    gettingData = True
    while gettingData:
        amount = input(prompt)
        if amount == "":
            amount = "0"
        try:
            amount = float(amount)
        except:
            print("Invalid entry.  ")
            continue
        if amount < 0:
            print("Amount cannot be negative.  ")
        else:
            gettingData = False
    return amount

def get_tip():
    """
    Prompts user for tip and returns tip amount.
    """
    return get_amount("Please enter the tip you want to leave: ")


# Presents the bill and collects payment
# returns payment information
# this function presents the bill and collects payment
# it returns payment information
def get_payment_type():

    paymentTypes = ["Cash", "Credit Card", "Check"]
    paymentTypeInvalid = True
    while paymentTypeInvalid:
        paymentTypeChoice = input("How would you like to pay (1)Cash,(2)Credit card or (3)Check? ")        
        try:
            paymentTypeChoiceInt = int(paymentTypeChoice)
        except:
            print("Please enter a valid payment type")
            continue
        paymentTypeInvalid = False
        return paymentTypes[paymentTypeChoiceInt - 1]

def collect_payment(paymentType, bill):    
    paymentInvalid = True
    if paymentType == "Credit Card":
        while paymentInvalid:
            print("Please provide your credit card data")
            cardNumber = input("Please enter your credit card number(4-digits): ")
            try:
                cardNumberInt = int(cardNumber)
            except:
                print("Invalid card number!")
                continue
            if cardNumberInt > 9999:
                print("The card number provided is invalid!")
                continue
            else:
                cardHolder = input("Please enter the card holder: ")
                expDate = input("Please enter the card expiration date: ")
                tip = get_tip()
                paymentInvalid = False
        print("The credit card with the number " + cardNumber + " issued to " + cardHolder + " has been charged with $" + str(round(bill.getTotal() + tip,2)))
    elif paymentType == "Cash":
        while paymentInvalid:
            tip = get_tip()
            moneyGiven = get_amount("Please enter the amount of money given in total: ")
            if moneyGiven < bill.getTotal() + tip:
                print("The amount of money given is not sufficient")
                continue
            else:
                paymentInvalid = False
                
                change = moneyGiven - (bill.getTotal() + tip)
                if float(change) < 0:
                    print("The money given is not sufficient to pay the bill and leave the tip")
                else: 
                    print("You paid your bill. Your change is $" + str(round(change,2)))
                
    elif paymentType == "Check":
        tip = get_tip()
        print("Your check with an amount of $" + str(bill.getTotal() + tip) + " will be cashed in soon")
    else:
        print("This payment type is not accepted")
        

