from animal import *


class Rabbit(Animal):
    tag = 1

    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1

    def get_rid(self):
        return str(self.rid).zfill(3)

    def get_parent1(self):
        return self.parent1

    def get_parent2(self):
        return self.parent2

    def __add__(self, other):
        return Rabbit(0, self, other)

    def __eq__(self, other):
        """Two Rabbits are equal if they have the same two parents"""
        parents_same = self.get_parent1().get_rid() == other.get_parent1().get_rid() and \
                       self.get_parent2().get_rid() == other.get_parent2().get_rid()

        parents_opposite = self.get_parent1().get_rid() == other.get_parent2().get_rid() and \
                            self.get_parent2().get_rid() == other.get_parent1().get_rid()

        return parents_same or parents_opposite

    def speak(self):
        print('meep')

    def __str__(self):
        return "rabbit:" + str(self.get_name()) + ":" + str(self.get_age())

father = Rabbit(4)
mother = Rabbit(3)
child = Rabbit(1, father, mother)

print(father)
print(mother)
print(child)
print('father id:', father.get_rid())
print('mother id:', mother.get_rid())
print('child id:', child.get_rid())
print('current tag:', Rabbit.tag)

new_child = father + mother
print('new child id:', new_child.get_rid())
print('current tag:', Rabbit.tag)

print('child == new_child: ', child == new_child)
