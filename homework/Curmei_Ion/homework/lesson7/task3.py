msg1 = 'result of operation: 42'
msg2 = 'result of the program: 54'
msg3 = 'result of operation: 209'
msg4 = 'result: 2'


def add_number_msg(message):
    """
    this function return the number in the string and add 10 value
    :param message:
    :return:
    """
    list_message = message.split()
    number_mesage = int(list_message[-1]) + 10
    print(number_mesage)


add_number_msg(msg1)
add_number_msg(msg2)
add_number_msg(msg3)
add_number_msg(msg4)
