def fibonacci(n):
    a, b = 0, 1
    count = 1
    while count <= n:
        yield a
        a, b = b, a + b
        count += 1


user_input = int(input("Introdu un numar: "))
fib_gen = fibonacci(user_input)
fib_number = 0
# save a N number of Fibonacci
for num in fib_gen:
    fib_number = num

print(f"Fibonacci({user_input}) = {fib_number}")
