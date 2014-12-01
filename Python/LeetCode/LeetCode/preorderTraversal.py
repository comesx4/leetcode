#
# https://oj.leetcode.com/problems/binary-tree-preorder-traversal/
#
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        if None == root:
            return []

        lst = []
        lst.append(root.val)
        lst.extend(self.preorderTraversal(root.left))
        lst.extend(self.preorderTraversal(root.right))