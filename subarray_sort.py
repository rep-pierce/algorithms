def subarraySort(array):
    smallest = float("inf")
    biggest = float("-inf")
    sortment = True

    i = 0
    left = 0
    right = len(array) - 1
    while i < len(array) - 1:
        
        sorted = array[i] <= array[i + 1]
        if not sorted:
            sortment = False
            if smallest > array[i + 1]:
                smallest = array[i + 1]

            if biggest < array[i]:
                biggest = array[i]

        i += 1

    if sortment:
        return [-1, -1]
        
    while left < right:

        if array[left] <= smallest:
            left += 1
            continue

        if array[right] >= biggest:
            right -= 1
            continue
        else: 
            break

    return [left, right]


# def subarraySort(array):
#     minOutOfOrder = float('inf')
#     maxOutOfOrder = float('-inf')
#     for i in range(len(array)):
#         num = array[i]
#         if isOutOfOrder(i, num, array):
#             minOutOfOrder = min(minOutOfOrder, num)
#             maxOutOfOrder = max(maxOutOfOrder, num)
#     if minOutOfOrder == float('inf'):
#         return [-1, -1]
#     subarrayLeftIdx = 0
#     while minOutOfOrder >= array[subarrayLeftIdx]:
#         subarrayLeftIdx += 1
#     subarrayRightIdx = len(array) - 1
#     while maxOutOfOrder <= array[subarrayRightIdx]:
#         subarrayRightIdx -= 1
#     return [subarrayLeftIdx, subarrayRightIdx]

# def isOutOfOrder(i, num, array):
#     if i == 0:
#         return num > array[i + 1]
#     if i == len(array) - 1:
#         return num < array[i - 1]
#     return num > array[i + 1] or num < array[i - 1]