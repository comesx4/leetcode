# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if None == l1:
            return l2
        if None == l2:
            return l1
        if None == l1 and None == l2:
            return None
        
        node1 = l1
        node2 = l2
        while True:
            if None == node2:
                break
            if node1.val <= node2.val:
                if node1.next == None:
                    node1.next = node2
                    break;
                else:
                    if node1.next.val < node2.val:
                        node1 = node1.next
                        continue
                    else:
                        tmp = node1.next
                        node1.next = node2
                        node2 = node2.next
                        node1.next.next = tmp
            else:
                tmp = node1
                node1 = node2
                node2 = tmp

        if l1.val <= l2.val:
            return l1
        else:
            return l2

if __name__ == "__main__":
    node = ListNode(-10)
    node.next = ListNode(-10)
    node.next.next = ListNode(-9)
    node.next.next.next = ListNode(-4)
    node.next.next.next.next = ListNode(1)
    node.next.next.next.next.next = ListNode(6)
    node.next.next.next.next.next.next = ListNode(6)

    node2 = ListNode(-7)

    ins = Solution()
    n = ins.mergeTwoLists(node, node2)
    n = ins.mergeTwoLists(ListNode(1), ListNode(1))
    input()



