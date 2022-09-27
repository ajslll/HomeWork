n = int(input('Введите ширину треугольнка N: '))
row = 1
while row <= n:
    print((' ' * (row - 1)) + '*' * (n - row + 1))
    row += 1
