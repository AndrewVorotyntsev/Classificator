import utils
import random
import os.path


def create_initial_weight_matrix(quantity_of_neurons, number_of_inputs):
    initial_weight = []
    for i in range(0, quantity_of_neurons, 1):
        initial_weight.append([])
        for j in range(0, number_of_inputs, 1):
            initial_weight[i].append(round(random.uniform(-10,10), 4))
    return initial_weight


if os.path.exists("weights.txt"):
    next_step = input("Файл weights.txt существует, он будет перезаписан! Продолжить? \n"
                      "Введите любой символ для отмены или нажмите Enter для продолжения")
    if len(next_step) != 0:
        print("Инициализация отменена - выход из программы")
        raise SystemExit

weights = create_initial_weight_matrix(2, 2)

utils.write_array_to_file_in_many_lines(weights, "weights.txt")

print("\nНачальные веса заданы случайно и записаны в файл\nМожно приступать к обучению сети")
