msg1 = 'result of operation: 42'
msg2 = 'result of operation: 514'
msg3 = 'result of operation: 9'
"""
# extracting number from string
list_msg1 = msg1.split(" ")
number_msg1 = int(list_msg1[-1])

list_msg2 = msg2.split(" ")
number_msg2 = int(list_msg2[-1])

list_msg3 = msg3.split(" ")
number_msg3 = int(list_msg3[-1])

print('result of operation:', number_msg1 + 10)
print('result of operation:', number_msg2 + 10)
print('result of operation:', number_msg3 + 10)
"""

index_number_msg1 = msg1.index(':') + 2
number_msg1 = int(msg1[index_number_msg1:])

index_number_msg2 = msg2.index(':') + 2
number_msg2 = int(msg2[index_number_msg2:])

index_number_msg3 = msg3.index(':') + 2
number_msg3 = int(msg3[index_number_msg3:])

print('result of operation:', (number_msg1 + 10))
print('result of operation:', (number_msg2 + 10))
print('result of operation:', (number_msg3 + 10))
