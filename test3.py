import inspect


def foo(a, b, *args,c, **kwargs):
    pass


sig = inspect.signature(foo)
for name, param in sig.parameters.items():
    print('参数：%s的类型为：%s' % (name, param.kind))
