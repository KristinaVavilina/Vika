num = int(input('Введите номер урока: '))
time = 0

for current_num in range(1, num + 1):
    time = time + 45

    if current_num != 1:
        if current_num % 2 == 0:
            time = time + 5
        else:
            time = time + 15

hours = "{:02d}".format(9 + time // 60)
minutes = "{:02d}".format(time % 60)

print(f'{hours}:{minutes}')
