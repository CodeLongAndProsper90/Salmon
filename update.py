def os():
  from time import sleep, time
  from patch import update
  commands = ['exit','time' , 'arch', 'help','man', 'version', 'nano', 'pi', 'copy filesys' , 'update']
  command = input('Scott' +"@salmonOs ~$")
  def console():
    def copy(image, file):
      os = open(file, 'w')
      os.write('')
      os.close()
      os = open(file, 'a')
      updte = open(image, 'r')
      for line in updte:
        patch = updte.readline()
        os.write(patch)
    def error():
      print("ERROR 001")
    if command in commands:
      if command == commands[0]:
        print('stopping Salmon Kernel')
        sleep(0.5)
        print("Exiting trinket.io interface")
        exit()
      elif command == commands[1]:
        print("Salmon has encountered an error and needs to restart.")
      elif command == commands[3]:
        print("Salmon Os commands")
        print(commands)
      elif command == commands[4]:
        man()
      elif command == commands[5]:
        version = 0.26
        print(version)
      elif command == commands[7]:
        print("3.1415265358979232846264338327950288419716939937510582097494450781640628620")
      elif command == commands[8]:
        file = input('What file to copy to?')
        copy('OS.py', file)
      elif command == commands[9]:
        update()
    if command not in commands:
      print("Bash: command " + command +" not found")
    def man():
      page = input("What command to look up?")
      if page in commands:
        if page == commands[0]:
          print("exit Salmon OS")
        #elif page == commands[1]:
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

  console()

