def gen_test():
    my_value = 1
    yield print(my_value)
    my_new_value = my_value + 1
    yield print(my_new_value)

foo = gen_test()
foo.__next__()
foo.__next__()


def gen_loop(n):
    yield n
    yield n + 1

for n in gen_loop(6):
    print(n)


def gen_fib():
    fib_n_1 = 1 # fib(n-1)
    fib_n_2 = 0 # fib(n-2)
    while True:
        # fib(n) = fib(n-1) + fib(n-2)
        next = fib_n_1 + fib_n_2
        print(next)
        yield next
        fib_n_2 = fib_n_1
        fib_n_1 = next

print('Fib Generator:')
fib = gen_fib()
fib.__next__()
fib.__next__()
fib.__next__()
fib.__next__()
fib.__next__()
