from abc import ABC, abstractmethod


class DessertItem(ABC):
    def __init__(self, name=None):
        self.name = name
        self.tax_percentage = .0725

    def __eq__(self, other):
        if self.calculate_cost() == other.calculate_cost():
            return True

    def __neg__(self, other):
        if self.calculate_cost() != other.calculate_cost():
            return True

    def __lt__(self, other):
        if self.calculate_cost() < other.calculate_cost():
            return True

    def __gt__(self, other):
        if self.calculate_cost() > other.calculate_cost():
            return True

    def __ge__(self, other):
        if self.calculate_cost() >= other.calculate_cost():
            return True

    def __le__(self, other):
        if self.calculate_cost() <= other.calculate_cost():
            return True

    @abstractmethod
    def calculate_cost(self):
        pass

    def calculate_tax(self):
        return round(self.tax_percentage * self.calculate_cost(), 2)

    def test_tax_percentage(self):
        assert self.tax_percentage == .0725
