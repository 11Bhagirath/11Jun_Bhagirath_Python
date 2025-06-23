'''for r in range(1,6):
    for c in range(r):
        print(r,end=" ")
    print(" ")'''

'''for r in range(1,6):
    for c in range(r):
        print(c+1,end=" ")
    print(" ")'''

'''p=1
for r in range(1,6):
    for c in range(r):
        print(p,end=" ")
        p+=1
    print(" ")'''

p = 1
for r in range(1, 6):
    print(*range(p, p := p + r))
