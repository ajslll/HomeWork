n = int(input('Введите ширину треугольнка N: '))
row = 1
while row <= n:
    print((' ' * (n - row)) + '*' * row)
    row += 1
