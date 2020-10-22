def game1():
  ANSI_BEGINNING_OF_LINE= u"\u001B[1000D" # big number
  for i in range(4):
    if i== 0:
      print(" ╔════╦════╦════╦════╗")
    else:
      print(ANSI_BEGINNING_OF_LINE,"╠════╬════╬════╬════╣")
    val = i*4
    print(' ║ {:2d} ║ {:2d} ║ {:2d} ║ {:2d} ║'.format(val, val+1, val+2, val+3,))
# loop ending here
  print(ANSI_BEGINNING_OF_LINE,"╚════╩════╩════╩════╝")
  if answer == 1:
    Main.Main()




  print("══╦══ ╦ ╔═══╗   ══╦══ ╔═══╗ ╔═══╗   ══╦══ ╔═══╗ ╔═══╗")   #title string
  print("  ║   ║ ║         ║   ║   ║ ║         ║   ║   ║ ║    ") 
  print("  ║   ║ ║         ║   ╠═══╣ ║         ║   ║   ║ ╠══╣ ") 
  print("  ║   ║ ║         ║   ║   ║ ║         ║   ║   ║ ║    ") 
  print("  ╩   ╩ ╚═══╝     ╩   ╩   ╩ ╚═══╝     ╩   ╚═══╝ ╚═══╝") 