def decorator_calc(func):
    def wrapper(first, second, operation):

        if first < 0 or second < 0:
            operation = '*'
        elif first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        elif second > first:
            operation = '/'

        return func(first, second, operation)

    return wrapper


@decorator_calc
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        if second != 0:
            return first / second
        else:
            return "Don't will be devided by zero "
    else:
        return 'unknow operation'


number1 = int(input("Introduction first number: "))
number2 = int(input("Introduction second number: "))

res = calc(number1, number2, "")
print(f"rezultatul operatiei este : {res}")
