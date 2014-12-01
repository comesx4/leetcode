#
# https://oj.leetcode.com/problems/maximum-depth-of-binary-tree/
#
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        leftDepth = 1
        rightDepth = 1
        if None == root:
            return 0

        if None != root.left:
            leftDepth += self.maxDepth(root.left)
        if None != root.right:
            rightDepth += self.maxDepth(root.right)
        
        return max(leftDepth, rightDepth)
