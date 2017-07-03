def insertion_sort(items):
    # sort in increasing order
    for index_unsorted in range(1, len(items)):
        next = items[index_unsorted]  # item that has to be inserted
        # in the right place

        # move all larger items to the right
        i = index_unsorted
        while i > 0 and items[i - 1] > next:
            items[i] = items[i - 1]
            i = i - 1

        # insert the element
        items[i] = next
    return items

result = insertion_sort([3, 4, 7, -1, 2])
print(result)
