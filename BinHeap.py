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

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentsize = len(alist)
        self.heaplist = [0] + alist[:]
        while i > 0:
            self.percDown(i)
            i = i - 1


bintree = BinHeap()
print(bintree.heaplist)
bintree.buildHeap([9, 5, 6, 2, 3])
print(bintree.heaplist)
# print(bintree.delMin())
