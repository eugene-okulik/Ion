def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


for i in 5, 200, 1000, 2000:
    fib_gen = fibonacci(i)
    fib_number = 0
    for num in fib_gen:
        fib_number = num
    print(f'Fibonaci({i}) = {fib_number}')
