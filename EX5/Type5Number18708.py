for i in range(1, 100):
    b = str(bin(i))[2:]
    for v in range(2):
        b += str(b.count('1') % 2)
    if int(b, 2) > 85:
        print(i)
        break
