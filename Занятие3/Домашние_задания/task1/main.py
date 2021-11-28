if __name__ == "__main__":
    input_file_1 = "input1"
    input_file_2 = "input2"
    output_file = "output"

    with open(input_file_1) as f:
        result = list(f.read())
        print(result)

    with open(input_file_2) as f:
        result2 = f.read()
        print(result2)
