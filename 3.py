n = int(input())
c = 0
s = 0
for i in range(1, n+1):
    if i % 2 == 0:
        c += 1
    else:
        s += 1
print(f'{c} - кол-во четных чисел, {s} - кол-во нечетных чисел')