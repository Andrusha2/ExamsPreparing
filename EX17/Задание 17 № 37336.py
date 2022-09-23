f = open('17.txt', 'r')
a = f.readlines()
a = list(map(int, a))
print(a)
mx = 0
counter = 0
for i in range(1, len(a)):
    v = i - 1
    if a[v] % 3 == 0 or a[i] % 3 == 0:
        counter += 1
        if a[v] + a[i] > mx:
            mx = a[v] + a[i]
print(counter, mx)
