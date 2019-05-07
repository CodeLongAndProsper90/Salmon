from time import sleep
print("Use 'help' for commands")
try:
    from OS import os
    print('Loading Salmon OS kernel ')
    sleep(0.75)
    sleep(0.5)
    print('Version: 0.30')
    sleep(0.5)
except:
  
    print('Main Kernel loading failed!')
    sleep(1)
    choice = input('Load backup Kernel?')
    choices = ['yes', 'no']
    while choice not in choices:
      print('yes or no')
      choice = input('Load backup Kernel?')

    if choice == 'yes':
        sleep(0.5)
        from update import os
        print('Loading backup Kernel')
        print('Version 0.30')
    elif choice == 'no':
      print('Loading aborted!')
      sleep(1)
      print("Salmon os has encountered a fatal execption and needs to be repaired or redownloaded! ")
      sleep(1)
      print("DANGER! The salmon Os kernel is damaged or missing! DANGER")
      sleep(2)
      exit()
      

while True:
    os()
