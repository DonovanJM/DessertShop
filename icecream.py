from dessert import DessertItem


class IceCream(DessertItem):
    def __init__(self, name="IceCream", scoop_count=3, price_per_scoop=1.99):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop
        self.packaging = "Bowl"

    def set_scoop_count(self, new_scoop_count):
        self.scoop_count = new_scoop_count

    def set_price_per_scoop(self, new_price_per_scoop):
        self.price_per_scoop = new_price_per_scoop

    def get_scoop_count(self):
        return self.scoop_count

    def get_price_per_scoop(self):
        return self.price_per_scoop

    def calculate_cost(self):
        price = round(float(self.price_per_scoop) * float(self.scoop_count), 2)
        return price

    def test_calculate_cost(self):
        assert self.calculate_cost() == 5.97

    def test_calculate_tax(self):
        assert self.calculate_tax() == 0.43

    def __str__(self):
        first = f"{self.scoop_count:0.0f} scoops @ ${self.price_per_scoop:0.2f}/scoop: "
        middle = f"${self.calculate_cost():0.2f}"
        this_string = f"{self.name} Ice Cream ({self.packaging})\n     "
        this_string += f"{first:33}"
        this_string += f"{middle:12}"
        this_string += f" [Tax: ${self.calculate_tax():0.2f}]"
        return this_string
