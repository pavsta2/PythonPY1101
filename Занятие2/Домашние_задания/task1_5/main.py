import random
from string import ascii_lowercase, ascii_uppercase, digits

def pass_gen(k:int):
    while True:
        yield(random.sample(ascii_lowercase+digits+ascii_uppercase, k))

if __name__ == "__main__":
    print(next(pass_gen(8)))
    print(next(pass_gen(8)))
