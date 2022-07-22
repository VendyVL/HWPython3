# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list1 = [1.1, 1.24, 3.1, 5.59, 10.01]

def des(list):
    res = []
    for i in range (0, len(list)):
        res.append(round(list[i]%1, 2))
    return res

list2 = des(list1)

print(list2)

def maxmin(list):
    max = list[0]
    min = list[0]
    for i in range (0, len(list)):
        if list[i] > max: max = list[i]
        if list[i] < min: min = list[i]
    return [max, min]

list3 = maxmin(list2)
print(list3)
print(list3[0]-list3[1])

# пожалуй, можно было короче