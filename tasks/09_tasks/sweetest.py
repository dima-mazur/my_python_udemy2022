
class IceCream:
    def __init__(self, flavor, sprinkles):
        self.flavor = flavor
        self.sprinkles = sprinkles


def sweetest_icecream(lst):
    aroma = {'Plain': 0, 'Vanilla': 5,
             'ChocolateChip': 5, 'Strawberry': 10, 'Chocolate': 10}

    result_list = []

    for ice in lst:
        aroma_items = aroma[ice.flavor]
        sprinkles = ice.sprinkles
        result_list.append(aroma_items + sprinkles)

    return max(result_list)

ice1 = IceCream('Chocolate', 13)
print(ice1.sprinkles)
sweetest_icecream([ice1])