#
# https://oj.leetcode.com/problems/same-tree/
#
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if None == p and None == q:
            return True

        if None == p or None == q:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) and p.val == q.val