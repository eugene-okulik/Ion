string = """
Etiam tincidunt neque erat, quis molestie enim imperdiet vel. 
Integer urna nisl, facilisis vitae semper at, dignissim vitae libero
"""

list_string = string.split()
new_list = []

for item in list_string:
    if item.endswith(',') or item.endswith('.'):
        item = item[:-1] + 'ing' + item[-1]
    else:
        item += 'ing'
    new_list.append(item)

new_string = ' '.join(new_list)
print(new_string)
