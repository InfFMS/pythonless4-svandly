# Напишите функцию, которая сокращает дробь вида M/N.
# Где M и N - наутральные числа.
# В качестве аргументов она принимает числитель и знаменатель,
# выводит числитель и знаменатель после сокращения
#
# Пример:
# Ввод:
# 25 15
# Вывод:
# 5 3
def delenie(a,b):
    d=0
    c=1
    h=1
    if a > b:
        d = int(b)
    if a < b:
        d = int(a)
    while (d > 0):
        if (a % d == 0) and (b % d == 0):
            c = a/d
            h = b/d
            break
        else:
            d -= 1
    print (c, h)
a = int(input())
b = int(input())
delenie(a,b)