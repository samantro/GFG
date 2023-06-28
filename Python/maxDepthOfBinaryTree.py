class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def maxDepth(self,root):
        if root == None:
            return 0
        return max(Solution.maxDepth(self,root.left),Solution.maxDepth(self,root.right)) + 1
    