def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


list_index = [5, 200, 1000, 2000]

for index in list_index:
    fib_gen = fibonacci(index)
    fib_number = 0
    for num in fib_gen:
        fib_number = num
    print(f'Fibonaci({index}) = {fib_number}')
