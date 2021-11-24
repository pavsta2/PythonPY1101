import json


def task():
    filename = "input.json"
    with open(filename) as f:
        dict_python = json.load(f)  #считать содержимое JSON файла

    return max(dict_python, key = lambda item: item["score"])   #найти максимальный элемент по ключу score


if __name__ == "__main__":
    print(task())
