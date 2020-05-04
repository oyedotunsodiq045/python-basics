apples = {
    'cox': 17,
    'royal blue': 22,
    'go gaga': 33,
    'red army': 47,
    'spring green': 57,
    'musty': 66
}

cox_stock = apples['cox']
print('We\'ve ' + str(cox_stock) + ' cox apples')

for apple in apples.keys():
    print(apple)


for apple, stock_count in apples.items():
    print('We\'ve ' + str(stock_count) + ' ' + apple + ' apples')


mac_apples = apples.get('macintosh', 1)
print(mac_apples)
