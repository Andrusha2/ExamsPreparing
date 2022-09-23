with open('17 (2).txt', 'r') as f:
    numbers = [int(x) for x in f.read().split('\n') if x]

count = 0
maximum = -1
for i in range(len(numbers) - 1):
    for j in range(i + 1, len(numbers)):
        if abs(numbers[i] - numbers[j]) % 2 == 0 and (numbers[i] % 31 == 0 or numbers[j] % 31 == 31):
            count += 1
            maximum = max(maximum, numbers[i] + numbers[j])
print(count)
print(maximum)
