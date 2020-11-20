# _*_ coding: utf-8 _*_
import os
from functools import reduce
from collections.abc import Iterable


print(os.path.abspath("."))
print(os.environ.get("PATH"))
os.mkdir("./testdir")

print(
    [
        x
        for x in os.listdir(".")
        if os.path.isfile(x) and os.path.splitext(x)[1] == ".py"
    ]
)