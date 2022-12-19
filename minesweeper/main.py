from functions import *
from visual import *

height = 16
width = 16
num_mines = 40
print("Mine density:", num_mines / (height * width))
num_flags = 0
gameBoard = genBoard(height, width, num_mines)   # The board which determines if there is a mine or not in each square
knownBoard = genKnownBoard(height,width)         # The board that has what is shown to the player
probsBoard = None                                # The board which contains the probability of each square having a bomb
seen = []                                        # A list of the squares which have number 0 that have already been cleared

SQ_SIZE = 40                                     # Side length of each square in the board (probably in pixels)
clock = p.time.Clock()
p.init()
screen = p.display.set_mode((width*SQ_SIZE, height*SQ_SIZE))

lost = False      # Whether the game has been lost or not
display = False   # Whether the probabilities are shown or not
while True:
    drawBoard(screen, knownBoard,gameBoard,probsBoard,SQ_SIZE,lost,display)
    clock.tick(MAX_FPS)
    p.display.flip()
    for e in p.event.get():
        if e.type == p.KEYDOWN:
            if e.key == p.K_p:
                display = True
                probsBoard = calcprobs(knownBoard, num_mines - num_flags)
                print("=================================")
            elif e.key == p.K_l:
                display = False
            elif e.key == p.K_c:
                # Flags and clear the squares that are certainly mines or not
                for y,row in enumerate(probsBoard):
                    for x,cell in enumerate(row):
                        if cell == 0.0:
                            knownBoard[y][x] = squareNum((y, x), gameBoard)
                        elif cell == 1.0:
                            knownBoard[y][x] = '🚩'
                # Recounts the number of flags. This is to prevent some issues in which the number of flags was incorrect
                num_flags = 0
                for row2 in knownBoard:
                    for cell2 in row2:
                        if cell2 == '🚩':
                            num_flags += 1
                cleanboard(knownBoard,gameBoard,seen)
        if e.type == p.MOUSEBUTTONDOWN and not lost:
            location = p.mouse.get_pos()
            col = location[0] // SQ_SIZE
            row = location[1] // SQ_SIZE
            if e.button == 1:
                if gameBoard[row][col] == 1:
                    if knownBoard[row][col] != '🚩':
                        print("It was a mine!")
                        lost = True
                else:
                    knownBoard[row][col] = squareNum((row,col),gameBoard)
                    cleanboard(knownBoard,gameBoard,seen)
            elif e.button == 3:
                if knownBoard[row][col] == None:
                    knownBoard[row][col] = '🚩'
                    num_flags += 1
                    print("Number of flags:", num_flags)
                elif knownBoard[row][col] == '🚩':
                    knownBoard[row][col] = None
                    num_flags -= 1
                    print("Number of flags:", num_flags)
