n = int(input('Введите ширину треугольнка N: '))
row = 1
# 1)
while row <= n:
    print('*' * (n - row + 1))
    row += 1
