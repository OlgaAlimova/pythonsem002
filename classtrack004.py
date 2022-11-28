# 1. Напишите программу, которая принимает на вход число N
# и выдаёт последовательность из N членов.
#
# *Пример:*
#
# - Для N = 5: 1, -3, 9, -27, 81

num = int(input('Введите число: '))
my_list = [1]

for i in range(num-1):
    my_list.append(my_list[i]*-3)
print(*my_list, sep=', ')

my_list2 = []
for i in range(num):
    my_list2.append((-3) ** i)
print(*my_list2, sep=', ')

a = 1
for i in range(num):
    print(a, end=', ')
    a *= -3