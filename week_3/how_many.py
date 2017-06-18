animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


def how_many(d):
    count = 0
    for val in d.values():
        count += len(val)
    return count

print(how_many(animals))
