class Employee:
    def __init__(self, name, last_name, salary):
        self.first_name = name.title()
        self.last_name = last_name.title()
        self.salary = salary

        # self.first_name = self.name.title()
        # self.last_name = self.l_name.title()

    @classmethod
    def from_string(cls, string):
        pars = string.split('-')
        cls.first_name = pars[0]
        cls.last_name = pars[1]
        cls.salary = int(pars[2])
        return Employee(cls.first_name, cls.last_name, cls.salary)


emp1 = Employee('mary', 'Sue', 60000)
emp2 = Employee.from_string('John-Smith-55000')

print(emp1.first_name)
print(emp1.salary)

print(emp2.first_name)
print(emp2.salary)

