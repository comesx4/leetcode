#
# https://oj.leetcode.com/problems/binary-tree-inorder-traversal/
#
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        if None == root:
            return []

        lst = []
        lst.extend(self.inorderTraversal(root.left))
        lst.append(root.val)
        lst.extend(self.inorderTraversal(root.right))
        return lst