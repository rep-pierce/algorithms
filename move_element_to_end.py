def moveElementToEnd(array, toMove):
    idx = 0
    totalIdx = 0

    while totalIdx < len(array):
        moving = None
        if array[idx] == toMove:
            moving = array.pop(idx)
            array.append(moving)
            idx -= 1
        totalIdx += 1
        idx += 1
        
    return array

