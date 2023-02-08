from dessert import DessertItem
from combine import Combinable


class Candy(DessertItem, Combinable):
    def __init__(self, name="Candy", candy_weight=5, price_per_pound=4.99):
        super().__init__(name)
        self.name = name
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound
        self.packaging = "Bag"

    def set_candy_weight(self, new_candy_weight):
        self.candy_weight = new_candy_weight

    def set_price_per_pound(self, new_price_per_pound):
        self.price_per_pound = new_price_per_pound

    def get_candy_weight(self):
        return self.candy_weight

    def get_price_per_pound(self):
        return self.price_per_pound

    def calculate_cost(self):
        price = round(float(self.price_per_pound) * float(self.candy_weight), 2)
        return price

    def test_calculate_cost(self):
        assert self.calculate_cost() == 24.95

    def test_calculate_tax(self):
        assert self.calculate_tax() == 1.81

    def __str__(self):
        first = f"{self.candy_weight:0.0f}lbs @ ${self.price_per_pound:0.2f}/lb:"
        second = f"${self.calculate_cost():0.2f}"
        this_string = f"{self.name} ({self.packaging})\n     "
        this_string += f"{first:33}"
        this_string += f"{second:12}"
        this_string += f" [Tax: ${self.calculate_tax():0.2f}]"
        return this_string

    def can_combine(self, other: "Candy"):
        if self.name == other.name and self.price_per_pound == other.price_per_pound:
            return True
        return False

    def combine(self, other: "Candy"):
        if self.can_combine(other):
            self.candy_weight += other.candy_weight
            del other
            return self
        else:
            raise ValueError("Candies are not the same.")
