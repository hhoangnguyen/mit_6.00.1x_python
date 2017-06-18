animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


def biggest(aDict):
    result = None

    my_dict = {}
    for char in aDict:
        my_dict[char] = len(aDict[char])

    best = max(my_dict.values())

    for char in my_dict:
        if my_dict[char] == best:
            result = char
    return result
test = {'a': [], 'b': [1, 7, 5, 4, 3, 18, 10, 0]}
print(biggest(test))


def biggest_answer(aDict):
    result = None
    biggestValue = 0
    for key in aDict.keys():
        if len(aDict[key]) >= biggestValue:
            result = key
            biggestValue = len(aDict[key])
    return result
print(biggest_answer(test))
