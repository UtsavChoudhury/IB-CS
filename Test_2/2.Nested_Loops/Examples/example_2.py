numbers = [7, -5, 11, 6]

i = 0

while i < len(numbers):
    j = i + 1
    while j < len(numbers):
        if numbers[j] < numbers[i]:
            t = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = t
            # OR (numbers[i], numbers[j] = numbers[j], numbers[i])
        j += 1
    i += 1

print(numbers)