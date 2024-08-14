g = float(input('Введите градусы: '))

const = 1 / 120

seconds = g // const
minutes = seconds // 60 % 60
hours = seconds // 3600

print(f'Часы:{hours} Минуты:{minutes} Секунды:{seconds % 60}')
