n = int(input())
for i in range(1, n+1):
    if 10<i<100:
        x = i//10
        y = i%10
        if x != y:
            print(i)
    elif 1e2 < i < 1e3:
        x = i // 100
        z = i % 100 // 10
        y = i % 10
        if x!=z and x!=y and y!=z:
            print(i)
    elif 1e3 < i < 1e4:
        x = i // 1000
        w = i % 1000 // 100
        z = i % 100 // 10
        y = i % 10
        if x != z and x != y and y != z and y != w and w != x and w != z:
            print(i)
    elif 1e4 < i < 1e5:
        x = i // 10000
        f = i % 10000 // 1000
        w = i % 1000 // 100
        z = i % 100 // 10
        y = i % 10
        if x != z and x != y and y != z and y != w and w != x and w != z and f != x and f != y and f != w and f != z:
            print(i)
    elif 1e5 < i < 1e6:
        x = i // 100000
        r = i % 100000 // 10000
        f = i % 10000 // 1000
        w = i % 1000 // 100
        z = i % 100 // 10
        y = i % 10
        if x!=z and x!=y and y!=z and y!=w and w!=x and w!=z and f!=x and f!=y and f!=w and f!=z and r!=x and r!=y and r!=z and r!=w and r!=f:
            print(i)




