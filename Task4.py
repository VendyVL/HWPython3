# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = int(input('Ввведите число '))
res = " "
while n > 0:
    res = str(n%2) + res # так сразу получается правильный порядок без переворачивания
    n = int(n/2)
print(res) 
