def myAtoi(str: str) -> int:
    sign, base, i = 1, 0, 0
    INT_MAX = pow(2, 31) - 1
    INT_MIN = -1 * pow(2, 31)
    while i < len(str) and str[i] == " ":
        i += 1
    if i == len(str):
        return 0
    if str[i] == "-" or str[i] == "+":
        if str[i] == "-":
            sign = -1
        i += 1
    while i < len(str) and str[i] >= "0" and str[i] <= "9":
        if base > INT_MAX // 10 or (
            base == INT_MAX // 10 and ord(str[i]) - ord("0") > 7
        ):
            if sign == 1:
                return INT_MAX
            else:
                return INT_MIN
        base = 10 * base + (ord(str[i]) - ord("0"))
        i += 1
    return base * sign


print(myAtoi("   "))
