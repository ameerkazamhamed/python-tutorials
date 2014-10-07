buxfrom = {}
buxfrom['class-1hour'] = 1
buxfrom['class-4weeks'] = buxfrom['class-1hour'] * 1.5 * 4
buxfrom['greendot-1day'] = 1
buxfrom['greendot-4weeks'] = buxfrom['greendot-1day'] * 7 * 4
buxfrom['normal-4weeks'] = buxfrom['greendot-4weeks'] + buxfrom['class-4weeks'] 
buxfrom['normal-year'] = buxfrom['greendot-4weeks'] * 13

print(buxfrom)

buxfor = {}
buxfor['camp-1hour'] = 15
buxfor['class-1hour'] = 25
buxfor['camp-sat-minecraft'] = buxfor['camp-1hour'] * 2
buxfor['summer-camp-1week'] = buxfor['camp-1hour'] * 5 * 5
buxfor['summer-class-1week'] = buxfor['class-1hour'] * 5 * 5
buxfor['tshirt-normal'] = 17
buxfor['sticker-logo'] = 2
buxfor['sticker-bumper'] = 5
buxfor['items-redshelf-perdollar'] = 5

print(buxfor)

def bux2dollars(bux=1):
    return bux / buxfor['items-redshelf-perdollar']

def dollars2bux(dollars=1):
    return dollars * buxfor['items-redshelf-perdollar']
