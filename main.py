from time import sleep
try:
    from OS import os
    sleep(0.5)
    print('Loading Salmon OS kernel ')
    sleep(0.75)
    print('Version: 0.30')
    sleep(0.5)
except:
    print('Main Kernel loading failed!')
    sleep(1)
    choice = input('Load backup Kernel?')
    if choice == 'y':
        sleep(0.5)
        from Backup import os
        print('Loading backup Kernel')
        print('Version 0.30')
while True:
    os()
