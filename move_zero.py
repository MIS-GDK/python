"""
移动零

给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
示例:
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
"""


def move_zero(nums):
    """
    type nums:list[int]
    rtype:none
    """
    i = 0
    j = 0
    while i < len(nums) - j:
        if nums[i] == 0:
            del nums[i]
            nums.append(0)
            j += 1
        else:
            i += 1
    return nums


print(move_zero([0, 0, 1]))

