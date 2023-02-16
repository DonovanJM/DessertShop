from order import Order
import uuid


class Customer:
    def __init__(self, customer_name="John Doe"):
        self.customer_name = customer_name
        self.order_history = []
        baby = uuid.uuid1()
        self.customer_id = baby.int
        self.order_count = 0

    def add2history(self, order: Order):
        self.order_history.append(order)
        self.order_count += 1
        return Customer

    def __str__(self):
        first = f"Customer Name: {self.customer_name}"
        second = f"Customer ID: {self.customer_id}"
        third = f"Total Orders: {self.order_count}"
        final = f"{first:30}"
        final += f"{second:55}"
        final += f"{third:20}"
        print(final)
