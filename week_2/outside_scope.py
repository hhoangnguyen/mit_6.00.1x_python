x = 5


def g(y):
    print(x)

g(2)
# ok, reference and use global x, must be careful in real life
print(x)


def h(y):
    x = x + 1

h(x)
# UnboundLocalError
print(x)
