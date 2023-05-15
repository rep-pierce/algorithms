# def fourNumberSum(array, targetSum):
#     array.sort()
#     quads = []
#     leftOne = 0
#     rightOne = len(array) - 1

#     while leftOne < rightOne - 2:
#         leftTwo = leftOne + 1
#         rightTwo = rightOne - 1

#         while leftTwo < rightTwo:
#             currentSum = array[leftOne] + array[leftTwo] + array[rightOne] + array[rightTwo]
#             if currentSum == targetSum:
#                 quads.append([array[leftOne], array[leftTwo], array[rightOne], array[rightTwo]])
#                 leftTwo += 1
#                 rightTwo -= 1
#             elif currentSum < targetSum:
#                 leftTwo += 1
#             elif currentSum > targetSum:
#                 rightTwo -=1

#         leftOne += 1
#         if array[leftOne] > 0:
#             rightOne -= 1

#     return quads


# def fourNumberSum(array, targetSum):
#     array.sort()
#     quads = []
    
#     for i in range(0, len(array) - 3):
#         for j in range(i + 1, len(array) - 2):
#             left = j + 1
#             right = len(array) - 1

#             while left < right:
#                 currentSum = array[i] + array[j] + array[left] + array[right]
#                 if currentSum == targetSum:
#                     quads.append([array[i], array[j], array[left], array[right]])
#                     left += 1
#                     right -= 1
#                 elif currentSum < targetSum:
#                     left += 1
#                 elif currentSum > targetSum:
#                     right -= 1

#     return quads


import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = a*b
d = np.dot(a,b)
print(c, d)
