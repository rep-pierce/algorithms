def first_non_consecutive(arr):
    first = None
    for n in arr:
        if first is None :
            first = n
        elif n == first + 1:
            first = n
        elif n != first + 1 :
            return n
        else:
            return None