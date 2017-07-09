class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def intersect(self, other):
        """Returns an intSet object of intersections of self and other intSet object"""
        intersect_set = intSet()
        for value in self.vals:
            if other.member(value):
                intersect_set.insert(value)
        return intersect_set

    def __len__(self):
        """Returns the number of element in self"""
        return len(self.vals)

set = intSet()
set.insert(3)
set.insert(4)
set.insert(2)
print(set)
print(len(set))

setB = intSet()
setB.insert(3)
setB.insert(2)

setC = intSet()
setC.insert(5)
setC.insert(6)

print(set.intersect(setB))
print(set.intersect(setC))
