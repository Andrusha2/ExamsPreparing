for i in range(1, 100):
    b = str(bin(i))[2:]
    if b.count('1') % 2 == 0:
        b += '0'
        b = b.replace(b[:2], '10', 1)
    else:
        b += '1'
        b = b.replace(b[:2], '11', 1)
    if int(b, 2) > 40:
        print(i)
        break
