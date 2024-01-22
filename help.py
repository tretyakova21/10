def func1(*args):
    print("Значения аргументов:")
    for arg in args:
        print(arg)

def print_name_and_age():
    name = input("Введите имя: ")
    age = input("Введите возраст: ")
    print(f"Имя: {name}")
    print(f"Возраст: {age}")

def is_king_move_possible():
    start_col = int(input("Введите номер столбца для первой клетки (от 1 до 8): "))
    start_row = int(input("Введите номер строки для первой клетки (от 1 до 8): "))
    end_col = int(input("Введите номер столбца для второй клетки (от 1 до 8): "))
    end_row = int(input("Введите номер строки для второй клетки (от 1 до 8): "))

    col_diff = abs(start_col - end_col)
    row_diff = abs(start_row - end_row)

    return col_diff <= 1 and row_diff <= 1

def add_lists_by_index():
    list1 = [int(x) for x in input("Введите элементы первого списка через пробел: ").split()]
    list2 = [int(x) for x in input("Введите элементы второго списка через пробел: ").split()]

    result_list = [list1[i] + list2[i] for i in range(min(len(list1), len(list2)))]
    result_list.extend(list1[len(result_list):] + list2[len(result_list):])
    return result_list

def calculation():
    var1 = int(input("Введите первую переменную: "))
    var2 = int(input("Введите вторую переменную: "))

    addition_result = var1 + var2
    subtraction_result = var1 - var2
    return addition_result, subtraction_result

# Пример использования
func1(1, 'abc', 3.14, [4, 5])

print_name_and_age()

if is_king_move_possible():
    print("YES")
else:
    print("NO")

result_list = add_lists_by_index()
print("Список, полученный путем сложения по индексу:", result_list)

addition_result, subtraction_result = calculation()
print(f"Результат сложения: {addition_result}")
print(f"Результат вычитания: {subtraction_result}")
