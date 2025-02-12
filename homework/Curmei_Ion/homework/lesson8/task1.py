import random

salary = int(input("Write a salary: "))
bool_variable = [True, False]
bonus = random.choice(bool_variable)

if bonus:
    salary = salary + random.randrange(1, 1000)

print(f"Your salary is: {salary}")
