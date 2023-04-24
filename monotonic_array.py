def isMonotonic(array):
    assign = None
    monotonic = True

    idx = 0

    while idx < len(array)-1:
        if assign == None:
            if array[idx] > array[idx+1]:
                assign = "decreasing"
            elif array[idx] < array[idx+1]:
                assign = "increasing"
            else:
                assign = None
                idx += 1
        elif assign == "increasing":
            if array[idx] <= array[idx+1]:
                idx += 1
            elif array[idx] > array[idx+1]:
                monotonic = False
                break
        elif assign == "decreasing":
            if array[idx] >= array[idx+1]:
                idx += 1
            elif array[idx] < array[idx+1]:
                monotonic = False
                break

    return monotonic