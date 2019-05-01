from OS import os, copy
version = 0.21
def copy(image, file):
  os = open(file, 'w')
  os.write('')
  os.close()
  os = open(file, 'a')
  updte = open(image, 'r')
  for line in updte:
    patch = updte.readline()
    os.write(patch)
def update():
  ve = open('version.txt', 'r')
  ver = ve.readline()
  print(ver)
  if ver > version:
    version = ver
    copy('update.py', 'OS.py')
update()
while True:
  os()