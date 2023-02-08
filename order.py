from payment import Payment
from cookie import Cookie
from candy import Candy


class Order(Cookie):
    def __init__(self):
        self.order = []
        self.pay_type = Payment.pay_type.CASH

    def add(self, dessert_item):
        original_type = type(dessert_item)
        if original_type == Cookie:
            print("Type Cookie")
            print(len(self.order))
            for i in range(len(self.order) - 1):
                print("Looping")
                current_type = type(self.order[i])
                if current_type != Cookie or current_type != Candy:
                    print("item is being appended")
                    self.order.append(dessert_item)
                else:
                    if self.order[i].name == dessert_item.name and self.order[i].price_per_dozen == dessert_item.price_per_dozen:
                        print("item is being combined")
                        self.order[i].cookie_quantity += dessert_item.cookie_quantity
                        return
        elif original_type == Candy:
            print("Type Candy")
            for j in range(len(self.order) - 1):
                if self.order[j].name == dessert_item.name and self.order[j].price_per_pound == dessert_item.price_per_pound:
                    print("item combined")
                    self.order[j].candy_weight += dessert_item.candy_weight
                    return
                else:
                    print("item appended")
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
