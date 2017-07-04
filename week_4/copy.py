dictionary = {'a': 1, 'b': 2}


def mutate(my_dict):
    my_dict['a'] = 0
    return my_dict

print('Current dictionary:', dictionary)
print('Calling mutate() on:', mutate(dictionary))
# {'a': 0, 'b': 2} we mutated original dictionary. this is bad
print('Mutated:', dictionary)


def not_mutate(my_dict):
    # use .copy or dict[:] to clone
    clone_dict = my_dict.copy()
    clone_dict['a'] = 0
    return clone_dict

print('Current dictionary:', dictionary)
print('Calling not_mutate() on:', dictionary)
# this is good, original dictionary didn't change
print('Not mutated:', dictionary)
