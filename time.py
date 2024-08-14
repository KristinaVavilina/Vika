time1 = input('Введите первый момент времени: ')
time2 = input('Введите второй момент времени: ')

time1 = time1.split(':')
time2 = time2.split(':')

h1, m1, s1 = int(time1[0]), int(time1[1]), int(time1[2])
h2, m2, s2 = int(time2[0]), int(time2[1]), int(time2[2])

hours = abs(h2 - h1) * 3600
minutes = abs(m2 - m1) * 60
seconds = abs(s2 - s1)

print(hours + minutes + seconds, 'секунд')
