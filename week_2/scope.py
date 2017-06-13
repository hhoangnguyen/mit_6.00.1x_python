def f(x):
    x = x + 1
    # x inside (local scope) is 4
    print('inside f(x): x = ', x)
    return x

x = 3
z = f(x)
print('z = ', z)

# x outside (global scope) is 3
print('outside f(x): x = ', x)
