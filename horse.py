x = int(input("Введите координату коня Х: "))
y = int(input("Введите координату коня У: "))
ax = int(input("Введите координату точки Х: "))
ay = int(input("Введите координату точки У: "))

if abs(ax-x) == 1 and abs(ay-y) == 2 or abs(ax-x) == 2 and abs(ay-y) == 1:
    print('Да', ax, ay)
else:
    print('Нет')
