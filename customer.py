from order import Order


class Customer:
    def __init__(self, customer_name="John Doe"):
        self.customer_name = customer_name
        self.order_history = []
        self.customer_id = 123456789

    def add2history(self, order: Order):
        self.order_history.append(order)
        return Customer
