'''
二分搜索 递归版本
'''


def binarysearch(nums, item):
    if len(nums) == 0:
        return False
    else:
        midpoint = len(nums)//2

        if nums[midpoint] == item:
            return True
        else:
            if nums[midpoint] < item:
                binarysearch(nums[midpoint+1:], item)
            else:
                binarysearch(nums[:midpoint-1], item)
        return False


# nums = [0, 1, 2, 8, 13, 17, 19, 32, 42]
# print(binarysearch(nums, 3))

'''
二分搜索 迭代版本
'''


def binarysearch2(nums, item):
    if len(nums) == 0:
        return False
    first = 0
    last = len(nums) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if nums[midpoint] == item:
            found = True
        else:
            if nums[midpoint] < item:
                first = midpoint + 1
            else:
                last = midpoint - 1

    return found


nums = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binarysearch2(nums, 13))
