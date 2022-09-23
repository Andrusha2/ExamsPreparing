for i in range(1, 100):
    b = str(bin(i))[2:]
    if i % 2 == 0:
        b = '10' + b
    else:
        b = '1' + b + '01'
    if int(b, 2) > 441:
        print(i)
        break
