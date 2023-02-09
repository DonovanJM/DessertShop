from dessert import DessertItem
from combine import Combinable


class Cookie(DessertItem, Combinable):
    def __init__(self, name="Cookie", cookie_quantity=13, price_per_dozen=9.99):
        super().__init__(name)
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen
        self.packaging = "Box"

    def set_cookie_quantity(self, new_cookie_quantity):
        self.cookie_quantity = new_cookie_quantity

    def set_price_per_dozen(self, new_price_per_dozen):
        self.price_per_dozen = new_price_per_dozen

    def get_cookie_quantity(self):
        return self.cookie_quantity

    def get_price_per_dozen(self):
        return self.price_per_dozen

    def calculate_cost(self):
        price = round(float(self.price_per_dozen) * (float(self.cookie_quantity) / 12), 2)
        return price

    def test_calculate_cost(self):
        assert self.calculate_cost() == 10.82

    def test_calculate_tax(self):
        assert self.calculate_tax() == 0.78

    def __str__(self):
        first = f"{self.cookie_quantity:0.0f} cookies @ ${self.price_per_dozen:0.2f} a dozen:"
        second = f"${self.calculate_cost():0.2f}"
        this_string = f"{self.name} cookies ({self.packaging})\n     "
        this_string += f"{first:33}"
        this_string += f"{second:12}"
        this_string += f" [Tax: ${self.calculate_tax():0.2f}]"
        return this_string

    def can_combine(self, other: "Cookie"):
        if other.name == self.name and other == self:
            return True
        return False

    def combine(self, other: "Cookie") -> "Cookie":
        if self.can_combine(other):
            self.cookie_quantity += other.cookie_quantity
            del other
        return self
