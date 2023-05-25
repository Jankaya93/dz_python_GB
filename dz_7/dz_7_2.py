# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения. Начинать с 1!
# print_operation_table(lambda x, y: x * y)

def print_operation_table(operation, num_rows=6, num_columns=6):
    column_headers = [f"{column:>4d}" for column in range(1, num_columns + 1)]
    print("    ", *column_headers)
    print("   +" + "-" * (5 * num_columns))

    for row in range(1, num_rows + 1):
        row_values = [operation(row, column) for column in range(1, num_columns + 1)]
        print(f"{row:2d} |", *map(lambda value: f"{value:4d}", row_values))


multiply = lambda x, y: x * y
print_operation_table(multiply)