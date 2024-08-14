a = int(input())
b = int(input())
s = []
if a>b:
    for i in range (1, b+1):
        if b % i == 0 and a % i ==0:
            s.append(i)
if b>a:
    for i in range(1,a+1):
        if a % i ==0 and b % i ==0:
           s.append(i)
print(max(s))
