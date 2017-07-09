from MITPerson import *


class Student(MITPerson):
    pass


class UG(Student):
    def __init__(self, name, class_year):
        MITPerson.__init__(self, name)
        self.year = class_year

    def get_class(self):
        return self.year

    def speak(self, utterance):
        return MITPerson.speak(self, " Dude, " + utterance)


class Grad(Student):
    pass


class TransferStudent(Student):
    pass


def is_student(obj):
    return isinstance(obj, Student)

s1 = UG('Matt Damon', 2017)
s2 = UG('Ben Affleck', 2017)
s3 = UG('Lin Manuel Miranda', 2018)
s4 = Grad('Leonardo di Caprio')
s5 = TransferStudent('Robert deNiro')

studentList = [s1, s2, s3, s4, s5]

print(s1)
print(s1.get_class())
print(s1.speak('where is the quiz?'))
print(s2.speak('I have no clue!'))
