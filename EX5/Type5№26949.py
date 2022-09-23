for i in range(100, 1, -1):
    b = str(bin(i))[2:]
    if i % 2 == 0:
        b += '00'
    else:
        b += '11'
    if int(b, 2) < 94:
        print(i)
        break
