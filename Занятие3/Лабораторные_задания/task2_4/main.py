import json


def task():
    filename = "input.json"
    with open(filename) as f:
        dict_p = json.load(f)

    gen_exr = (item["contains_improvement_appeals"] for item in dict_p)  # TODO записать выражение-генератор возвращающее значение по ключу contains_improvement_appeals
    return sum(gen_exr)


if __name__ == "__main__":
    print(task())
