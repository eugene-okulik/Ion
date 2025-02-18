def fibonacci(n):
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


count = 0

for num in fibonacci(10000000000000000000000000000000):
    if count == 5:
        print(num)
    elif count == 200:
        print(num)
    elif count == 1000:
        print(num)
    elif count == 100000:
        print(num)
        break
    count += 1
