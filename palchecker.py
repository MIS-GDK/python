from collections import deque


def palchecker(astring):
    chardeque = deque()
    if len(astring) == 0:
        return True
    for i in astring:
        if (
            (ord(i) >= 48 and ord(i) <= 57)
            or (ord(i) >= 65 and ord(i) <= 90)
            or (ord(i) >= 97 and ord(i) <= 122)
        ):
            chardeque.appendleft(i)

    stillequal = True
    chardeque_len = len(chardeque)

    while stillequal and chardeque_len > 1:
        if chardeque.popleft().upper() == chardeque.pop().upper():
            chardeque_len -= 2
        else:
            stillequal = False

    return stillequal


print(palchecker("A man, a plan, a canal: Panama"))
