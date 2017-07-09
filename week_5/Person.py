import datetime

class Person(object):
    def __init__(self, name):
        self.name = name
        self.birthday = None
        self.last_name = name.split(' ')[-1]

    def get_last_name(self):
        return self.last_name

    def set_birthday(self, month, day, year):
        self.birthday = datetime.date(year, month, day)

    def set_age(self):
        if self.birthday is None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        """Return True if self's name is lexicographically less than other's name, and False otherwise"""
        if self.last_name == other.last_name:
            return self.name < other.name
        return self.last_name < other.last_name

    def __str__(self):
        return self.name

"""
p1 = Person('Mark Zuckerberg')
p1.set_birthday(5, 14, 84)
p2 = Person('Drew Houston')
p2.set_birthday(3, 4, 83)
p3 = Person('Bill Gates')
p3.set_birthday(10, 28, 55)
p4 = Person('Andrew Gates')
p5 = Person('Steve Wozniak')

personList = [p1, p2, p3, p4, p5]
# print in order created
for e in personList:
    print(e)

print()
# print in alphabetical order
personList.sort()
for e in personList:
    print(e)
"""
