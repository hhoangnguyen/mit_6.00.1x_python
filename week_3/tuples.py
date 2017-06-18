te = ()
t = (2, 'one', 3)
print(t)
print(t[0])
print(t + (5, 6))
print(t[1:2]) # return extra ',' means this is a tuple with a single element
print(('one')) # return a string
print(('one', 3))

x = 3
y = 2
(x, y) = (y, x)
print(x, y)

x = (1, 2, (3, 'John', 4), 'Hi')
print(x[0:-2])
