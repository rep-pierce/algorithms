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