import json


def task(input_filename: str, output_filename: str):
    with open(input_file) as f:
        python_obj = json.load(f)  #считать содержимое json файл input.json

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(python_obj, f, indent= 4, ensure_ascii=False)



if __name__ == "__main__":
    input_file = "input.json"
    output_file = "output.json"

    task(input_file, output_file)

    with open(output_file) as output_f:
        for line in output_f:
            print(line, end="")
