if __name__ == "__main__":
    import numbers

    input_file_1 = "input1"
    input_file_2 = "input2"
    output_file = "output"

    with open(input_file_1) as f:
        result = f.read().split(",")
        print(result, type(result))
        for i in range(len(result)):
            for j in result[i]:
                if not (j.isalpha() or j.isdigit()):
                    result[i] = result[i].replace(j, '')

        print(result, type(result))

    with open(input_file_2) as f:
        result2 = f.read().split(",")
        print(result2, type(result2))
        for i in range(len(result2)):
            for j in result2[i]:
                if not (j.isdigit() or j.isalpha()):
                    result2[i] = result2[i].replace(j, '')
        print(result2, type(result2))

    final_list = [int(d) for d in result if d.isdigit()] + [int(d) for d in result2 if d.isdigit()]
    print(final_list)

    with open(output_file,"w",encoding= "UTF-8") as f:
        f.write(str(final_list))


