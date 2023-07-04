from time import perf_counter
from typing import Any, Callable


def benchmark(func: Callable) -> Callable:
    """Декоратор, который выводит время выполнения функции."""

    def wrapper(*args: tuple, **kwargs: dict) -> Any:
        time_start = perf_counter()
        res = func(*args, **kwargs)
        print(func.__name__, perf_counter() - time_start)
        return res

    return wrapper


def logging(func: Callable) -> Callable:
    """Декоратор, который регистрирует действия скрипта.
    (на самом деле он просто выводит их, но это могло бы быть логирование!)
    """

    def wrapper(*args: tuple, **kwargs: dict) -> Any:
        res = func(*args, **kwargs)
        print(func.__name__, args, kwargs)
        return res

    return wrapper


def counter(func: Callable) -> Callable:
    """Декоратор считает и выводит количество раз, которое функция была вызвана."""

    def wrapper(*args: tuple, **kwargs: dict) -> Any:
        wrapper.count = wrapper.count + 1
        res = func(*args, **kwargs)
        print(f'{func.__name__} была использована: {wrapper.count} раз(а)')
        return res

    wrapper.count = 0
    return wrapper


@counter
@benchmark
@logging
def reverse_string(string: str) -> str:
    return str(reversed(string))


if __name__ == '__main__':
    text = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
    print(reverse_string(text))
    print(reverse_string(text * 1000))
