import tkinter
from tkinter import *
from dessertshop import *


class GUI:
    def __init__(self, height, width):
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

        self.main_window = tkinter.Tk(className="Dessertshop")
        self.main_window.geometry(f"{height}x{width}")
        self.create_menu(0)
        self.create_input(6)
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
        self.conformation_button = Button(self.main_window, text="Continue", command=lambda: self.add_to_order(n))
        n -= 2
        self.conformation_button.grid(row=n, column=4, )
        n += 1

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
        real_order = Order()
        self.selected_items.append(6)
        a = str(self.selected_items[len(self.selected_items) - 2])
        while run:
            try:
                treat_type = a
                if treat_type == "1":
                    print("identified its a candy")
                    l = self.user_prompt_candy(n, a)
                    real_order.add(l)
                    return
                elif treat_type == "2":
                    # freezer.take(Cookie)
                    l = self.user_prompt_cookie(n, a)
                    real_order.add(l)
                    return
                elif treat_type == "3":
                    # freezer.take(IceCream)
                    l = self.user_prompt_ice_cream(n, a)
                    real_order.add(l)
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
                    run = False
            except IndexError:
                run = False

        return "Hello"

    def user_prompt_candy(self, n, a):
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

        self.conformation_button = Button(self.main_window, text="Continue", command=lambda: self.build_dessert_item(a))
        self.conformation_button.grid(row=n, column=4, )

    def user_prompt_cookie(self, n, a):
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

        self.conformation_button = Button(self.main_window, text="Continue", command=lambda: self.build_dessert_item(a))
        self.conformation_button.grid(row=n, column=4, )

    def user_prompt_ice_cream(self, n, a):
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

        self.conformation_button = Button(self.main_window, text="Continue", command=lambda: self.build_dessert_item(a))
        self.conformation_button.grid(row=n, column=4, )

    def build_dessert_item(self, a):
        if a == 1:
            candy = Candy(str(self.text_box.get("1.0", "end-1c")), float(self.text_box2.get("1.0", "end-1c")),
                          float(self.text_box3.get("1.0", "end-1c")))
            return candy
        elif a == 2:
            cookie = Cookie(str(self.text_box.get("1.0", "end-1c")), float(self.text_box2.get("1.0", "end-1c")),
                            float(self.text_box3.get("1.0", "end-1c")))
            return cookie


def runGUI():
    gui_window = GUI(1000, 1000)


runGUI()
