x = int(input('Enter a number'))
a = 0
b = 1

for i in range(1, x+1):
    print(a, end = ",")
    c = a+b
    a = b
    b = c


