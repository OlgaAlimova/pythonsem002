# Напишите программу, в которой пользователь будет задавать две
# строки, а программа - определять количество вхождений одной строки в другой.

str1 = input('Введите 1 строку: ')
str2 = input('Введите 2 строку: ')
n = 0
for i in range(len(str1)):
    if str1[i:i+len(str2)] == str2:
        n += 1
print(f'Подстрока {str2} встречается в строке ' f' {str1} {n} раз')


