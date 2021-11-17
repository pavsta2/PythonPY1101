def positive_check(fn):
    def wrapper(arg):
        if not arg > 0:
            raise ValueError("Аргумент функции не является положительным числом")   #написать проверку положительности аргумента arg

        result = fn(arg)

        return result

    return wrapper


@positive_check   #задекорировать функцию
def some_func(num: int):
    return num ** 2


if __name__ == "__main__":
    print(some_func(5))  # всё хорошо

    some_func(-10)  # должна быть вызвана ошибка ValueError
