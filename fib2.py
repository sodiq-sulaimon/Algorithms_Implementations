def fib2(n):
    if n == 0:
        return 0
    # create an array for 0,...n
    f = [i for i in range(n+1)]
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]

f1 = fib2(100)
print(f1)