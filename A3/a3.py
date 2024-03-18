x = int(input())
a = 0
b = [1]
if x == 1:
    print('yek')
else:
    for i in range(2, (x//2)+1):
        if x%i == 0:
            b += [i]
            a += 1
    b.append(x)        
    if a == 0:
        print('aval')
    else:
        print('morakab', '\nshomarande ha:',b)
