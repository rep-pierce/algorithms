def smallestDifference(array1, array2):
    smallest_difference = None
    small_array = []

    for i in array1:
        for j in array2:
            difference = abs(i-j)
            if smallest_difference == None:
                smallest_difference = difference
                small_array = [i, j]
            elif difference < smallest_difference:
                smallest_difference = difference
                small_array = [i, j]
    return small_array

