# Напишите процедуру, которая принимает параметр – натуральное число N –
# и выводит на экран треугольник из * с катетами равными N.
# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *********
# **********
def treugolnic(N):
    T=("*")
    n = 1
    while ( n<N + 1 ):
        print (T*n)
        n += 1
N = int(input())
treugolnic(N)