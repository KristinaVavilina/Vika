for i in range(1, 26):
    if i % 2 == 0:
        print(i // 2, end=' ')
    else:
        print('*', end=' ')
    if i % 5 == 0:
        print()
