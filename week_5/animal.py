class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_age(self, new_age):
        self.age = new_age

    def set_name(self, new_name=""):
        self.name = new_name

    def __str__(self):
        return "animal:" + str(self.name) + ":" + str(self.age)


class Cat(Animal):
    def speak(self):
        print('meow')

    def __str__(self):
        return "cat:" + str(self.get_name()) + ":" + str(self.get_age())


class Rabbit(Animal):
    tag = 1

    def speak(self):
        print('meep')

    def __str__(self):
        return "rabbit:" + str(self.get_name()) + ":" + str(self.get_age())

print(Rabbit.tag)


class Person(Animal):
    def __init__(self, name, age):
        # call parent's methods
        Animal.__init__(self, age)
        Animal.set_name(self, name)
        self.friends = []

    def get_friends(self):
        return self.friends

    def add_friends(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)

    def speak(self):
        """Override paren's speak method"""
        print("hello")

    def __str__(self):
        return "person:" + str(self.get_name()) + ":" + str(self.get_age())

    def age_diff(self, other):
        diff = self.get_age() - other.get_age()
        if diff > 0:
            print(self.get_name(), 'is', diff, ' years older than', other.get_name())
        else:
            print(self.get_name(), 'is', abs(diff), ' years younger than', other.get_name())

eric = Person('eric', 45)
huy = Person('huy', 33)
# note 2 different ways to call age_diff
eric.age_diff(huy)
Person.age_diff(huy, eric)
