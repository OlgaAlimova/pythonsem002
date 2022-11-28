# Реализуйте алгоритм перемешивания списка. Встроенный
# алгоритм SHUFFLE не использовать! Реализовать свой метод

import random

def randomlist(mylist):
    new_randomlist = []
    while len(mylist):
        index = random.randrange(0, len(mylist))
        new_randomlist.append(mylist.pop(index))
    return new_randomlist

n  = int(input('Введите длину списка: '))
my_list = []
for i in range(n):
    element = input(f'Введите {i} элемент списка: ')
    my_list.append(f'{i} : {element}')
print(my_list)
print(randomlist(my_list))

