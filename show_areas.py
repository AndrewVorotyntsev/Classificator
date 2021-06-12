import utils
import matplotlib.pyplot as plt


x = [utils.read_file_to_two_dimensional_array_of_floats("area1.txt"),
     utils.read_file_to_two_dimensional_array_of_floats("area2.txt")]  # 2 x 2 x amount_of_dots
w = utils.read_file_to_two_dimensional_array_of_floats("weights.txt")  # 2 x 2

# Подаем на вход рандомную точку
area_to_analyze = 0
point_to_analyze = 0

plt.axis([-10, 10, -10, 10])
plt.grid(True)
# Исходные точки
plt.plot(x[0][0], x[0][1], 'o', c="r")
plt.plot(x[1][0], x[1][1], 'o', c="b")
# Веса
plt.plot([w[0][0]], [w[0][1]], 'o', color="orange")
plt.plot([w[1][0]], [w[1][1]], 'o', color="yellow")

# Входной вектор
plt.quiver([0], [0], x[area_to_analyze][0][point_to_analyze], x[area_to_analyze][1][point_to_analyze], angles='xy', scale_units='xy', scale=1, color="purple")
# Векторы весов
plt.quiver([0], [0], [w[0][0]], [w[0][1]], angles='xy', scale_units='xy', scale=1, color="orange")
plt.quiver([0], [0], [w[1][0]], [w[1][1]], angles='xy', scale_units='xy', scale=1, color="yellow")


# TODO: добавить вектор-разницу

plt.show()
