class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

    def getData(self):
        return self.val

    def getNext(self):
        return self.next


class ListNode:
    def __init__(self):
        super().__init__()
        self.head = None

    def add(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node


a = [1, 2, 3, 5, 8]
s = ListNode()
for i in a:
    s.add(i)
temp = s.head
while temp:
    print(temp.getData())
    temp = temp.getNext()
