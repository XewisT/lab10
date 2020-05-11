"""
 2. Сформувати функцію для обчислення цифрового кореню натурального числа.
 Цифровий корінь отримується наступним чином: необхідно скласти всі цифри заданого
 числа, потім скласти всі цифри знайденої суми і повторювати процес до тих пір, поки
 сума не буде дорівнювати однозначному числу, що і буде цифровим коренем заданого
 числа.
"""
from timeit import timeit
def Summa(x): #складаємо всі цифри заданого числа, поки воно не стане однозначним
    if x < 10:
        return x
    else:
        return x % 10 + Summa(x // 10)

def Root(x):
    if x < 10:
        return x
    else:
        return Root((Summa(x)))

def TmSumma(x):
    a = 0
    for i in range(x):
        a += x % 10
        x //= 10
    return a

def TmRoot(x):
    while x > 9:
        i = int(x % 10)
        x = x // 10
        x = x + i
    return x

x = int(input('Введіть число: '))
res = input('Настисніть r щоб обрати рекурсію, i-ітерацію: ')
if res == 'r':
    print(x, Summa(x), Root(x))
elif res == 'i':
    print(x, TmSumma(x), TmRoot(x))
q = timeit('"-".join(str(n) for n in range(100))', number=10000)
print(q)
