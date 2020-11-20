import inspect


def parrot(
    voltage, state="a stiff", action="voom", request="test", type="Norwegian Blue"
):
    print("-- This parrot wouldn't", action, end=" ")
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


def has_request_arg(fn):
    sig = inspect.signature(fn)
    params = sig.parameters
    found = False
    for name, param in params.items():
        if name == "request":
            found = True
            continue
        if found and (
            param.kind != inspect.Parameter.VAR_POSITIONAL
            and param.kind != inspect.Parameter.KEYWORD_ONLY
            and param.kind != inspect.Parameter.VAR_KEYWORD
        ):
            print(param.kind)
            # 若判断为True，表明param只能是位置参数。且该参数位于request之后，故不满足条件，报错。
            raise ValueError(
                "request parameter must be the last named parameter in function: %s%s"
                % (fn.__name__, str(sig))
            )
    return found


print(has_request_arg(parrot))
