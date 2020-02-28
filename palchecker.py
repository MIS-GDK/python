from collections import deque


def palchecker(astring):
    chardeque = deque()

    for i in astring:
        chardeque.appendleft(i)

    stillequal = True
    chardeque_len = len(astring)

    while stillequal and chardeque_len > 1:
        if chardeque.popleft() == chardeque.pop():
            chardeque_len -= 2
        else:
            stillequal = False

    return stillequal


print(palchecker('hj'))
