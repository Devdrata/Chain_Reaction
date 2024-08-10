This is my take on the (somewhat) popular game titled Chain Reaction. This was coded in python, is nowhere near optimized, and can definitely be improved upon.
#A cool project to take upon if you want to learn the fundamentals of OOP and POP in python, knowledge which can later be extended to other languages as well.
GamePlay:
1) The Game starts by printing a 10x10 Grid of numbers.
2) There are two players, Player One (Yellow) and Player Two (Cyan). The Players alternate in choosing their 'cells' from the grid.
3) Upon choosing a cell, the number in it increments by one. If the cell is at one of the four corners of the grid, and it contains the number 2, then it will explode, incrementing each of its neighbour by one,
   and also changing their neighbour's color.
   If the cell is a part of the edge of the grid, then the same happens if it contains the number 3, while for any other cell, it happens if it contains the number 4.
4) The game ends when one of the two colors disappears, leaving the one behind as the winner.
