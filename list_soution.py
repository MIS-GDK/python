# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __init__(self):
        self.head = None

    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if head.next == None:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head

    def reverseList2(self, head: ListNode) -> ListNode:
        headNode = ListNode(0)

        while head is not None:
            temp = head.next
            head.next = headNode.next
            headNode.next = head
            head = temp

        return headNode.next

    def addnode(self, val):
        temp = ListNode(val)
        temp.next = self.head
        self.head = temp

        return self.head


mylist = Solution()

for i in range(1, 6):
    # print(i)
    my_head = mylist.addnode(i)


new_my_head = mylist.reverseList(my_head)
# new_my_head = mylist.reverseList2(my_head)
print("------------------------")

while new_my_head is not None:
    print(new_my_head.val)
    new_my_head = new_my_head.next
