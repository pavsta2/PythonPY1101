def gen_geom_pr(num: int = 1):
    while True:
        yield num * num
        num += 1

if __name__ == "__main__":
    my_gen = gen_geom_pr(4)

    print(next(my_gen))
    print(next(my_gen))
    print(next(my_gen))
