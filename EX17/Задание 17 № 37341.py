a = open('17 (4).txt', 'r')
a = a.readlines()
a = list(map(int, a))
b = 0
mx = 0
for i in range(len(a) - 1):
    for v in range(i + 1, len(a)):
        if (a[i] - a[v]) % 2 == 0 and (a[i] % 19 == 0 or a[v] % 19 == 0):
            b += 1
            if a[i] + a[v] > mx:
                mx = a[i] + a[v]
print(b, mx)
