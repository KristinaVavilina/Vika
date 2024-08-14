a = [[1, 10, 5],
    [-5, 0, 10],
    [-12, -1, 9],
    [8, 8, 4]]
count = 0

for string in a:
    print("Строка:", string)

    for number in string:
        print("Число:", number)

        if number < 0:
            count += 1
print("Кол-во отрицательных чисел:", count)
