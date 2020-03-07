def sum_list(numlist):
    if len(numlist) == 1:
        n = n + 1
        print(n)
        return numlist[0]
    else:
        n = n+1
        return numlist[0] + sum_list(numlist[1:])


# print(sum([2, 4, 6, 8]))
sum([2, 4, 6, 8])
