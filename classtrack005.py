# 2. Для натурального n создать словарь индекс-значение,
# состоящий из элементов последовательности 3n + 1.
#
# *Пример:*
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input('Введите значение n = '))
my_list = []
for i in range(1, n+1):
    my_list.append(f'{i} : {3*i+1}')
print(*my_list, sep=', ')


d = {}
for j in range(1, n + 1):
    d[j] = 3 * j + 1
print(d)
