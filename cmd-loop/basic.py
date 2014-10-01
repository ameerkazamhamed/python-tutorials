
def handle_blah(event):
    print(event)

handlers = {
    'blah': handle_blah
}

while True:
    cmdline = input()
    cmd = cmdline.split(' ', 1)[0]
    if cmd and cmd in handlers.keys():
        handlers[cmd](cmdline)
    

