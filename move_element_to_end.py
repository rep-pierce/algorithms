# def moveElementToEnd(array, toMove):
#     idx = 0
#     totalIdx = 0

#     while totalIdx < len(array):
#         moving = None
#         if array[idx] == toMove:
#             moving = array.pop(idx)
#             array.append(moving)
#             idx -= 1
#         totalIdx += 1
#         idx += 1
        
#     return array

# def moveElementToEnd(array, toMove):
#     i = 0
#     j = len(array) - 1

#     while i < j:
#         while i < j and array[j] == toMove:
#             j -= 1
#         if array[i] == toMove:
#             array[i], array[j] = array[j], array[i]
#         i += 1

#     return array

def moveElementToEnd(array, toMove):
    a = []
    b = []
    for i in array:
        if i != toMove:
            a.append(i)
        else:
            b.append(i)
    c = a+b
    return c