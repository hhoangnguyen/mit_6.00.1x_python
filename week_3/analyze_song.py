def lyric_to_frequencies(lyrics):
    my_dict = {}
    for word in lyrics:
        if word in my_dict:
            my_dict[word] += 1
        else:
            my_dict[word] = 1
    return my_dict


def most_common_words(freqs):
    values = freqs.values()
    best = max(values)
    words = []
    for word in freqs:
        if freqs[word] == best:
            words.append(word)
    return (words, best)

test_song = ['e', 'a', 'b', 'a', 'a', 'b', 'a', 'b', 'c', 'c', 'd', 'f', 'f', 'f', 'f']
print(lyric_to_frequencies(test_song))
print(most_common_words(lyric_to_frequencies(test_song)))
