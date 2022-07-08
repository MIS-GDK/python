def palindrome(str):
    if len(str) < 2:
        return True
    if ord(str[0]) < 65 or (ord(str[0]) > 90 and ord(str[0]) < 97) or ord(str[0]) > 122:
        return palindrome(str[1:])
    elif (
        ord(str[len(str) - 1]) < 65
        or (ord(str[len(str) - 1]) > 90 and ord(str[len(str) - 1]) < 97)
        or ord(str[len(str) - 1]) > 122
    ):
        return palindrome(str[:-1])
    elif str[0].lower() != str[len(str) - 1].lower():
        return False

    return palindrome(str[1:-1])


print(palindrome("aB'dbd,ba"))
