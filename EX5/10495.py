a = int(input())
b = 0
c = 0
while b < a:
    b = 0
    c += 1
    b = c
    for i in range(2):
        if sum(list(map(int, bin(b)[2:]))) % 2 != 0:
            b <<= 1
            b |= 1
        else:
            b <<= 1
print(c)
