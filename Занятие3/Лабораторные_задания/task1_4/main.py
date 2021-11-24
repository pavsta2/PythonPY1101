INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():
    with open(INPUT_FILE) as f:
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f2:
            for up_line in map(str.upper, f):
                f2.write(up_line)



if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
