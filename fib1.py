def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
fib1 = fibonacci(35)
print(fib1)