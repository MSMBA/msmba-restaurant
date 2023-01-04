# this is a demo of the api
from lab4api import *

# demo for mcdonald's
start_meal("McDonald's", "Welcome to McDonald's")

myMenu = get_menu("msmba-restaurant/menu.csv","Our Menu")
show_menu(myMenu)

myOrder = create_order("John", 5)
get_choice(myMenu, myOrder)
show_order(myOrder)

tickets = prepare_food(myOrder)
for ticket in tickets:
    plate = pickup_food(ticket)
    serve_food(plate)

myBill = new_bill()
myBill.addOrder(myOrder)
show_bill(myBill)
complain_if_bill_bad(myBill)

myPaymentType = get_payment_type()
collect_payment(myPaymentType, myBill)

end_meal("McDonald's", "Have a nice day!")
