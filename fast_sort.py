def fastsort(alist, a, b):
    if a >= b:
        return
    p = alist[b]
    left = a
    right = b - 1

    while left <= right:
        while left <= right and alist[left] < p:
            left += 1

        while left <= right and alist[right] > p:
            right -= 1

        if left <= right:
            alist[left], alist[right] = alist[right], alist[left]
            left, right = left + 1, right - 1
    alist[left], alist[b] = alist[b], alist[left]
    fastsort(alist, a, left - 1)
    fastsort(alist, left + 1, b)
    return alist


def fastsort2(alist):
    if len(alist) < 2:
        return alist

    pivot = alist[0]
    less = [i for i in alist[1:] if i < pivot]
    great = [i for i in alist[1:] if i >= pivot]

    return fastsort2(less) + [pivot] + fastsort2(great)


a = [23, 33, 44, 12, 55, 12, 8]

print(fastsort2(a))

print(fastsort(a, 0, 6))
