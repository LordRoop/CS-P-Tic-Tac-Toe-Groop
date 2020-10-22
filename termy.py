import os

def cls():  #clears the screen
  if os.name =='nt':
    os.system('cls')
  else:
    os.system('clear')
