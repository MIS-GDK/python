def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    val = 0
    while val < len(nums):
        count = nums.count(nums[val])
        if count > 1:
            # nums.pop(val)
            del nums[val]
        else:
            val = val + 1
    return len(nums)


print(removeDuplicates([1, 1, 2, 3, 2, 1, 1]))
