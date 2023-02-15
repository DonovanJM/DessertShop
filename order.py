from payment import Payment


class Order:
    def __init__(self):
        super().__init__()
        self.order = []
        self.pay_type = Payment.pay_type.CASH

    def sort_order(self):
        for i in range(len(self.order)):
            for j in range(i+1, len(self.order)):
                if self.order[i] > self.order[j]:
                    temp = self.order[i]
                    self.order[i] = self.order[j]
                    self.order[j] = temp

    def add(self, dessert_item):
        for i in range(len(self.order)):
            if len(self.order) == 1:
                print("first item")
                self.order.append(dessert_item)
        self.order.append(dessert_item)

    def item_count(self):
        return len(self.order)

    def order_cost(self):
        total_cost = 0
        for i in range(len(self.order)):
            total_cost += self.order[i].calculate_cost()
        return total_cost

    def order_tax(self):
        total_tax = 0
        for i in range(len(self.order)):
            total_tax += self.order[i].calculate_tax()
        return total_tax

    # def combine_order(self):
    # for i in range(len(self.order)):
    # for j in range(len(self.order)):
    # if self.order[i].can_combine(self.order[j]):
    # self.order[i].combine(self.order[j])
    # break

    def __str__(self):

        def get_payment_type():
            pay_type = input("What form of payment will be used? (CASH, CARD, PHONE): ")
            if pay_type == "Cash" or pay_type == "cash":
                self.pay_type = Payment.pay_type.CASH
            elif pay_type == "Card" or pay_type == "card":
                self.pay_type = Payment.pay_type.CARD
            elif pay_type == "Phone" or pay_type == "phone":
                self.pay_type = Payment.pay_type.PHONE
            else:
                print("That is not a valid payment method. Please enter('Cash', 'Card or 'Phone')")
                get_payment_type()
        self.customer_name = input("Enter the customer name: ")
        get_payment_type()
        print("------------Receipt---------------")
        for i in range(len(self.order)):
            print(self.order[i])
        print("------------------------------------------------------")
        print(f"Total items in the order: {self.item_count()}")
        order_sub = "Order Subtotals:|"
        order_total = "Order Total:"
        order_num = f"${self.order_cost():0.2f}"
        this_string = f"{order_sub:26}"
        this_string += f"{order_num:24}"
        this_string += f"[Tax: ${self.order_tax():0.2f}]"
        print(f"{this_string}")
        that_string = f"{order_total:50}"
        x = self.order_cost() + self.order_tax()
        that_string += f"${x:0.2f}"
        print(that_string)
        print("------------------------------------------------------")
        print(f"Paid with {self.pay_type.value}")
        print("-------------------------------------------------------")
