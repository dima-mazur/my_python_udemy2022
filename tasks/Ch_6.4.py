class Pizza:
    order_number = 0

    def __init__(self, *args):
        self.ingredients = list(*args)

        Pizza.order_number += 1
        self.order_number = Pizza.order_number

    @classmethod
    def hawaiian(cls):
        return cls(['ham', 'pineapple'])

    @classmethod
    def meat_festival(cls):
        return cls(['beef', 'meatball', 'bacon'])

    @classmethod
    def garden_feast(cls):
        return cls(['spinach', 'olives', 'mushrooms'])


p1 = Pizza(['bacon', 'parmesan', 'ham'])
p2 = Pizza.garden_feast()

p1.ingredients
p2.ingredients

p1.order_number
p2.order_number





