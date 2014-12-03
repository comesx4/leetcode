#
# https://oj.leetcode.com/problems/remove-duplicates-from-sorted-list/
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if None == head:
            return None
        
        node = head
        while None != node.next:
            if node.next.val == node.val:
                node.next = node.next.next
            else:
                node = node.next

        return head