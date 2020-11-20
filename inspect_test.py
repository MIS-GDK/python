import inspect


def get_required_kw_args(fn):
    args = []
    params = inspect.signature(fn).parameters
    for name, param in params.items():
        if (
            param.kind == inspect.Parameter.KEYWORD_ONLY
            and param.default == inspect.Parameter.empty
        ):
            args.append(name)
    return tuple(args)


def add_test(x, *, y=3, z):
    return x + y


sig = inspect.signature(add_test)
print(sig)
print(sig.parameters)
print(sig.parameters.items())

# print(get_required_kw_args(add_test))

