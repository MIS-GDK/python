class BinHeap:
    def __init__(self):
        self.heaplist = [0]
        self.currentsize = 0

    def insert(self, k):
        self.heaplist.append(k)
        self.currentsize = self.currentsize + 1
        self.percUp(self.currentsize)

    def percUp(self, i):
        while i // 2 > 0:
            if self.heaplist[i] < self.heaplist[i // 2]:
                temp = self.heaplist[i // 2]
                self.heaplist[i // 2] = self.heaplist[i]
                self.heaplist[i] = temp
            i = i // 2

    def delMin(self):
        temp = self.heaplist.pop()
        self.currentsize = self.currentsize - 1
        self.heaplist[1] = temp
        self.percDown(1)
        return self.heaplist

    def percDown(self, i):
        while i * 2 < self.currentsize:
            if i * 2 + 1 > self.currentsize:
                minchild = i * 2
            else:
                if self.heaplist[i * 2] < self.heaplist[i * 2 + 1]:
                    minchild = i * 2
                else:
                    minchild = i * 2 + 1

            if self.heaplist[i] > self.heaplist[minchild]:
                temp = self.heaplist[i]
                self.heaplist[i] = self.heaplist[minchild]
                self.heaplist[minchild] = temp

            i = minchild


bintree = BinHeap()
bintree.insert(5)
bintree.insert(3)
bintree.insert(10)
bintree.insert(6)
bintree.insert(4)
bintree.insert(2)
print(bintree.heaplist)
print(bintree.delMin())
