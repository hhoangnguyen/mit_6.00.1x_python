from Person import *


class MITPerson(Person):
    next_id_num = 0 # next ID number to assign

    def __init__(self, name):
        Person.__init__(self, name)
        self.id_num = MITPerson.next_id_num
        MITPerson.next_id_num += 1

    def get_id_num(self):
        return self.id_num

    def __lt__(self, other):
        return self.id_num < other.id_num

    def speak(self, utterance):
        return self.name + " says: " + utterance

"""
m3 = MITPerson('Mark Zuckerberg')
m3.set_birthday(5, 14, 84)
m2 = MITPerson('Drew Houston')
m2.set_birthday(3, 4, 83)
m1 = MITPerson('Bill Gates')
m1.set_birthday(10, 28, 55)

MITPersonList = [m1, m2, m3]

# print in order created
for e in MITPersonList:
    print(e)

print()

# print in order id_num
MITPersonList.sort()
for e in MITPersonList:
    print(e)

print()

p1 = MITPerson('Eric')
p2 = MITPerson('John')
p3 = MITPerson('John')
p4 = Person('John')

print('p1 < p2:', p1 < p2)
# it is important to know that p1 < p4 throw an exception because p4 doesn't have an id_num
# and p1 < p4 => p1.__lt__(p4) uses __lt__ of MITPerson which needs id_num
# p4 < p1 is ok because it uses __lt__ of Person which compares name instead of id_num
print('p1 > p4:', p1 > p4)
"""
