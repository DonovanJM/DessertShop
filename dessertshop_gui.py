import tkinter
from tkinter import *
from order import Order
from candy import Candy
from cookie import Cookie
from icecream import IceCream
from payment import Payment
from sundae import Sundae
import pickle


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

        self.optionmenu1 = OptionMenu(self.main_window, self.options, *self.dict1.values())
        self.optionmenu1.grid(row=n, column=0)

        self.options.trace("w", self.my_show)

        n += 2
        self.conformation_button1 = Button(self.main_window, text="Continue", command=lambda: self.add_to_order(n))
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

        self.text_box = Text(self.main_window, height=1, width=4)
        self.text_box.grid(row=n, column=0, columnspan=2, sticky="w")

        self.text_box2 = Text(self.main_window, height=1, width=8)
        self.text_box2.grid(row=n, column=1, columnspan=2, sticky="w")

        self.text_box3 = Text(self.main_window, height=1, width=8)
        self.text_box3.grid(row=n, column=2, columnspan=2, sticky="w")
        if self.conformation_button is not None:
            self.conformation_button.destroy()
        self.conformation_button = Button(self.main_window, text="Add to order",
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

        self.text_box = Text(self.main_window, height=1, width=4)
        self.text_box.grid(row=n, column=0, columnspan=2, sticky="w")

        self.text_box2 = Text(self.main_window, height=1, width=8)
        self.text_box2.grid(row=n, column=1, columnspan=2, sticky="w")

        self.text_box3 = Text(self.main_window, height=1, width=8)
        self.text_box3.grid(row=n, column=2, columnspan=2, sticky="w")
        if self.conformation_button is not None:
            self.conformation_button.destroy()
        self.conformation_button = Button(self.main_window, text="Add to order",
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

        self.text_box = Text(self.main_window, height=1, width=4)
        self.text_box.grid(row=n, column=0, columnspan=2, sticky="w")

        self.text_box2 = Text(self.main_window, height=1, width=8)
        self.text_box2.grid(row=n, column=1, columnspan=2, sticky="w")

        self.text_box3 = Text(self.main_window, height=1, width=8)
        self.text_box3.grid(row=n, column=2, columnspan=2, sticky="w")
        print("making button")
        if self.conformation_button is not None:
            self.conformation_button.destroy()
        self.conformation_button = Button(self.main_window, text="Add to order",
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

        self.text_box = Text(self.main_window, height=1, width=4)
        self.text_box.grid(row=n, column=0, columnspan=2, sticky="w")

        self.text_box2 = Text(self.main_window, height=1, width=8)
        self.text_box2.grid(row=n, column=1, columnspan=2, sticky="w")

        self.text_box3 = Text(self.main_window, height=1, width=8)
        self.text_box3.grid(row=n, column=2, columnspan=2, sticky="w")

        self.text_box4 = Text(self.main_window, height=1, width=8)
        self.text_box4.grid(row=n, column=3, columnspan=2, sticky="w")

        self.text_box5 = Text(self.main_window, height=1, width=8)
        self.text_box5.grid(row=n, column=4, columnspan=2, sticky="w")
        if self.conformation_button is not None:
            self.conformation_button.destroy()
        self.conformation_button = Button(self.main_window, text="Add to order",
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

        self.text_box = Text(self.main_window, height=1, width=25)
        self.text_box.grid(row=n + 6, column=1, columnspan=3, sticky="w")

        self.label1 = tkinter.Label(self.main_window, text="What form of payment will be used? (Cash, Card, Phone):")
        self.label1.grid(row=n + 7, column=0, sticky="w")

        self.dict1 = {1: "Cash", 2: "Card", 3: "Phone"}
        self.options = tkinter.StringVar(self.main_window)
        self.options.set(self.dict1[1])

        self.optionmenu1 = OptionMenu(self.main_window, self.options, *self.dict1.values())
        self.optionmenu1.grid(row=n + 7, column=1)

        self.options.trace("w", self.my_show)

        n += 2
        self.conformation_button1 = Button(self.main_window, text="Print Receipt", command=lambda: self.print_receipt())
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


def runGUI():
    gui_window = GUI(1000, 1000)


runGUI()
