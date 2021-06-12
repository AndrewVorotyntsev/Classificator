import utils


# Сложение изначального вектора с разницей умноженной на темп
def adding_vectors(a, b):
    pace = 0.5
    return [a[0] + b[0] * 0.5, a[1] + b[1] * pace]


# Вычитание векторов по правилу треугольника
def subtracting_vectors(a, b):
    return [a[0] - b[0], a[1] - b[1]]


# TODO: добавить возможность обрабатывать произвольное количество классов данных
# Количество классов данных следует задавать при инициализации нейросети (в init и generator)
x = [utils.read_file_to_two_dimensional_array_of_floats("area1.txt"),
     utils.read_file_to_two_dimensional_array_of_floats("area2.txt")]  # 2 x 2 x amount_of_dots
w = utils.read_file_to_two_dimensional_array_of_floats("weights.txt")  # 2 x 2

# Перемножение матриц 2 * 2
# Получаем число, добавляем его в массив


# Подаем на вход рандомную точку
area_to_analyze = 1
point_to_analyze = 4
#area_to_analyze = int(input("Введите область для анализа"))
#point_to_analyze = int(input("Введите точку для анализа"))

input_data = [x[area_to_analyze][0][point_to_analyze], x[area_to_analyze][1][point_to_analyze]]


z = utils.multiply_matrices(input_data, w)


# Выбираем победителя

win = int(z[1] > z[0])
print("Win", win)

# Подкрутка весов
u = subtracting_vectors(input_data, w[win]) # Получаем разницу между входным и весовым вектором

w[win] = adding_vectors(w[win], u)

utils.write_array_to_file_in_many_lines(w, "weights.txt")
