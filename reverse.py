def reverse_str(str):
    if len(str) == 1:
        return str[0]
    else:
        return str[len(str) - 1] + reverse_str(str[: len(str) - 1])


print(reverse_str("qwertty"))


def reverse(x):
    """
    :type x:int
    :rtype:int
    """
    nagative = ""
    reverse_x = ""
    if x < 0:
        x = -x
        nagative = "-"
    for i in str(x):
        reverse_x = i + reverse_x
    reverse_x = nagative + reverse_x
    if int(reverse_x) > pow(2, 31) - 1 or int(reverse_x) < -pow(2, 31):
        return 0
    return int(reverse_x)


def reverse2(x):
    flag = 1
    if x < 0:
        x = -x
        flag = -1
    r = str(x)[::-1]
    R = int(r) * flag
    if R > pow(2, 31) - 1 or R < -pow(2, 31):
        return 0
    return R


print(reverse2(123))
