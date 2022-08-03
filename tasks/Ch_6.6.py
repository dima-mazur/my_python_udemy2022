prices = {"Strawberries": 1.5, "Banana": 0.5, "Mango": 2.5,
		  "Blueberries": 1, "Raspberries": 1, "Apple": 1.75,
		  "Pineapple": 3.5}


class Beverage:
    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.cost = 0

    def get_cost(self):
        for i in self.ingredients:
            if i in prices:
                self.cost += prices[i]
        return f'${self.cost:.2f}'

    def get_price(self):
        return f'${self.cost * 2.5:.2f}'

    def get_name(self):
        name = self.ingredients
        if len(name) > 1:
            name.sort()
            name += ['Fusion']
        else:
            name += ['Smoothie']

        new_name = []

        for i in name:
            if i.find('berries'):
                new_name.append(i.replace('berries', 'berry'))

        result = ''
        for i in new_name:
            result += i + ' '

        return result.strip()


s1 = Beverage(['Banana'])
print(s1.ingredients)
print(s1.get_cost())
print(s1.get_price())
print(s1.get_name())

s2 = Beverage(['Raspberries', 'Strawberries', 'Blueberries'])
print(s2.ingredients)
print(s2.get_cost())
print(s2.get_price())
print(s2.get_name())
