def args_type_check(fn):
    def wrapper(*args):
        result = fn(*args)

        if not isinstance(*args, int):
            raise TypeError(f"Аргумент функции {fn} д.б.целое число")
    return wrapper
@args_type_check
def return_arg_int(arg: int):
    return print(arg)


if __name__ == "__main__":
    return_arg_int("er")
