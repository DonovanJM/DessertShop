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


def main_menu():
    real_order = Order()
    try:
        customer_db = pickle.load(open("customer.pickle", "rb"))
    except EOFError:
        customer_db = {}
    run = True
    while run:
        treat_type = input("1: Candy\n2: Cookie\n3: Ice Cream\n4: Sundae\n5: Admin Module\n"
                           "What would you like to add to the order? "
                           "(1-5, Enter for done):")
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
        elif treat_type == "5":
            admin_prompt(customer_db)
        elif treat_type == "":
            if len(real_order.order) == 0:
                return
            run = False
        else:
            print("Invalid dessert type, please enter 1-4.")
    # real_order.combine_order()
    real_order.sort_order()
    real_order.__str__()
    check_customer(customer_db, real_order).__str__()

    if input("Press y and Enter to start a new order").lower() == "y":
        main_menu()


def user_prompt_candy():
    print()
    candy_type = str(input("Enter the type of candy: "))
    print()
    candy_weight = input("Enter the quantity purchased: ")
    try:
        candy_weight = float(candy_weight)
    except ValueError:
        print(f"You entered {candy_weight}, which is not a number. Please try again.")
        user_prompt_candy()
        return
    print()
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
    print()
    cookie_type = str(input("Enter the type of Cookie: "))
    print()
    cookie_quantity = input("Enter the quantity purchased: ")
    try:
        cookie_quantity = float(cookie_quantity)
    except ValueError:
        print(f"You entered {cookie_quantity}, which is not a number. Please try again.")
        user_prompt_cookie()
        return
    print()
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
    print()
    ice_cream_type = str(input("Enter the type of ice cream: "))
    print()
    scoop_count = input("Enter the number of scoops: ")
    try:
        scoop_count = float(scoop_count)
    except ValueError:
        print(f"You entered {scoop_count}, which is not a number. Please try again.")
        user_prompt_icecream()
        return
    print()
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
    print()
    ice_cream_type = str(input("Enter the type of ice cream: "))
    print()
    scoop_count = input("Enter the number of scoops: ")
    try:
        scoop_count = float(scoop_count)
    except ValueError:
        print(f"You entered {scoop_count}, which is not a number. Please try again.")
        user_prompt_sundae()
        return
    print()
    price_per_scoop = input("Enter the price per scoop: ")
    try:
        price_per_scoop = float(price_per_scoop)
    except ValueError:
        print(f"You entered {price_per_scoop}, which is not a number. Please try again.")
        user_prompt_sundae()
        return
    print()
    topping = str(input("Enter the topping: "))
    print()
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


def admin_prompt(customer_db):
    print()
    a = input("1: Shop Customer List\n2: Customer Order History\n3: Best Customer\n4: Exit Admin Module\n"
              "What would you like to do? (1-4): ")
    if a == "1":
        for i in customer_db:
            customer_db[i].__str__()
        admin_prompt(customer_db)
    elif a == "2":
        searched_customer = input("Enter the name of the customer: ")
        current_customer = customer_db[searched_customer]
        count = 1
        for i in current_customer.order_history:
            print(f"Customer Name: {current_customer.customer_name}           Customer ID: "
                  f"{current_customer.customer_id}\n"
                  f"------------------------------------------------------------------\n"
                  f"Order #: {count}")
            print("------------Receipt---------------")
            for j in range(len(i.order)):
                print(i.order[j])
            print("------------------------------------------------------")
            print(f"Total items in the order: {i.item_count()}")
            order_sub = "Order Subtotals:|"
            order_total = "Order Total:"
            order_num = f"${i.order_cost():0.2f}"
            this_string = f"{order_sub:26}"
            this_string += f"{order_num:24}"
            this_string += f"[Tax: ${i.order_tax():0.2f}]"
            print(f"{this_string}")
            that_string = f"{order_total:50}"
            x = i.order_cost() + i.order_tax()
            that_string += f"${x:0.2f}"
            print(that_string)
            print("------------------------------------------------------")
            print(f"Paid with {i.pay_type.value}.")
            print("------------------------------------------------------")
        admin_prompt(customer_db)
    elif a == "3":
        biggest = 0
        best_customer = None
        for i in customer_db:
            current_customer_history_length = len(customer_db[i].order_history)
            if current_customer_history_length > biggest:
                biggest = current_customer_history_length
                best_customer = customer_db[i]
        print('--------------------------------------------------------------')
        print(f"The Dessert Shop's most valued customer is: {best_customer.customer_name}")
        print("--------------------------------------------------------------")
        admin_prompt(customer_db)
    elif a == "4":
        print()
        main_menu()


def main():
    # cookie = Cookie()
    # icecream = IceCream()
    # sundae = Sundae()
    #freezer = Freezer()
    # freezer.put(cookie)
    # freezer.put(icecream)
    # freezer.put(sundae)
    main_menu()


if __name__ == "__main__":
    main()
