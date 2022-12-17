def binary_search(list_of_values, value):
    '''
    Returns index of targt in list
    >>>binary_search([1,2,5,7,8], 7)
    3
    '''
    minn=0
    maxx=len(list_of_values)-1
    index=(maxx+minn)//2
    while list_of_values[index]!=value:
        if maxx==minn:
            index=-1
            break
        if value>list_of_values[index]:
            minn=index+1
            index=(maxx+minn)//2
        elif value<list_of_values[index]:
            maxx=index
            index=(maxx+minn)//2
    return index