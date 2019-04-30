from time import time, sleep
salmon = True
verson = '0.1.1'
print("GNU/Salmon comes with NO warrenty!")
print("Enter help for commands")
commands = ['exit', 'time', 'arch', 'help','man', 'version', 'nano', 'pi', 'admin', 'rollback', 'source']
def man():
  page = input("What command to look up?")
  if page in commands:
    if page == commands[0]:
      print("exit Salmon OS")
    elif page == commands[1]:
      print("Returns the number of seconds from the Epoch")
    elif page == commands[2]:
      print("Returns the system archecture")
    elif page == commands[3]:
      print("Print the available commands")
    elif page == commands[4]:
      print("You're here!")
    elif page == commands[5]:
      print("Prints the Current Salmon verson")
    elif page == commands[6]:
      print("Salmon Os file editor")
    elif page == commands[7]:
      print("Print pi")
    elif page  == commands[8]:
      print("This is texas. Don't mess with it")
time = 0
def pi():
  print("Salmon Os commands:")
  print(commands)
def error():
  print("ERROR 001: THIS OS IS CURRENTLY IN DEVELPMENT. WAIT FOR THIS COMMAND TO BE CODED")
def login():
  user = input('user')
  if user == 'scott':
    operator = 'scott'
def console():
  command = input("scott@salmonOs ~$")
  if command in commands:
    if command == commands[0]:
      print('stopping Salmon Kernel')
      sleep(0.5)
      print("Stopping anomalous Doge")
      sleep(.05)
      print("Exiting trinket.io interface")
      exit()
    elif command == commands[1]:
      print(time())
    elif command  == commands[2]:
      print("x64")
    elif command == commands[3]:
      pi()
    elif command == commands[4]:
      man()
    elif command == commands[5]:
      print(verson)
    elif command == commands[6]:
      filename = input("Filename?")
      choice = input("Read or Write?")
      choice = choice.lower()
      if choice == "Write":
        file = open(filename, 'a')
        text = input("What do you want to write?")
        file.write(text)
        file.close()
      elif choice == "Read":
        print("Danger! This feature is unstable. Just open the file.")
        file = open(filename, 'r')
        text = file.read()
        print(text)
        file.close()
    elif command == commands[7]:
      print('3.141592653589793238462643383279502884197169399375105820974944592307816')
    elif command == commands[8]:
      adcmd = input("run update or change version")
      adcmd = adcmd.lower()
      if adcmd == 'update':
        print("DANGER! TURN BACK NOW! DANGER!")
      elif adcmd == 'version':
        ver = input("What Version to change to?")
        version = ver
    elif command == commands[9]:
      print("https://k1206150-students-katyisd-org.trinket.io/sites/salmon-os-rollback")
    elif command == commands[10]
    print("")
  if command not in commands:
    print("Bash:" + command +" not found")
while salmon == True:
  console()
