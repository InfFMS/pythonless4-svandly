# Напишите функцию, которая находит
# наибольший общий делитель двух натуральных чисел
# На входе два числа, на выходе их НОД.
def nod(a, b):
    if a > b:
        l = a
    else:
        l = b
    while l > 0:
        d = a % l
        j = b % l
        if (d == 0) and (j == 0):
            print (l)
            break
        l -= 1
a = int(input())
b = int(input())
nod(a, b)
