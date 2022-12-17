def quick_sort(lst):
    """
    The function implements a quick sorting algorithm.
    :param lst: a list to sort.
    :return: a sorted list.
    >>> quick_sort([1,3,4,10,9,2,5,6,8,7])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> quick_sort([5])
    [5]
    """
    if len(lst) <= 1:
        return lst
    left = []
    center = [] 
    right = []
    res = lst[(len(lst) // 2) - 1]
    for element in lst:
        if element < res:
            left.append(element)
        elif element == res:
            center.append(element)
        else:
            right.append(element)
    return quick_sort(left) + center + quick_sort(right)
    
if __name__ == "__main__":
    import doctest
    print(doctest.testmod(verbose=True))