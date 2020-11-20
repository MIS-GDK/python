def decorate(func):
    print("running decorator when import")
    return func


@decorate
def foo():
    print("running foo")
    pass


if __name__ == "__main__":
    print("start foo")
    foo()
