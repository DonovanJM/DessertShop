from icecream import IceCream



class Sundae(IceCream):
    def __init__(self, name="Vanilla", scoop_count=3, price_per_scoop=1.99, topping_name="Sprinkles",
                 topping_price=.99):
        super().__init__(name, scoop_count, price_per_scoop)
        self.topping_name = topping_name
        self.topping_price = topping_price
        self.packaging = "Boat"

    def set_topping_name(self, new_topping_name):
        self.topping_name = new_topping_name

    def set_topping_price(self, new_topping_price):
        self.topping_price = new_topping_price

    def get_topping_name(self):
        return self.topping_name

    def get_topping_price(self):
        return self.topping_price

    def calculate_cost(self):
        price = round(float(self.topping_price) + (float(self.price_per_scoop) * float(self.scoop_count)), 2)
        return price

    def test_calculate_cost(self):
        assert self.calculate_cost() == 6.96

    def test_calculate_tax(self):
        assert self.calculate_tax() == 0.43

    def __str__(self):
        first = f"{self.scoop_count:0.0f} scoops @ ${self.price_per_scoop:0.2f}/scoop\n     "
        middle = f"{self.topping_name} @ ${self.topping_price:0.2f}:"
        second = f"${self.calculate_cost():0.2f}"
        this_string = f"{self.topping_name} {self.name} Sundae ({self.packaging})\n     "
        this_string += f"{first}"
        this_string += f"{middle:33}"
        this_string += f"{second:12}"
        this_string += f" [Tax: ${self.calculate_tax():0.2f}]"
        return this_string
