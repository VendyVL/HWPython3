# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

list1 = [2, 3, 5, 9, 3]

def fun(list):
    res = 0
    for i in range (1, len(list)):
        if i%2!=0:
            res = res + list[i]
    return res

print(list1)
print(fun(list1))