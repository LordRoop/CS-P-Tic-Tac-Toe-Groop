"""This file runs our 3x3 game"""
import termy
import time

def game3(): #gives us the ability to add color to our game
  ANSI_BEGINNING_OF_LINE= u"\u001B[1000D" # big number
  redfont= "\u001b[31m"
  greenfont= "\u001b[32;1m"
  bluefont= "\u001b[34;1m"
  resetfont= "\u001b[0m"
  cyanfont= "\u001b[36m"
  icon = {
    0 : " ",
    1 : (cyanfont+"X"+resetfont),
    2 : (redfont+"O"+resetfont),
  }
  pos = [[0,0,0],[0,0,0],[0,0,0]]   #list of board positions
  
  
  def drawboard3x3():     #draws the board merging ascii characters with values in pos list
    
    termy.cls()
    for k in range(-1, 3):
      if k == -1:
        print(ANSI_BEGINNING_OF_LINE,"     0    1    2  ")
        print(ANSI_BEGINNING_OF_LINE,"  ╔════╦════╦════╗")
      elif k == 2:
        print(ANSI_BEGINNING_OF_LINE,k,'║', icon[pos[0+k][0]] ,' ║', icon[pos[0+k][1]]  ,' ║', icon[pos[0+k][2]] ,' ║')
        print(ANSI_BEGINNING_OF_LINE,"  ╚════╩════╩════╝")
      else:
        print(ANSI_BEGINNING_OF_LINE,k,'║', icon[pos[0+k][0]] ,' ║', icon[pos[0+k][1]]  ,' ║', icon[pos[0+k][2]] ,' ║')
        print(ANSI_BEGINNING_OF_LINE,"  ╠════╬════╬════╣")
 
  gameover = False
  winner = 0
  round = 1
  while not gameover :    
    drawboard3x3()
    # get inputs
    try:   # in case of problem with user input, it goes to "except"
      
      player = 2 - round % 2   # odd round -> player 1; even round -> player 2
      print("\nPlayer ",player, "'s turn!!", sep='')
      col=-1
      while col!=0 and col!=1 and col!=2:
        col = int(input("choose column [0-2]:  "))
      row=-1
      while row!=0 and row!=1 and row!=2:
        row = int(input("choose row [0-2]:  "))
      if pos[row][col]== 0: # position empty, valid play
        pos[row][col] = player  # update table

        # test for winner in rows, columns, and diagonals
        if (pos[0][0]== player and pos[0][1]== player and pos[0][2]== player) or (pos[1][0]== player and pos[1][1]== player and pos[1][2]== player) or (pos[2][0]== player and pos[2][1]== player and pos[2][2]== player) or (pos[0][0]== player and pos[1][0]== player and pos[2][0]== player) or (pos[0][1]== player and pos[1][1]== player and pos[2][1]== player) or (pos[0][2]== player and pos[1][2]== player and pos[2][2]== player) or (pos[0][0]== player and pos[1][1]== player and pos[2][2]== player) or (pos[2][1]== player and pos[1][2]== player and pos[0][3]== player):
          winner = player
        round = round + 1 # keep track of rounds
      else: 
        print(redfont, "position occupied", resetfont) # avoid reusing space 
        time.sleep(.76)  # timed pause
      if winner!=0:   # there is a winner
        drawboard3x3()
        print(greenfont, "\nGame Over, player", winner, "wins!!!\n\n\n", resetfont) 
        gameover = True
        input("\npress enter to return to main menu")
          
      elif round > 9:   # Board full without winner
        drawboard3x3()
        print(bluefont, "\nGame Over, it's a draw!!\n\n\n", resetfont)
        gameover = True
        input("\npress enter to return to main menu")
         

    except:   # catchall for bad key strokes
      print(redfont, "invalid entry", resetfont) 
      time.sleep(.76)  
      continue
  
  
  
  
  
        
        