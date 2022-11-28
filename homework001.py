# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

num = input('Введите число: ')
sum = 0
for i in range(len(num)):
    if num[i] == '.':
        num = num.replace('.', ',')
    # print(num)
    if num[i] != (','):
        sum += int(num[i])
print(f' Сумма всех цифр числа = {sum}')


number = input('Введите число: ')
n = len(number)
summa = 0
num = float(number)
for i in range(n):
    num = num * 10
num = int(num)
# print(f'num = {num}')
for i in range(2*n):
    s = num % 10
    # print(s)
    num = int(num) / 10
    # print(num)
    summa += int(s)
    # print(summa)
print(f' Сумма всех цифр числа = {summa}')


