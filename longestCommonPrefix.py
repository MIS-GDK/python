def longest_CommonPrefix(strs):
    if strs == [] or strs == "":
        return ""
    if len(strs) == 1:
        return strs[0]

    a = min(strs, key=len)
    b = 0
    for i in range(len(a)):

        for j in range(len(strs) - 1):
            if strs[j][i] != strs[j + 1][i]:
                break
        else:
            b += 1
            continue
        break
    return strs[0][:b]


print(longest_CommonPrefix(["aca", "cba"]))
