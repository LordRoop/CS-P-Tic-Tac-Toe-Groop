def game1():
    #print(" ╔═══╦═══╦═══╦═══╗")
    #print(" ║ 0 ║ 1 ║ 2 ║ 3 ║")
    #print(" ╠═══╬═══╬═══╬═══╣")
    #print(" ║ 4 ║ 5 ║ 6 ║ 7 ║")
    #print(" ╠═══╬═══╬═══╬═══╣")
    #print(" ║ 8 ║ 9 ║10 ║11 ║")
    #print(" ╠═══╬═══╬═══╬═══╣")
    #print(" ║12 ║13 ║14 ║15 ║")
    #print(" ╚═══╩═══╩═══╩═══╝")
  
  ttt = [['0', '1', '2', '3'], ['4', '5', '6', '7'], ['8', '9', '10', '11'], ['12', '13', '14', '15']]
  row = int(input("type row from zero to 3: \n"))
  col = int(input("type col from zero to 3: \n"))
  ttt[row][col] = str(input("type value 0-4: \n"))
  
  ANSI_BEGINNING_OF_LINE= u"\u001B[1000D" # big number
  for i in range(4):
    if i== 0:
      print(" ╔════╦════╦════╦════╗")
    else:
      print(ANSI_BEGINNING_OF_LINE,"╠════╬════╬════╬════╣")
    val = i*4
    print(" ║", ttt[i][0], " ║", ttt[i][1], " ║", ttt[i][2], " ║", ttt[i][3]," ║")
    #print(' ║ {:2d} ║ {:2d} ║ {:2d} ║ {:2d} ║'.format(ttt[i][0], ttt[i][1], ttt[i][2], ttt[i][3],))
# loop ending here
  print(ANSI_BEGINNING_OF_LINE,"╚════╩════╩════╩════╝")