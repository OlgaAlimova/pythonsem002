# Написать программу, которая состоит 4 из этапов:
# - создает список из рандомных четырех значных чисел
# - принимает с консоли цифру и удаляет ее из всех элементов списка
# - цифры каждого элемента суммирует пока результат не станет однозначным числом
# - из финального списка убирает все дублирующиеся элементы
# - после каждого этапа выводить результат в консоль
# Пример:
# - 1 этап: [2634, 6934, 7286, 3353, 4602, 3176, 3796]
# - 2 этап: Введите цифру: 3
# - 2 этап: [264, 694, 7286, 5, 4602, 176, 796]
# - 3 этап: 264 -> 2+6+4 -> 12 -> 1+2 -> 3
# - 3 этап: [3, 1, 5, 5, 3, 5, 4]
# - 4 этап: [3, 1, 5, 4]

import random

#step1

count = int(input('Введите количество элементов списка: '))
my_list = []
for i in range(count):
    my_list.append(random.randint(1000, 9999))
print(my_list)

#step2

n = int(input('Введите число, которое нужно удалить: '))
for i in range(count):
    number = 0
    s = my_list[i]
    k = 0
    for j in range(4):
        num = s % 10
        # print(num)
        if num != n:
            number = number + num * (10**k)
            # print(number)
            s = s // 10
            k += 1
            # print(s)
        else:
            s = s // 10
            # print(s)
            continue
        # print(f'Цикл выполнился {j} раз')
    else:
        my_list[i] = number
print(my_list)

#step3

new_list = []
for m in range(count):
    sum_digits = 0
    dig_sum = 0
    p = my_list[m]
    while(p):
        sum_digits += p % 10
        p = p // 10
        # print(sum_digits, p)
        continue
    else:
        t = 0
        while sum_digits > 9:
            dig_sum += sum_digits % 10
            sum_digits = sum_digits // 10
        else:
            dig_sum += sum_digits
            if dig_sum > 9:
                dig_sum = ((dig_sum % 10) + (dig_sum // 10))
            new_list.insert(count - t, dig_sum)
            continue
        t += 1
print(new_list)

#step4

fin_list = []
for w in new_list:
    if w not in fin_list:
        fin_list.append(w)
print(fin_list)


