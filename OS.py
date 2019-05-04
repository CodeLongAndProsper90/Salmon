def os():
    from time import sleep
    from os import uname
    platform = []
    platform = uname()
    op = platform[0]
    username = platform[1]
    arch = platform[4]

    #Insert your name down here |
    #          V------------------
    user = 'Scott'
    commands =['exit', 'time', 'help', 'man', 'version' ,'pi', 'halt', 'arch',]
    command = input(user +"@salmonOs ~$")
    def console():
        def man():
          page = input("What command to look up?")
          if page in commands:
            if page == commands[0]:
              print("Halt Salmon OS")
            elif page == commands[1]: 
              print("Returns the time")
            elif page == commands[2]:
              print("Print the available commands")
            elif page == commands[3]:
              print("You're here!")
            elif page == commands[4]:
              print("Prints the Current Salmon verson")
            elif page == commands[5]:
              print("Prints pi")
            elif page == commands[6]:
              print('Use this command to force a system halt')
            elif page == commands[7]:
              print("Gives you info about the system Salmon os is running on.")
        def error(message, number):
            
          print("ERRORNO " + number + ':' + message)
        if command in commands:
          if command == commands[0]:
            print('stopping Salmon Kernel')
            sleep(0.5)
            print('Complete!')
            sleep(0.25)
            print("Terminating Fb")
            sleep(0.25)
            print("Complete!")
            sleep(0.75)
            exit()
          elif command == commands[1]:
            error('Salmon has encountered a fatal execption and needs to restart', '004')
            sleep(3)
            exit()
          elif command == commands[2]:
            print("Salmon Os commands")
            print(commands)
          elif command == commands[3]:
            man()
          elif command == commands[4]:
            version = 0.30
            print(version)
          elif command == commands[5]:
            print("3.1415265358979232846264338327950288419716939937510582097494450781640628620")
          elif command == commands[6]:
            print('stopping Salmon Kernel')
            sleep(0.5)
            print('Complete!')
            sleep(0.25)
            print("Terminating Fb")
            sleep(0.25)
            print("Complete!")
            sleep(0.75)
            exit()
          elif command == commands[7]:
            print('OS: ' + op + '; User: ' + username  + '; Arch: ' + arch)
        if command not in commands:
          print("Salmon Shell Emulator Protocal: command " + command +" not found")

    console()

