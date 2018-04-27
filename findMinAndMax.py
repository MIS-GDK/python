def findMinMax(L):
    if len(L) != 0:
        min = L[0]
        max = L[0]
        for i in L:
            if min > i:
                min = i
            if max < i:
                max = i
        return (min,max)
    else:
        return(None,None)

# 测试
if findMinMax([]) != (None, None):
    print('测试失败!')
elif findMinMax([7]) != (7, 7):
    print('测试失败!')
elif findMinMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')