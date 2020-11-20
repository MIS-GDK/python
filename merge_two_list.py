def merge(nums1, m: int, nums2, n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i = 0
    j = 0
    while i < m and j < n:
        if nums1[i] <= nums2[j]:
            i += 1
        else:
            for x in range(m, i, -1):
                nums1[x] = nums1[x - 1]
            nums1[i] = nums2[j]
            j += 1
            m = m + 1
            i = i + 1
    while j < n:
        nums1[i] = nums2[j]
        j = j + 1
        i = i + 1
    nums1 = nums1[: m + n]
    for val in nums1:
        print(val)


def merge2(nums1, m: int, nums2, n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1
        else:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1
    if n > 0:
        nums1[:n] = nums2[:n]
    for val in nums1:
        print(val)


merge2([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
# for i in range(3 - 1, -1, -1):
#     print(i)
