from time import sleep
login = False
sudo = False
version = '0.5.fish'
print("Salmon OS running Cod firmware with penguins")
print("Use 'help' for commands")
user = input("Username?")
users = ['codelongandprosper', 'crash', 'icey']
user = user.lower()
passwords = ['ktel2345', 'Fish', 'abla']
passwords[0] = '8t8mph'
passwords[1] = 'evil penguin minions'
if user in users:
  password = input('Password?')
  if user == users[0]:
    if password == passwords[1]:
      login = True
      sudo = True
    else:
      login == False
      exit()
  if user == users[1]:
    if password == passwords[0]:
      login = True
    else:
      login = False
      exit()
  if user == users[2]:
    if password == passwords[2]:
      login = True
    else:
      login = False
      exit()
else:
  login = False
  print("You are not in the list of Comrades!")
  exit()
try:
    from kernel import os
    print('Loading Salmon OS kernel ')
    sleep(0.75)
    sleep(0.5)
    print('Version ' + version)
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
        print('Version ' + version)
    elif choice == 'no':
      print('Loading aborted!')
      sleep(1)
      print("Salmon os has encountered a fatal execption and needs to be repaired or redownloaded! ")
      sleep(1)
      print("DANGER! The salmon Os kernel is damaged or missing! DANGER")
      sleep(2)
      exit()
      

while login != False:
    os(user, version, sudo)
    os(user, version)
