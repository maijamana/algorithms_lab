def selection_sort(lst):
    """
    The function implements a selection sorting algorithm.
    :param list_to_sort: a list to sort.
    :return: a sorted list.
    >>> selection_sort([1, 2, 4,  5, 65, 76, 34, 5, 4, 32, 123, 9, 80, 5, 0, 120, 789, 1221, 12324])
    [0, 1, 2, 4, 4, 5, 5, 5, 9, 32, 34, 65, 76, 80, 120, 123, 789, 1221, 12324]
    """
    for element in range(0, len(lst) - 1):
        value = element
        for i in range(element + 1, len(lst)):
            if lst[i] < lst[value]:
                value = i

        if value != element:
            lst[value], lst[element] = \
                lst[element], lst[value]
    return lst

if __name__ == "__main__":
    import doctest
    print(doctest.testmod(verbose=True))