'''This file prints out our main menu'''
import termy
import game4x4
import game3x3
import instructions
import time 
  
def menu(): # our menu
  termy.cls()
  print("══╦══ ╦ ╔═══╗   ══╦══ ╔═══╗ ╔═══╗   ══╦══ ╔═══╗ ╔═══╗")   #title string
  time.sleep(0.2)                                                 #pause between prints
  print("  ║   ║ ║         ║   ║   ║ ║         ║   ║   ║ ║    ") 
  time.sleep(0.2)
  print("  ║   ║ ║         ║   ╠═══╣ ║         ║   ║   ║ ╠══╣ ") 
  time.sleep(0.2)
  print("  ║   ║ ║         ║   ║   ║ ║         ║   ║   ║ ║    ") 
  time.sleep(0.2)
  print("  ╩   ╩ ╚═══╝     ╩   ╩   ╩ ╚═══╝     ╩   ╚═══╝ ╚═══╝") 

  print("0: Exit")
  time.sleep(0.2)   
  print("1: Read Instructions")
  time.sleep(0.2)
  print("2: Play 3x3 Tic Tac Toe")
  time.sleep(0.2)
  print("3: Play 4x4 Tic Tac Toe")
  time.sleep(0.2)
  answer = int(input("select number: "))
  
  if answer == 1:          #  This If statement is what makes the menu interactive
    instructions.instructions1()
  elif answer == 2:
    game3x3.game3()
  elif answer == 3:
    game4x4.game4()
  elif answer == 0:
    print("Goodbye!!!")
    return 
  else: 
    print("\nBad Choice :(\n")
  menu() #recursion
# start menu
menu()