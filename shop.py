####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "Cupcake Shop"
signature_flavors = ["chocolate chip","strawberry cheesecake","oreo","cinnamon"]
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    # your code goes here!
    for item in menu:
        print (item, menu[item])


def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    # your code goes here!
    for flavor in original_flavors:
        print (flavor)


def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    # your code goes here!
    for flavor in signature_flavors:
        print (flavor)

def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    # your code goes here!
    if len(order_list) == 0:
        return False
    else:
        return True


def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    # your code goes here!

    request = str(input("What is your order? Type Exit when you are done ordering."))

    while request.lower() != "exit":
        order_list.append(request)
        print (order_list)
        request = input("What is your order? Type Exit when you are done ordering.")
    return order_list

def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    # your code goes here!
    if total >= 5:
        return ("Your order is eligible for credit card payment")
    else:
        return ("Your order is NOT eligible for credit card payment")


def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    # your code goes here!
    for order in order_list:
        if order in original_flavors:
            total += 2
        elif order in signature_flavors:
            total += 2.750
    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    # your code goes here!
    for order in order_list:
        print (order)
    total_cost = get_total_price(order_list)
    credit_card = accept_credit_card(total_cost)
    print ("Total cost of your order is " + str(total_cost))
    print (credit_card)
    print (cupcake_shop_name)

