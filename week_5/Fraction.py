class Fraction(object):
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def __str__(self):
        return str(self.numer) + ' / ' + str(self.denom)

    def getNumer(self):
        return self.numer

    def getDenom(self):
        return self.denom

    def __add__(self, other):
        numerNew = other.getDenom() * self.getNumer() + other.getNumer() * self.getDenom()
        denomNew = other.getDenom() * self.getDenom()
        return Fraction(numerNew, denomNew)

    def convert(self):
        return self.getNumer() / self.getDenom()

one_half = Fraction(1, 2)
print(one_half)
print(one_half.getNumer())
print(one_half.getDenom())

two_thirds = Fraction(2, 3)

new = one_half + two_thirds
print(new)
print(one_half.convert())
