def get_name(self):
    print(self.name)


class MyType(type):
    def __new__(cls, cls_name, bases, dict_attr):
        dict_attr["get_name"] = get_name  # 将get_name 作为属性添加到类属性中
        return super(MyType, cls).__new__(cls, cls_name, bases, dict_attr)


class Foo(metaclass=MyType):
    def __init__(self, name):
        self.name = name


obj = Foo("wd")
obj.get_name()  # 调用该方法
