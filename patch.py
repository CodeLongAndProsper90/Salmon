def update():
  from
  def copy(image, file):
    os = open(file, 'w')
    os.write('')
    os.close()
    os = open(file, 'a')
    updte = open(image, 'r')
    for line in updte:
      patch = updte.readline()
      os.write(patch)
    copy('update.py', 'OS.py')
