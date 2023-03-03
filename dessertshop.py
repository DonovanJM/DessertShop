from order import Order
from candy import Candy
from cookie import Cookie
from icecream import IceCream
from payment import Payment
from sundae import Sundae
from customer import Customer
import pickle
import argparse
from dessertshop_gui import runGUI
import tkinter


class GUI:
    def __init__(self, height, width):
        self.conformation_button1 = None
        self.order = None
        self.a = None
        self.text_box4 = None
        self.text_box5 = None
        self.text_box3 = None
        self.text_box2 = None
        self.conformation_button = None
        self.i = None
        self.text_box = None
        self.options = None
        self.optionmenu1 = None
        self.prompt = None
        self.label1 = None
        self.blank = None
        self.dict1 = None
        self.selected_items = []
        self.dessert_item = None

        self.main_window = tkinter.Tk(className="Dessert shop")
        self.main_window.geometry(f"{height}x{width}")
        self.create_menu(0)
        self.create_input(6)

        print(self.order)

        tkinter.mainloop()

    def create_menu(self, n):
        self.blank = tkinter.Label(self.main_window, text="What would you like to do?", padx=40)
        self.blank.grid(row=n, column=0, columnspan=20, sticky="w")
        n += 1
        self.label1 = tkinter.Label(self.main_window, text="1: Candy")
        self.label1.grid(row=n, column=0, sticky="w")
        n += 1
        self.label1 = tkinter.Label(self.main_window, text="2: Cookie")
        self.label1.grid(row=n, column=0, sticky="w")
        n += 1
        self.label1 = tkinter.Label(self.main_window, text="3: Ice Cream")
        self.label1.grid(row=n, column=0, sticky="w")
        n += 1
        self.label1 = tkinter.Label(self.main_window, text="4: Sundae")
        self.label1.grid(row=n, column=0, sticky="w")
        n += 1
        self.label1 = tkinter.Label(self.main_window, text="5: Admin Module")
        self.label1.grid(row=n, column=0, sticky="w")

    def create_input(self, n):
        self.label1 = tkinter.Label(self.main_window, text="Dessert type:")
        self.label1.grid(row=n, column=0, sticky="w")
        n += 1

        self.dict1 = {1: "Candy", 2: "Cookie", 3: "Ice Cream", 4: "Sundae", 5: "Admin Module", 6: "None"}
        self.options = tkinter.StringVar(self.main_window)
        self.options.set(self.dict1[6])

        self.optionmenu1 = tkinter.OptionMenu(self.main_window, self.options, *self.dict1.values())
        self.optionmenu1.grid(row=n, column=0)

        self.options.trace("w", self.my_show)

        n += 2
        self.conformation_button1 = tkinter.Button(self.main_window, text="Continue", command=lambda: self.add_to_order(n))
        n -= 2
        self.conformation_button1.grid(row=n, column=4, )
        n += 1
        return

    def my_show(self, *args):
        for self.i, j in self.dict1.items():
            if j == self.options.get():
                self.selected_items.append(self.i)

    def retrieve_input(self):
        return self.text_box.get("1.0", "end-1c")

    def add_to_order(self, n):
        print("success")

        try:
            customer_db = pickle.load(open("customer.pickle", "rb"))
        except EOFError:
            customer_db = {}
        run = True
        self.order = Order()
        self.selected_items.insert(0, "6")
        self.a = str(self.selected_items[len(self.selected_items) - 1])
        while run:
            try:
                if self.a == "1":
                    print("identified its a candy")
                    self.user_prompt_candy(n)
                    self.order.add(self.dessert_item)
                    return
                elif self.a == "2":
                    # freezer.take(Cookie)
                    self.user_prompt_cookie(n)
                    self.order.add(self.dessert_item)
                    return
                elif self.a == "3":
                    # freezer.take(IceCream)
                    self.user_prompt_ice_cream(n)
                    self.order.add(self.dessert_item)
                    return
                elif self.a == "4":
                    # freezer.take(Sundae)
                    self.user_prompt_sundae(n)
                    self.order.add(self.dessert_item)
                    return
                elif self.a == "5":
                    admin_prompt(customer_db)
                elif self.a == "":
                    if len(self.order.order) == 0:
                        return
                    run = False
                elif self.a == "6":
                    print("Identified their is nothing")
                    self.dessert_item = None
                    self.optionmenu1.configure(state="disabled")
                    if self.conformation_button1 is not None:
                        self.conformation_button1.configure(state="disabled")
                    if self.conformation_button is not None:
                        self.conformation_button.configure(state="disabled")
                    if self.text_box is not None:
                        self.text_box.configure(state="disabled")
                    if self.text_box2 is not None:
                        self.text_box2.configure(state="disabled")
                    if self.text_box3 is not None:
                        self.text_box3.configure(state="disabled")
                    if self.text_box4 is not None:
                        self.text_box4.configure(state="disabled")
                    if self.text_box5 is not None:
                        self.text_box5.configure(state="disabled")

                    self.print_order(n)
                    return
                else:
                    print("Invalid dessert type, please enter 1-4.")
                    run = False
            except IndexError:
                run = False
        return

    def user_prompt_candy(self, n):
        print("Went into candy function")
        self.label1 = tkinter.Label(self.main_window, text="Enter the type of candy:")
        self.label1.grid(row=n, column=0, sticky="w")
        self.label1 = tkinter.Label(self.main_window, text="Enter the amount (pounds):")
        self.label1.grid(row=n, column=1, sticky="w")
        self.label1 = tkinter.Label(self.main_window, text="Enter the price per pound:")
        self.label1.grid(row=n, column=2, sticky="w")
        n += 1

        self.text_box = tkinter.Text(self.main_window, height=1, width=4)
        self.text_box.grid(row=n, column=0, columnspan=2, sticky="w")

        self.text_box2 = tkinter.Text(self.main_window, height=1, width=8)
        self.text_box2.grid(row=n, column=1, columnspan=2, sticky="w")

        self.text_box3 = tkinter.Text(self.main_window, height=1, width=8)
        self.text_box3.grid(row=n, column=2, columnspan=2, sticky="w")
        if self.conformation_button is not None:
            self.conformation_button.destroy()
        self.conformation_button = tkinter.Button(self.main_window, text="Add to order",
                                                  command=lambda: self.build_dessert_item())
        self.conformation_button.grid(row=n, column=4, )
        return

    def user_prompt_cookie(self, n):
        print("Went into cookie function")
        self.label1 = tkinter.Label(self.main_window, text="Enter the type of cookie:")
        self.label1.grid(row=n, column=0, sticky="w")
        self.label1 = tkinter.Label(self.main_window, text="Enter the amount of cookies:")
        self.label1.grid(row=n, column=1, sticky="w")
        self.label1 = tkinter.Label(self.main_window, text="Enter the price per dozen:")
        self.label1.grid(row=n, column=2, sticky="w")
        n += 1

        self.text_box = tkinter.Text(self.main_window, height=1, width=4)
        self.text_box.grid(row=n, column=0, columnspan=2, sticky="w")

        self.text_box2 = tkinter.Text(self.main_window, height=1, width=8)
        self.text_box2.grid(row=n, column=1, columnspan=2, sticky="w")

        self.text_box3 = tkinter.Text(self.main_window, height=1, width=8)
        self.text_box3.grid(row=n, column=2, columnspan=2, sticky="w")
        if self.conformation_button is not None:
            self.conformation_button.destroy()
        self.conformation_button = tkinter.Button(self.main_window, text="Add to order",
                                                  command=lambda: self.build_dessert_item())
        self.conformation_button.grid(row=n, column=4, )
        return

    def user_prompt_ice_cream(self, n):
        print("Went into ice cream function")
        self.label1 = tkinter.Label(self.main_window, text="Enter the type of ice cream:")
        self.label1.grid(row=n, column=0, sticky="w")
        self.label1 = tkinter.Label(self.main_window, text="Enter the amount of scoops:")
        self.label1.grid(row=n, column=1, sticky="w")
        self.label1 = tkinter.Label(self.main_window, text="Enter the price per scoop:")
        self.label1.grid(row=n, column=2, sticky="w")
        n += 1

        self.text_box = tkinter.Text(self.main_window, height=1, width=4)
        self.text_box.grid(row=n, column=0, columnspan=2, sticky="w")

        self.text_box2 = tkinter.Text(self.main_window, height=1, width=8)
        self.text_box2.grid(row=n, column=1, columnspan=2, sticky="w")

        self.text_box3 = tkinter.Text(self.main_window, height=1, width=8)
        self.text_box3.grid(row=n, column=2, columnspan=2, sticky="w")
        print("making button")
        if self.conformation_button is not None:
            self.conformation_button.destroy()
        self.conformation_button = tkinter.Button(self.main_window, text="Add to order",
                                                  command=lambda: [self.build_dessert_item(), print("Should work")])
        self.conformation_button.grid(row=n, column=4, )
        print("Made button")
        return

    def user_prompt_sundae(self, n):
        print("Went into ice cream function")
        self.label1 = tkinter.Label(self.main_window, text="Enter the type of ice cream:")
        self.label1.grid(row=n, column=0, sticky="w")
        self.label1 = tkinter.Label(self.main_window, text="Enter the amount of scoops:")
        self.label1.grid(row=n, column=1, sticky="w")
        self.label1 = tkinter.Label(self.main_window, text="Enter the price per scoop:")
        self.label1.grid(row=n, column=2, sticky="w")
        self.label1 = tkinter.Label(self.main_window, text="Enter the topping:")
        self.label1.grid(row=n, column=3, sticky="w")
        self.label1 = tkinter.Label(self.main_window, text="Enter the topping price:")
        self.label1.grid(row=n, column=4, sticky="w")
        n += 1

        self.text_box = tkinter.Text(self.main_window, height=1, width=4)
        self.text_box.grid(row=n, column=0, columnspan=2, sticky="w")

        self.text_box2 = tkinter.Text(self.main_window, height=1, width=8)
        self.text_box2.grid(row=n, column=1, columnspan=2, sticky="w")

        self.text_box3 = tkinter.Text(self.main_window, height=1, width=8)
        self.text_box3.grid(row=n, column=2, columnspan=2, sticky="w")

        self.text_box4 = tkinter.Text(self.main_window, height=1, width=8)
        self.text_box4.grid(row=n, column=3, columnspan=2, sticky="w")

        self.text_box5 = tkinter.Text(self.main_window, height=1, width=8)
        self.text_box5.grid(row=n, column=4, columnspan=2, sticky="w")
        if self.conformation_button is not None:
            self.conformation_button.destroy()
        self.conformation_button = tkinter.Button(self.main_window, text="Add to order",
                                                  command=lambda: self.build_dessert_item())
        self.conformation_button.grid(row=n, column=5, )
        return

    def build_dessert_item(self):
        print("went into build dessert")
        print(self.a)
        if self.a == "1":
            print("building dessert")
            self.dessert_item = Candy(str(self.text_box.get("1.0", "end-1c")),
                                      float(self.text_box2.get("1.0", "end-1c")),
                                      float(self.text_box3.get("1.0", "end-1c")))
            print(self.dessert_item)

        elif self.a == "2":
            print("building dessert")
            self.dessert_item = Cookie(str(self.text_box.get("1.0", "end-1c")),
                                       float(self.text_box2.get("1.0", "end-1c")),
                                       float(self.text_box3.get("1.0", "end-1c")))
            print(self.dessert_item)

        elif self.a == "3":
            print("building dessert")
            self.dessert_item = IceCream(str(self.text_box.get("1.0", "end-1c")),
                                         float(self.text_box2.get("1.0", "end-1c")),
                                         float(self.text_box3.get("1.0", "end-1c")))
            print(self.dessert_item)

        elif self.a == "4":
            print("building dessert")
            self.dessert_item = Sundae(str(self.text_box.get("1.0", "end-1c")),
                                       float(self.text_box2.get("1.0", "end-1c")),
                                       float(self.text_box3.get("1.0", "end-1c")),
                                       str(self.text_box4.get("1.0", "end-1c")),
                                       float(self.text_box5.get("1.0", "end-1c")))
            print(self.dessert_item)
        return

    def print_order(self, n):
        print("Went into print order function")
        self.label1 = tkinter.Label(self.main_window, text="Enter the customer name:")
        self.label1.grid(row=n + 6, column=0, sticky="w")

        self.text_box = tkinter.Text(self.main_window, height=1, width=25)
        self.text_box.grid(row=n + 6, column=1, columnspan=3, sticky="w")

        self.label1 = tkinter.Label(self.main_window, text="What form of payment will be used? (Cash, Card, Phone):")
        self.label1.grid(row=n + 7, column=0, sticky="w")

        self.dict1 = {1: "Cash", 2: "Card", 3: "Phone"}
        self.options = tkinter.StringVar(self.main_window)
        self.options.set(self.dict1[1])

        self.optionmenu1 = tkinter.OptionMenu(self.main_window, self.options, *self.dict1.values())
        self.optionmenu1.grid(row=n + 7, column=1)

        self.options.trace("w", self.my_show)

        n += 2
        self.conformation_button1 = tkinter.Button(self.main_window, text="Print Receipt", command=lambda: self.print_receipt())
        n -= 2
        self.conformation_button1.grid(row=n + 7, column=4, )

    def print_receipt(self):
        self.selected_items.insert(0, "1")
        self.a = str(self.selected_items[len(self.selected_items) - 1])
        if self.a == "1":
            self.order.pay_type = Payment.pay_type.CASH
        elif self.a == "2":
            self.order.pay_type = Payment.pay_type.CARD
        elif self.a == "3":
            self.order.pay_type = Payment.pay_type.PHONE
        self.order.customer_name = self.text_box.get("1.0", "end-1c")
        print("------------Receipt---------------")
        for i in range(len(self.order.order)):
            print(self.order.order[i])
        print("------------------------------------------------------")
        print(f"Total items in the order: {self.order.item_count()}")
        order_sub = "Order Subtotals:|"
        order_total = "Order Total:"
        order_num = f"${self.order.order_cost():0.2f}"
        this_string = f"{order_sub:26}"
        this_string += f"{order_num:24}"
        this_string += f"[Tax: ${self.order.order_tax():0.2f}]"
        print(f"{this_string}")
        that_string = f"{order_total:50}"
        x = self.order.order_cost() + self.order.order_tax()
        that_string += f"${x:0.2f}"
        print(that_string)
        print("------------------------------------------------------")
        print(f"Paid with {self.order.pay_type.value}")
        print("-------------------------------------------------------")


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
        searched_customer = input("Enter the name of the customer:\n")
        try:
            count = 1
            current_customer = customer_db[searched_customer]
            print(f"Customer Name: {current_customer.customer_name}           Customer ID: "
                  f"{current_customer.customer_id}\n------------------------------------------------------------------")
            for i in current_customer.order_history:
                print(f"Order #: {count}")
                count += 1
                print("----------------------------------Receipt--------------------------")
                for j in range(len(i.order)):
                    current_item = i.order[j]
                    if type(current_item) == Candy:
                        print(f"{current_item.name} ({current_item.packaging}) {current_item.candy_weight:0.2f} lbs. @ "
                              f"${current_item.price_per_pound:0.2f}/lb.: ${current_item.calculate_cost():0.2f} [Tax: $"
                              f"{current_item.calculate_tax():0.2f}]")
                    elif type(current_item) == Cookie:
                        print(f"{current_item.name} ({current_item.packaging}) {current_item.cookie_quantity} cookies "
                              f"@ ${current_item.price_per_dozen:0.2f}/dozen: ${current_item.calculate_cost():0.2f} "
                              f"[Tax: ${current_item.calculate_tax():0.2f}]")
                    elif type(current_item) == IceCream:
                        print(
                            f"{current_item.name} Ice Cream ({current_item.packaging}) {current_item.scoop_count} "
                            f"scoops "
                            f"@ ${current_item.price_per_scoop}/scoop: ${current_item.calculate_cost():0.2f} [Tax: "
                            f"${current_item.calculate_tax():0.2f}]")
                    elif type(current_item) == Sundae:
                        print(
                            f"{current_item.name} Ice Cream ({current_item.packaging}) {current_item.scoop_count} "
                            f"scoops "
                            f"@ ${current_item.price_per_scoop}/scoop: ${current_item.calculate_cost():0.2f} [Tax: "
                            f"${current_item.calculate_tax():0.2f}]\n{current_item.topping_name} @ "
                            f"${current_item.topping_price:0.2f}")
                print("----------------------------------------------------------------------")
                print(f"Total items in the order: {i.item_count()}")
                order_sub = "Order Subtotals: "
                order_total = "Order Total: "
                order_num = f"${i.order_cost():0.2f}"
                this_string = f"{order_sub}"
                this_string += f"{order_num}"
                this_string += f" [Tax: ${i.order_tax():0.2f}]"
                print(f"{this_string}")
                that_string = f"{order_total}"
                x = i.order_cost() + i.order_tax()
                that_string += f"${x:0.2f}"
                print(that_string)
                print("---------------------------------------------------------------------------")
                print(f"Paid for with {i.pay_type.value}.\n")
        except KeyError:
            print("Could not find customer")
            admin_prompt(customer_db)
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
    parser = argparse.ArgumentParser()
    parser.add_argument("-g", "--gui", action="store_true")
    args = parser.parse_args()
    print(args)
    if str(args) == "Namespace(gui=True)":
        runGUI()
    else:
        main_menu()
    # cookie = Cookie()
    # icecream = IceCream()
    # sundae = Sundae()
    # freezer = Freezer()
    # freezer.put(cookie)
    # freezer.put(icecream)
    # freezer.put(sundae)


if __name__ == "__main__":
    main()


def runGUI():
    gui_window = GUI(1000, 1000)
