def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """
    newstr = ""
    INT_MAX = pow(2,31)-1
    INT_MIN = -pow(2,31)
    if str.strip() == "":
        return 0
    result,flag, i = 1,1, 0
    while str[i] == " ":
        i += 1
    if str[i] == "-" or str[i] == "+":
        if str[i] == "-":
            flag = -1
        i += 1
    while i < len(str) and str[i] >= '0' and str[i] <= '9':
