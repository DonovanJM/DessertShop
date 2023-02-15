from order import Order
from freeze import Freezer
from candy import Candy
from cookie import Cookie
from icecream import IceCream
from sundae import Sundae
from customer import Customer
import pickle


def check_customer(customer_db, real_order):
    current_name = real_order.customer_name
    if current_name not in customer_db.keys():
        real_customer = Customer(current_name)
        customer_db[current_name] = real_customer
        real_customer.add2history(real_order)
        the_real_customer = real_customer
    else:
        old_customer = customer_db[current_name]
        old_customer.add2history(real_order)
        customer_db[current_name] = old_customer
        the_real_customer = old_customer

    pickle_out = open("customer.pickle", "wb")
    pickle.dump(customer_db, pickle_out)
    pickle_out.close()
    return the_real_customer


def main_menu(freezer):
    real_order = Order()
    try:
        customer_db = pickle.load(open("customer.pickle", "rb"))
    except EOFError:
        customer_db = {}
    i = 0
    while i == 0:
        treat_type = input("1: Candy\n2: Cookie\n3: Ice Cream\n4: Sundae\nWhat would you like to add to the order? "
                           "(1-4, Enter for done):")
        if treat_type == "1":
            a = user_prompt_candy()
            real_order.add(a)
        elif treat_type == "2":
            # freezer.take(Cookie)
            a = user_prompt_cookie()
            real_order.add(a)
        elif treat_type == "3":
            # freezer.take(IceCream)
            a = user_prompt_icecream()
            real_order.add(a)
        elif treat_type == "4":
            # freezer.take(Sundae)
            a = user_prompt_sundae()
            real_order.add(a)
        elif treat_type == "":
            i = 1
        else:
            print("Invalid dessert type, please enter 1-4.")
    # real_order.combine_order()
    real_order.sort_order()
    real_order.__str__()
    a = check_customer(customer_db, real_order)
    a.customer_information()

    if input("Would you like to start another order?").lower() == "y":
        main_menu(freezer)


def user_prompt_candy():
    candy_type = str(input("Enter the type of candy: "))
    candy_weight = input("Enter the quantity purchased: ")
    try:
        candy_weight = float(candy_weight)
    except ValueError:
        print(f"You entered {candy_weight}, which is not a number. Please try again.")
        user_prompt_candy()
        return
    price_per_pound = input("Enter the price per pound: ")
    try:
        price_per_pound = float(price_per_pound)
    except ValueError:
        print(f"You entered {price_per_pound}, which is not a number. Please try again.")
        user_prompt_candy()
        return
    a_candy = Candy(candy_type, candy_weight, price_per_pound)
    return a_candy


def user_prompt_cookie():
    cookie_type = str(input("Enter the type of Cookie: "))
    cookie_quantity = input("Enter the quantity purchased: ")
    try:
        cookie_quantity = float(cookie_quantity)
    except ValueError:
        print(f"You entered {cookie_quantity}, which is not a number. Please try again.")
        user_prompt_cookie()
        return
    price_per_dozen = input("Enter the price per dozen: ")
    try:
        price_per_dozen = float(price_per_dozen)
    except ValueError:
        print(f"You entered {price_per_dozen}, which is not a number. Please try again.")
        user_prompt_cookie()
        return
    a_cookie = Cookie(cookie_type, cookie_quantity, price_per_dozen)
    return a_cookie


def user_prompt_icecream():
    ice_cream_type = str(input("Enter the type of ice cream: "))
    scoop_count = input("Enter the number of scoops: ")
    try:
        scoop_count = float(scoop_count)
    except ValueError:
        print(f"You entered {scoop_count}, which is not a number. Please try again.")
        user_prompt_icecream()
        return
    price_per_scoop = input("Enter the price per scoop: ")
    try:
        price_per_scoop = float(price_per_scoop)
    except ValueError:
        print(f"You entered {price_per_scoop}, which is not a number. Please try again.")
        user_prompt_icecream()
        return
    a_ice_cream = IceCream(ice_cream_type, scoop_count, price_per_scoop)
    return a_ice_cream


def user_prompt_sundae():
    ice_cream_type = str(input("Enter the type of ice cream: "))
    scoop_count = input("Enter the number of scoops: ")
    try:
        scoop_count = float(scoop_count)
    except ValueError:
        print(f"You entered {scoop_count}, which is not a number. Please try again.")
        user_prompt_sundae()
        return
    price_per_scoop = input("Enter the price per scoop: ")
    try:
        price_per_scoop = float(price_per_scoop)
    except ValueError:
        print(f"You entered {price_per_scoop}, which is not a number. Please try again.")
        user_prompt_sundae()
        return
    topping = str(input("Enter the topping: "))
    topping_price = (input("Enter the price for the topping: "))
    try:
        topping_price = float(topping_price)
    except ValueError:
        print(f"You entered {topping_price}, which is not a number. Please try again.")
        user_prompt_sundae()
        return
    a_sundae = Sundae(ice_cream_type, scoop_count, price_per_scoop, topping,
                      topping_price)
    return a_sundae


def main():
    # cookie = Cookie()
    # icecream = IceCream()
    # sundae = Sundae()
    freezer = Freezer()
    # freezer.put(cookie)
    # freezer.put(icecream)
    # freezer.put(sundae)
    main_menu(freezer)


if __name__ == "__main__":
    main()
