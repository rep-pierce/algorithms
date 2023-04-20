# def smallestDifference(array1, array2):
#     smallest_difference = None
#     small_array = []

#     for i in array1:
#         for j in array2:
#             difference = abs(i-j)
#             if smallest_difference == None:
#                 smallest_difference = difference
#                 small_array = [i, j]
#             elif difference < smallest_difference:
#                 smallest_difference = difference
#                 small_array = [i, j]
#     return small_array

def smallestDifference(array1, array2):
    array1.sort()
    array2.sort()

    x = len(array1) - 1
    y = len(array2) - 1

    small_diff = float('inf')
    small_pair = []

    while x >= 0 and y >= 0:
        diff = abs(array1[x] - array2[y])
        if diff == 0:
            return [array1[x], array2[y]]
        elif diff < small_diff:
            small_diff = diff
            small_pair = [array1[x], array2[y]]

        if array1[x] < array2[y]:
            y -= 1
        else:
            x -= 1

    return small_pair


        
    