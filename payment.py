from enum import Enum


class Payment(Enum):
    CASH = "CASH"
    CARD = "CARD"
    PHONE = "PHONE"

    pay_type = Enum("Pay_type", [CASH, CARD, PHONE])
