def merge(a, b):
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i = i + 1
        else:
            c.append(b[j])
            j = j + 1
    if i == len(a):
        for x in b[j:]:
            c.append(x)
    if j == len(b):
        for y in a[i:]:
            c.append(y)

    return c


def mergeSort(alist):
    if len(alist) == 1:
        return alist
    middle = len(alist) // 2
    left = mergeSort(alist[:middle])
    right = mergeSort(alist[middle:])

    return merge(left, right)


print(mergeSort([2, 1, 8, 7, 5, 10, 3]))

