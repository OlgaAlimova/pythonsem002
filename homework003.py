# Задайте список из n чисел последовательности (1 + 1/n)^n.
# Вывестив консоль сам список и сумму его элементов.

n = int(input('Введите число n: '))
my_list = []
sum_element = 0.00
for i in range(1, n+1):
    sum_element = sum_element + (1 + (1 / n))**n
    my_list.append(f'{i} : {(1 + (1 / n))**n}')
print(*my_list, sep=', ')
print(sum_element)


