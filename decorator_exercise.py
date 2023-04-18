from typing import Callable


def star(func: Callable) -> Callable:
    """A decorator that prints 15 * before and after the function call"""
    def wrapper(*args, **kwargs):
        print("*" * 15)
        func(*args, **kwargs)
        print("*" * 15)
    return wrapper


def reverse_first_arg_string(func: Callable) -> Callable:
    """A decorator that reverses the first argument of the function call"""
    def wrapper(*args, **kwargs):
        args = list(args)
        if len(args) > 0 and isinstance(args[0], str):
            args[0] = args[0][::-1]
        func(*args, **kwargs)
    return wrapper


@star
@reverse_first_arg_string
def printer(msg):
    print(msg)


printer("i love python")


"""
Desired Behavior:

INPUT:
printer("i love python")

OUTPUT:
***************
nohtyp evol i
***************

"""