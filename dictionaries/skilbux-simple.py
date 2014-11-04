buxfrom = {}
buxfrom['class-1hour'] = 1
buxfrom['class-4weeks'] = buxfrom['class-1hour'] * 1.5 * 4
buxfrom['greendot-1day'] = 1
buxfrom['greendot-4weeks'] = buxfrom['greendot-1day'] * 7 * 4
buxfrom['normal-4weeks'] = buxfrom['greendot-4weeks'] + buxfrom['class-4weeks'] 
buxfrom['normal-year'] = buxfrom['greendot-4weeks'] * 13
buxfrom['codestudio-port'] = 2
buxfrom['codestudio-intro'] = 30

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

def bux2dollars(bux=1):
    return bux / buxfor['items-redshelf-perdollar']

def dollars2bux(dollars=1):
    return dollars * buxfor['items-redshelf-perdollar']

def ask(text):
    return input(text).strip().lower()

def howmany():
    while True:
        try:
            total = 0
            attendance90 = int(ask('How many 90 minute regular classes have you attended since September 1st? '))
            attendance120 = int(ask('How many 2-hour regular classes have you attended since September 1st? '))
            greendots = int(ask('How many greendots do you have since September 1st? '))
            codestudiointro = ask('Have you completed the 20-hour Intro to Code at code.studio.org? ')
            codestudioports = int(ask('How many JavaScript-to-Python ports have you completed by yourself? '))
            total += attendance90 * buxfrom['class-1hour'] * 1.5
            total += attendance120 * buxfrom['class-1hour'] * 2
            total += greendots * buxfrom['greendot-1day']
            if codestudiointro.startswith('y'):
                total += buxfrom['codestudio-intro']
            total += codestudioports * buxfrom['codestudio-port'] 
            print('You have earned {} total SkilBux so far.'.format(total))
            return total
        except Exception:
            print("Let's try that again...")

if __name__ == '__main__':
    howmany()
