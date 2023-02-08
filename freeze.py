from typing import Optional
from cookie import Cookie
from icecream import IceCream
from sundae import Sundae


class Freeze:
    def __init__(self):
        self.temperature = None

    def chill(self):
        self.temperature = "Chilling"

    def thaw(self):
        self.temperature = "Thawing"

    def temperature(self):
        return self.temperature


class Freezer:

    def put(self, item: Optional[Sundae or IceCream] = Cookie) -> None:
        item.chill()

    def take(self, item_name: Optional[Sundae or IceCream] = Cookie) -> None:
        item_name.thaw()
