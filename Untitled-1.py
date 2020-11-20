def wrapper1(func):
    def inner1(*args, **kwargs):
        print("1")
        res = func(*args, **kwargs)
        print("2")
        return res

    return inner1


def wrapper2(func):
    def inner2(*args, **kwargs):
        print("3")
        res = func(*args, **kwargs)
        print("4")
        return res

    return inner2


def wrapper3(func):
    def inner3(*args, **kwargs):
        print("5")
        res = func(*args, **kwargs)
        print("6")
        return res

    return inner3


# @wrapper1  # inner1 = wrapper1(inner2)
# @wrapper2  # inner2 = wrapper2(inner3)  -- wrapper2(wrapper3(foo))
@wrapper3  # inner3 = wrapper3(foo)
def foo():
    print("from foo")


# foo()
