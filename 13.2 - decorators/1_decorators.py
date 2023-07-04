from functools import wraps
from typing import Callable


def change_args(*args: str, **kwargs: int) -> Callable:
    """
    Принимает произвольное количество неименованных аргументов типа str и именованных аргументов типа int.
    Заменяет все аргументы декорированной функции на переданные в change_args.

    Пример использования:

    @change_args("a", "b", z=3)
    def my_func(x, y, z):
        print(x, y, z)

    my_func()  # Вывод: "a b 3"
    """

    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args_we_dont_need, **kwargs_we_dont_need):
            return func(*args, **kwargs)

        return inner

    return wrapper


def change_function(func: Callable) -> Callable:
    """
    Заменяет декорированную функцию на новую функцию.

    Пример использования:

    @change_function(lambda x, y: x * y)
    def my_func(x, y):
        return x + y

    print(my_func(1, 2))  # Вывод: 2
    """

    @wraps(func)
    def wrapper(func_we_dont_need: Callable) -> Callable:
        @wraps(func_we_dont_need)
        def inner(*args, **kwargs):
            return func(*args, **kwargs)

        return inner

    return wrapper
