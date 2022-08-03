class Name:

    def __init__(self, name, last_name):
        self.name = name
        self.last_n = last_name

    def first_name(self):
        n = self.name.title()
        return n

    def last_name(self):
        ln = self.last_n.title()
        return ln

    def full_name(self):
        a = self.first_name()
        b = self.last_name()
        return f'{a} {b}'

    def initials(self):
        a = self.first_name()
        b = self.last_name()
        return f'{a[0]}.{b[0]}.'


a1 = Name('john', 'SMITH')
print(a1.first_name())
print(a1.last_name())
print(a1.full_name())
print(a1.initials())
