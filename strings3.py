def pos(n):
    for i in range(n-1, -1, -1):
        print(i, end=' ')

def neg(n):
    for i in range(n, 1):
        print(i, end=' ')

n = 0
if n == 0:
    print("already Zero")
elif n > 0:
    pos(n)
else:
    neg(n)