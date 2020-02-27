from timeit import Timer


def test1():
    l = []
    for i in range(10):
        l = l + [i]



t1 = Timer("test1()", "from list_test import test1")
print("concat ", t1.timeit(number=1000) * 1000, "milliseconds")

print(__name__)
