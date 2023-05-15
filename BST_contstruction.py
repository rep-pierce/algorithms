# class BST:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

#     def insert(self, value):
#         currentNode = self
#         while True:
#             if value < currentNode.value:
#                 if currentNode.left is None:
#                     currentNode.left = BST(value)
#                     break
#                 else:
#                     currentNode = currentNode.left
#             else:
#                 if currentNode.right is None:
#                     currentNode.right = BST(value)
#                     break
#                 else:
#                     currentNode = currentNode.right
#         return self

#     def contains(self, value):
#         currentNode = self
#         while currentNode is not None:
#             if value < currentNode.value:
#                 currentNode = currentNode.left
#             elif value > currentNode.value:
#                 currentNode = currentNode.right
#             else:
#                 return True
#         return False

#     def remove(self, value, parentNode = None):
#         currentNode = self
#         while currentNode is not None:
#             if value < currentNode.value:
#                 parentNode = currentNode
#                 currentNode = currentNode.left
#             elif value > currentNode.value:
#                 parentNode = currentNode
#                 currentNode = currentNode.right
#             else:
#                 if currentNode.left is not None and currentNode.right is not None:
#                     currentNode.value = currentNode.right.getMinValue()
#                     currentNode.right.remove(currentNode.value, currentNode)
#                 elif parentNode is None:
#                     if currentNode.left is not None:
#                         currentNode.value = currentNode.left.value
#                         currentNode.right = currentNode.left.right
#                         currentNode.left = currentNode.left.left
#                     elif currentNode.right is not None:
#                         currentNode.value = currentNode.right.value
#                         currentNode.left = currentNode.right.left
#                         currentNode.right = currentNode.right.right
#                     else:
#                         currentNode.value = None
#                 elif parentNode.left == currentNode:
#                     parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
#                 elif parentNode.right == currentNode:
#                     parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
#                 break
#         return self if currentNode is not None else None

#     def getMinValue(self):
#         currentNode = self
#         while currentNode.left is not None:
#             currentNode = currentNode.left
#         return currentNode.value

# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BST(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BST(value)
                
        return self

    def contains(self, value):
        # Write your code here.
        if value < self.value:
            if self.left:
                return self.left.contains(value)
            return False
        elif value > self.value:
            if self.right:
                return self.right.contains(value)
            return False
        return True
        pass

    def remove(self, value):
        if not self:
            return self

        if value < self.value:
            if self.left:
                self.left = self.left.remove(value)
        elif value > self.value:
            if self.right:
                self.right = self.right.remove(value)
        else:
            if not self.right and not self.left:
                return None
            elif not self.left:
                self.value = self.right.value
                self.left = self.right.left
                self.right = self.right.right
            elif not self.right:
                self.value = self.left.value
                self.right = self.left.right
                self.left = self.left.left
                return self

            else:
                successor = self.right.inOrderSuccessor()
                self.value = successor.value
                self.right = self.right.remove(successor.value)
                
        return self

    def inOrderSuccessor(self):
        while self.left:
            self = self.left
        return self