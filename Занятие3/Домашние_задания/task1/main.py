def read_file(input_file):
    with open(input_file) as f:
        result = f.read().split(",")
        for i in range(len(result)):
            for j in result[i]:
                if not (j.isalpha() or j.isdigit()):
                    result[i] = result[i].replace(j, '')
    return result


def final_list(list_str):
    list_ok = []
    for d in list_str:
        if d.isdigit():
            list_ok.append(int(d))
        else:
            list_ok.append(d)
    return list_ok


if __name__ == "__main__":

    input_file_1 = "input1"
    input_file_2 = "input2"
    output_file = "output"

    list_str_1 = read_file(input_file_1)
    print(list_str_1, type(list_str_1))

    list_str_2 = read_file(input_file_2)
    print(list_str_2, type(list_str_2))

    list_dig_str_1 = final_list(list_str_1)
    list_dig_str_2 = final_list(list_str_2)

    print(list_dig_str_1)
    print(list_dig_str_2)

    final_list_dig_str = list_dig_str_1 + list_dig_str_2
    print(final_list_dig_str)

    with open(output_file, "w", encoding="UTF-8") as f:
        f.write(str(final_list_dig_str))
