def args_type_check(fn):
    def wrapper(args, kwargs):
        fn(args, kwargs)

        try:
            iter(args)  # объект не является итерируемым объектом
        except TypeError:  # ожидаем ошибку TypeError: 'int' object is not iterable
            print(f"Объект {args} не является итерируемым")
        try:
            iter(kwargs)  # объект не является итерируемым объектом
        except TypeError:  # ожидаем ошибку TypeError: 'int' object is not iterable
            print(f"Объект {kwargs} не является итерируемым")


    return wrapper

@args_type_check
def return_arg_iter(args, kwargs):
    return print(args, kwargs)


if __name__ == "__main__":
    return_arg_iter((1,2,3), 3)
