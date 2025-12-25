PRICE_LIST = """
caiet  50p
carte  200p
pix  100p
creion  70p
album  120p
penal  300p
geanta  500p
"""
list_price_list = PRICE_LIST.split()
new_dict = {
    list_price_list[x]: list_price_list[x + 1]
    for x in range(0, len(list_price_list), 2)
}

print(new_dict)
