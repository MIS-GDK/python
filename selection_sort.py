def selectionsort(alist):
    for i in range(len(alist) - 1, 0, -1):
        positionOfMax = 0
        for j in range(1, i + 1):
            if alist[j] > alist[positionOfMax]:
                positionOfMax = j

        temp = alist[i]
        alist[i] = alist[positionOfMax]
        alist[positionOfMax] = temp
    return alist


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selectionsort(alist)
print(alist)

