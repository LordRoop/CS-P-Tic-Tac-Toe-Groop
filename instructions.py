def instructions1():           # code of different colors
  redfont= "\u001b[31m"   
  greenfont= "\u001b[32;1m"
  cyanfont= "\u001b[36m"
  resetfont=  "\u001b[0m"
  briblue= "\u001b[34;1m"


  print(greenfont, "\nHow to play Tic Tac Toe!:\n", resetfont)
  print(briblue, "A two player game that is fun for countless hours!\n", resetfont)
  print(greenfont, "Here are some rules:\n",resetfont)
  print(cyanfont, "Player 1 is X\n", resetfont)
  print(redfont, "Player 2 is O\n", resetfont)
  print(cyanfont, "Player 1 will place their X marker on any box by typing the number that corresponds to the box on the game board i.e. 4 for the top right box.\n",resetfont)
  print(redfont, "Player 2 will place their O marker on any box other than the one already taken using the same command of typing the box number.\n",resetfont)
  print(greenfont, "How to Win:\n",resetfont)
  print(briblue, "First to place their markers 4 times in a row vertically, horizontally, or diagonally, wins!\n",resetfont)
  print(briblue, "There are many different strategies to win this game, but that is up to you to learn through trial and error...\n",resetfont)
  print(greenfont, "Good Luck!!!\n",resetfont)
  input("Press enter to return to main menu")