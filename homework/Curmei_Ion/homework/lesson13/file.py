import datetime
import os
from os import WCONTINUED

base_path = os.path.dirname(__file__)

homework_path = os.path.dirname(os.path.dirname(base_path))
ion_path = os.path.dirname(homework_path)

eugen_path = os.path.join(ion_path, 'eugene_okulik/hw_13', 'data.txt')
new_eugehn_path = os.path.join(ion_path, 'eugene_okulik/hw_13', 'data1.txt')


def read_file():
    with open(eugen_path, 'r') as data_file:
        for line in data_file.readlines():
            yield line


with open(new_eugehn_path, 'w') as new_file:
    for line in read_file():
        try:
            defix = line.find(' - ')
            number_2 = line.find('2023')
            str_data = line[number_2:defix]
            python_data = (datetime.datetime.strptime(str_data, '%Y-%m-%d %H:%M:%S.%f'))
            date_time = python_data + datetime.timedelta(weeks=1)
            new_file.write(date_time.strftime('%Y-%m-%d %H:%M:%S.%f') + '\n')
            week_day = python_data
            new_file.write(week_day.strftime('%A') + '\n')

            now = datetime.datetime.now()
            last_date = str((now - python_data))

            new_file.write(last_date + '\n')

        except ValueError:
            continue

"""
new file
2023-12-04 20:34:13.212967
Monday
467 days, 17:29:20.679632
2023-07-22 18:25:10.121473`
Saturday
602 days, 19:38:23.771158
2023-06-19 15:23:45.312167
Monday
635 days, 22:39:48.580485
"""
