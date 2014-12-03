#   
# https://oj.leetcode.com/problems/populating-next-right-pointers-in-each-node/
#
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if None == root:
            return
        node = root
        next = root.left
        while None != node.left:
            node.left.next = node.right
            if None != node.next:
                node.right.next = node.next.left
                node = node.next
            else:
                node = next
                next = next.left


        