"""
1. Сформувати функцію, що буде обчислювати факторіал
заданого користувачем натурального числа n.
"""
from timeit import timeit   #Імпортуєм timeit
def tm(x):                     #Pекурсія
    if x == 0:
        return 1
    else:
        return x * tm(x - 1)

def it(x):                      #Iтерація
    a = 1
    for i in range(1, x + 1):
        a *= i
    return a
res = input('Настисніть r щоб обрати рекурсію, i - ітерацію: ')
x = int(input('Введіть число: '))
if res == 'r':
    print(x, tm(x))
elif res == 'i':
    print(x, it(x))
q = timeit('"-".join(str(n) for n in range(100))', number = 10000)
print(q)
