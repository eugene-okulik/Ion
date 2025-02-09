msg1 = 'result of operation: 42'
msg2 = 'result of operation: 514'
msg3 = 'result of operation: 9'

# find the index of number
find_number_msg1 = msg1.index('42')

# add the number in variable
number_msg1 = int(msg1[find_number_msg1:]) + 10
new_msg1 = f'{msg1[:find_number_msg1]}{number_msg1}'

# find the index of number
find_number_msg2 = msg2.index('514')

# add the number in variable
number_msg2 = int(msg2[find_number_msg2:]) + 10
new_msg2 = f'{msg2[:find_number_msg2]}{number_msg2}'

# find the index of number
find_number_msg3 = msg3.index('9')

# add the number in variable
number_msg3 = int(msg3[find_number_msg3:]) + 10
new_msg3 = f'{msg3[:find_number_msg3]}{number_msg3}'

print(new_msg1)  # result of operation:  52
print(new_msg2)  # result of operation:  52
print(new_msg3)  # result of operation:  52
