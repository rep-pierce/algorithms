# def isMonotonic(array):
#     assign = None
#     monotonic = True

#     idx = 0

#     while idx < len(array)-1:
#         if assign == None:
#             if array[idx] > array[idx+1]:
#                 assign = "decreasing"
#             elif array[idx] < array[idx+1]:
#                 assign = "increasing"
#             else:
#                 assign = None
#                 idx += 1
#         elif assign == "increasing":
#             if array[idx] <= array[idx+1]:
#                 idx += 1
#             elif array[idx] > array[idx+1]:
#                 monotonic = False
#                 break
#         elif assign == "decreasing":
#             if array[idx] >= array[idx+1]:
#                 idx += 1
#             elif array[idx] < array[idx+1]:
#                 monotonic = False
#                 break

#     return monotonic

def isMonotonic(array):
    if len(array) <= 2:
        return True
    
    direction = array[1] - array[0]
    for i in range(2, len(array)):
        if direction == 0:
            direction = array[i] - array[i-1]
            continue
        if breaksDirection(direction, array[i-1], array[i]):
            return False
        
    return True

def breaksDirection(direction, previousNum, currentNum):
    difference = currentNum - previousNum
    if direction > 0:
        return difference < 0
    return difference > 0