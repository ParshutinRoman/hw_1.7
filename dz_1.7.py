class FarmUnit:
    feed = 0  # kg
    weight = 0  # kg
    fertility = 0  # units/year
    product = 'meat'
    price_alive = 0  # bitcoins
    price_dead = 0  # bitcoins

    def to_feed(self, value):
        self.feed += value

    def to_kill(self, weight):
        self.price_dead *= weight

    def to_sell(self, weight):
        self.price_alive *= weight * 0.1


class FourLegsUnit(FarmUnit):
    sub_product = ['horn']


class TwoWingsUnit(FarmUnit):
    sub_product = ['egg', 'feather']


class Cow(FourLegsUnit):
    bonus_product = ['milk', 'skin']


class Sheep(FourLegsUnit):
    bonus_product = ['fur']


class Pig(FourLegsUnit):
    bonus_product = ['fat']


class Goat(FourLegsUnit):
    bonus_product = ['milk']


class Duck(TwoWingsUnit):
    pass


class Chicken(TwoWingsUnit):
    pass


class Goose(TwoWingsUnit):
    pass
