s = int(input("По сколь биток продается? "))
a = int(input("На сколько процентов взлетит? "))
n = int(input("На сколько дней выдать курсы? "))
for i in range(1, n+1):
    s *= 1+(a*.01)
    print(round(s, 1))
