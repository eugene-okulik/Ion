import datetime

data = 'Jan 15,2023 - 12:05:33'
python_data = datetime.datetime.strptime(data, '%b %d,%Y - %H:%M:%S')
print(python_data.strftime('%B'))
print(python_data.strftime('%d.%m.%Y,%H:%M'))
print()
temperatures = [
    20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32,
                30, 28, 24, 23
    ]


def is_high(x):
    return x > 28


new_temperatures = list(filter(is_high, temperatures))
average_temperatures = (sum(temperatures) / len(temperatures))

print(f'maxim temperatures is: {max(temperatures)}')
print(f'minim temperatures is: {min(temperatures)}')
print(f'average temperatures is: {round(average_temperatures, 2)}')
