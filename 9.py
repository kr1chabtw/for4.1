m = int(input("Хав мач мани ду ю хэв? "))
n = int(input("Сколько вещичек хотите прикупить? "))
s = int(input("Скидка после покупки: "))
s *= .01
r = 0
for i in range(1, n+1):
    a = int(input(f'Сколько стоит {i} вещичка? '))
    a *= (1-r)
    r += s
    m -= a
    print(a)
print(f'{m} - оставшиеся мани')


