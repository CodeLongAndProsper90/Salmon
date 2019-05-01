def os():
  from time import sleep, time
  verson = '0.2.0'
  commands = ['exit', 'time', 'arch', 'help','man', 'version', 'nano', 'pi', 'copy filesys']
  command = input("user@salmonOs ~$")
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
        print(time())
      elif command  == commands[2]:
        error()
      elif command == commands[3]:
        print("Salmon Os commands")
        print(commands)
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
        print("3.1415265358979232846264338327950288419716939937510582097494450781640628620")
      elif command == commands[8]:
        file = input('What file to copy to?')
        copy('old.py', file)
    if command not in commands:
      print("Bash: command " + command +" not found")
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

  console()