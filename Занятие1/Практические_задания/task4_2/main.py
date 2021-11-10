from itertools import count


def task():
    iterator_numbers = count(1, 1)
    numbers = map(lambda x: x ** 2,
                  filter(lambda x: x % 2 == 0,
                         iterator_numbers))

    for _ in range(10):
        print(next(numbers))


if __name__ == "__main__":
    task()
