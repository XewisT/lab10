"""
3. Сформувати функцію для обчислення індексу максимального елемента масиву
n*n, де 1<=n<=5.
"""
from random import randint
from timeit import timeit

def it(a): #ітерація
    for i in range(len(a)):
        if a[i] == max(a):
            return i
def tm(a): # a[1:] знаходить найбільше число всередині а. Потім залишається два елементи які оператор if порівнює і повертає найбільший
    if len(a) == 2:
        return a[1] if a[1] > a[0] else a[0]
    else:
        return tm([a[0], tm(a[1:])])
a = [randint(1, 5) ** 2 for x in range(10)]
print(a)
res = input('Настисніть r щоб обрати рекурсію, i - ітерацію: ')
if res == 'r':
    print(a.index(tm(a)))
elif res == 'i':
    print(it(a))
q = timeit('"-".join(str(n) for n in range(100))', number=10000)
print(q)
