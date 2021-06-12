def write_array_to_file_in_many_lines(array_to_read, file_name):
    file_to_write = open(file_name, "w")
    for i in range(len(array_to_read)):
        # Для загрузки в несколько строк объявляем переменную строки после запуска цикла
        line = ""
        for j in range(len(array_to_read[i])):
            line = line + str(array_to_read[i][j]) + " "
        line = line.strip(" ") + "\n"
        file_to_write.write(line)


def multiply_matrices(a, b):
    result = []
    res = 0
    for i in range(len(b)):
        for j in range(len(a)):
            res = res + a[j]*b[i][j]
        result.append(round(res, 4))
        res = 0
    return result


def multiply_vectors(a, b):
    pass

def read_file_to_one_dimensional_array_of_floats(file_name):
    array_to_write = []
    with open(file_name) as f:
        for line in f:
            for x in line.split():
                array_to_write.append(float(x))
    return array_to_write


def read_file_to_two_dimensional_array_of_floats(file_name):
    array_to_write = []
    with open(file_name) as f:
        for line in f:
            array_to_write.append([float(x) for x in line.split()])
    return array_to_write


