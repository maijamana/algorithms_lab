def linear_search(list_of_values, value):
    n = -1
    for i in range(len(list_of_values)):
        if list_of_values[i] == value:
            n = i
    return n
print(linear_search([1, 2, 3], 3))
