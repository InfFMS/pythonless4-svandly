# Напишите функцию number_to_words(num), которая принимает
# в качестве аргумента натуральное число num и возвращает
# его словесное описание на русском языке.
#
# Примечание 1.
# Считайте, что число 1 ≤ num ≤ 99.
#
# Примечание 2.
# Следующий программный код:
#
# print(number_to_words(7))
# print(number_to_words(85))
# должен выводить:
#
# семь
# восемьдесят пять
n = 1
def number_to_words(num):
    edinici = ["один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    desatki = ["двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
    pricol = ["десять","одинадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
    if (num < 1) or (num > 99):
        print("Ошибка")
    if num // 10 > 1:
        n = (num // 10) - 2
        m = (num % 10) - 1
        print(desatki[n], edinici[m])
    elif num // 10 == 1:
        n = (num % 10)
        print(pricol[n])
    else:
        n = (num % 10) - 1
        print(edinici[n])
num = int(input())
number_to_words(num)