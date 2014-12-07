# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        length = len(num)
        if  length == 1:
            return TreeNode(num[0])
        elif length == 0:
            return None
        else:
            mid = length / 2
            node = TreeNode(num[mid])
            node.left = self.sortedArrayToBST(num[:mid])
            node.right = self.sortedArrayToBST(num[mid + 1:])                     
            return node

if __name__ == "__main__":
    ins = Solution()
    num = [1,2,3,4,5,6,7,8,9]

    node = ins.sortedArrayToBST(num)
    input()