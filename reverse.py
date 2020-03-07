def reverse_str(str):
    if len(str) == 1:
        return str[0]
    else:
        return str[len(str) - 1] + reverse_str(str[: len(str) - 1])


print(reverse_str("qwertty"))

