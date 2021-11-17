def header_footer(fn):  #написать декоратор
    def wrapper(*args, **kwargs):
        print("========")
        result = fn(*args, **kwargs)
        print("========")
        return result
    return wrapper


@header_footer
def my_func():
    print("Hello World")


if __name__ == "__main__":
    my_func()
