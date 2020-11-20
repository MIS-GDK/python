# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        headNode = ListNode(0)
        temp2 = headNode
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                temp2.next = l1
                l1 = l1.next
            else:
                temp2.next = l2
                l2 = l2.next
            temp2 = temp2.next
        if l1 is None:
            temp2.next = l2
        else:
            temp2.next = l1
        return headNode.next
