
class Handlers():
    
    def on_blah(event):
        print(event)

while True:
    cmdline = input()
    cmd = cmdline.split(' ', 1)[0]
    on_cmd = 'on_' + cmd
    if hasattr(Handlers,on_cmd):
        getattr(Handlers,on_cmd)(cmdline)
    

