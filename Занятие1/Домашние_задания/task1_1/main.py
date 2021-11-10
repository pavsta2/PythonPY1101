from itertools import count

def func_(list_) -> list:
    counter_index = count(1,1)
    enumer_new = zip(counter_index, list_)

    return list(enumer_new)

if __name__ == "__main__":
    print(func_([1,"t",4,6,8,9,7,6,5,4]))


