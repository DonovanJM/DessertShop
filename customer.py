from order import Order
import random


class Customer:
    def __init__(self, customer_name="John Doe"):
        self.customer_name = customer_name
        self.order_history = []
        self.customer_id = random.randint(1, 100000000)

    def add2history(self, order: Order):
        self.order_history.append(order)
        return Customer
