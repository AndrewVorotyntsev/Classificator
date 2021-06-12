import matplotlib.pyplot as plt
import random

# Количество точек
amount_of_dots = 5

# Мат ожидание и дисперсия по оси x и y
# Чтобы добавить новые классы данных увеличить массивы
mu_x = [4, -5]
sigma_x = [1, 1]
mu_y = [4, 5]
sigma_y = [1, 1]

for k in range(len(mu_x)):
    x = []
    y = []

    # Генерируем случайные числа с заданными характеристиками и записываем в массив
    for i in range(amount_of_dots):
        x.append(round(random.normalvariate(mu_x[k], sigma_x[k]), 4))
        y.append(round(random.normalvariate(mu_y[k], sigma_y[k]), 4))

    print(x, y)

    # Открываем файл для записи
    file_name = "area" + str(k+1) + ".txt"
    file = open(file_name, "a")

    # В первую строку записываем значения по x
    for i in x:
        print(i)
        i = str(i) + " "
        file.write(i)
    file.write("\n")
    # Во вторую строку - значения по y
    for j in y:
        print(j)
        j = str(j) + " "
        file.write(j)


