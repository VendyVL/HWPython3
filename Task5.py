# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input('Ввведите число '))

def fib(n):
    fib = [0, 1, 1]
    a = 0
    b = 1
    for i in range (2, n+1):
        summ = a+b
        a = b
        b = summ
        fib.append(summ)
        i+=1
    return fib

def round(list):
    res = []
    a = len(list)
    while a!=1:
        if a%2 == 0:
            res.append(-list[a-1])
        else:
            res.append(list[a-1])
        a = a - 1
    return res
list = round(fib(n))
list.extend(fib(n))
print(list)

