from cookie import Cookie
from icecream import IceCream
from sundae import Sundae
from candy import Candy
from customer import Customer

chocolate_chip = Cookie()
other_cookie = Cookie("Chocolate", 134, 9.99)
vanilla = IceCream()
chocolate = IceCream("Chocolate", 123, 1.99)
twix = Candy()
hershey = Candy("Hershey", 12, 4.99)
sundae1 = Sundae()
sundae2 = Sundae("Vanilla", 123, 1.99, "Hot Fudge", .99)
customer1 = Customer()

def test_cookie_default():
    assert chocolate_chip.cookie_quantity == 13
    assert chocolate_chip.price_per_dozen == 9.99
    assert chocolate_chip.can_combine(other_cookie) == True
    assert chocolate_chip.can_combine(hershey) == False
    assert chocolate_chip.combine(other_cookie) == chocolate_chip
    assert chocolate_chip.combine(hershey) == chocolate_chip


def test_icecream_default():
    assert vanilla.scoop_count == 3
    assert vanilla.price_per_scoop == 1.99


def test_candy_default():
    assert twix.candy_weight == 5
    assert twix.price_per_pound == 4.99
    assert twix.can_combine(hershey) == True
    assert twix.can_combine(sundae1) == False
    assert twix.combine(hershey) == twix
    assert twix.combine(sundae1) == twix


def test_sundae_default():
    assert sundae1.name == "Vanilla"
    assert sundae1.scoop_count == 3
    assert sundae1.price_per_scoop == 1.99
    assert sundae1.topping_name == "Sprinkles"
    assert sundae1.topping_price == .99


def test_customer():
    assert customer1.customer_id == 123456789
    assert customer1.customer_name == "John Doe"


def main():
    """Testing default values of cookie object"""
    test_cookie_default()
    """Testing default values of ice cream object"""
    test_icecream_default()
    """Testing default values of candy object"""
    test_candy_default()
    """Testing default values of sundae object"""
    test_sundae_default()
    chocolate_chip.test_calculate_cost()
    twix.test_calculate_cost()
    vanilla.test_calculate_cost()
    sundae1.test_calculate_cost()
    "Testing Calculate Tax Method"
    chocolate_chip.test_tax_percentage()
    twix.test_calculate_tax()
    vanilla.test_calculate_tax()
    sundae1.test_calculate_tax()
    test_customer()


if __name__ == "__main__":
    main()
