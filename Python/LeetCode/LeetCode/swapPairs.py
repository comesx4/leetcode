# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if None == head or head.next == None:
            return head

        tmp = head.next
        head.next = tmp.next
        tmp.next = head
        head = tmp

        node = head.next.next
        parent = head.next
        while None != node and None != node.next:
            tmp = node.next
            node.next = tmp.next
            tmp.next = node

            parent.next = tmp
            parent = tmp.next
            node = tmp.next.next
        return head

if "__main__" == __name__:
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(4)
    node.next.next.next.next = ListNode(5)

    ins = Solution()
    n = ins.swapPairs(node)
    input()