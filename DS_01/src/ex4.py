def fib(n):
    result = 0
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib(n - 1) + fib(n - 2)
    return result

print(fib(27))