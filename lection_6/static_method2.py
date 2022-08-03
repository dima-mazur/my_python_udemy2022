class Date:
    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year

    def display(self):
        return f'{self.month} - {self.day} - {self.year}'

    @classmethod
    def millenium_c(cls, month, day):
        return cls(month, day, 2000)

    @staticmethod
    def millenium_s(month, day):
        return Date(month, day, 2000)


d1 = Date.millenium_c(6, 9)
d2 = Date.millenium_s(6, 9)
print(d1.display())
print(d2.display())


class DataTime(Date):
    def display(self):
        return  f'{self.month} - {self.day} - {self.year} - 00:00:00PM '


dt1 = DataTime(10, 10, 1990)
dt2 = DataTime.millenium_s(10, 10)
dt3 = DataTime.millenium_c(10, 10)

print(isinstance(dt1, DataTime))
print(isinstance(dt2, DataTime))
print(isinstance(dt3, DataTime))

print(dt1.display())
print(dt2.display())
print(dt3.display())