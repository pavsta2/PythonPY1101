def print_args(*args):
    print(type(args), args)


def print_kwargs(**kwargs):
    print(type(kwargs), kwargs)


def print_args_kwargs(*args, **kwargs):
    for index, arg in enumerate(args):
        print(f"Позиционный аргумент {index}: {arg}")

    for key, kwarg in kwargs.items():
        print(f"Именованный аргумент {key}: {kwarg}")


if __name__ == "__main__":
    print_args(1, 4, 5)
    print_kwargs(kwarg1="test", b=1)

    print_args_kwargs(1, 4, 5, kwarg1="test", b=1)
