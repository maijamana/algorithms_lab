def merge_sort(lst):
    '''
    Merge sort algorithm
    :param lst: list of numbers
    :param return: returns sorted list of numbers
    >>> merge_sort([1, 123123, -2 , 45, 77, 4, 67, 989, 6767, 88, 456, 23, 45, 55, 0, 12, 11])
    [-2, 0, 1, 4, 11, 12, 23, 45, 45, 55, 67, 77, 88, 456, 989, 6767, 123123]
    '''
    if not lst:
        return lst
    lenght = len(lst)
    if lenght > 1:
        leftpart = lst[:lenght // 2]
        rightpart = lst[lenght // 2:]
        merge_sort(leftpart)
        merge_sort(rightpart)
        leftelem = 0
        rightelem = 0
        mergeelem = 0
        while leftelem < len(leftpart) and rightelem < len(rightpart):
            if leftpart[leftelem] < rightpart[rightelem]:
                lst[mergeelem] = leftpart[leftelem]
                leftelem += 1
            else:
                lst[mergeelem] = rightpart[rightelem]
                rightelem += 1
            mergeelem += 1
        while leftelem < len(leftpart):
            lst[mergeelem] = leftpart[leftelem]
            leftelem += 1
            mergeelem += 1
        while rightelem < len(rightpart):
            lst[mergeelem] = rightpart[rightelem]
            rightelem += 1
            mergeelem += 1
        return lst