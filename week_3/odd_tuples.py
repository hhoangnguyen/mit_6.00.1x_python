def odd_tuples(a_tup):
    counter = 1
    new_tup = ()
    for t in a_tup:
        if counter % 2 == 1:
            new_tup = new_tup + (t, )
        counter += 1
    print(new_tup)
    return new_tup
odd_tuples((1, 2, 3, 4, 5))
