import pygame as p
p.font.init()

path = ''    # This should contain the path of where the game folder is
Icon = p.image.load(path+'images/bombicon.png')
p.display.set_icon(Icon)
mine = p.image.load(path+'images/mine.png')
flag = p.image.load(path+'images/flag.png')
notpressed = p.image.load(path+'images/notpressed.png')
numbers = {}
for i in range(9):
    numbers[i] = p.image.load(path+f'images/type{i}.png')


MAX_FPS = 10
def dimension(grid):
    return(len(grid))
def dimensionx(grid):
    return(len(grid[0]))

# Inserts some image centered on a given square
def blitimage(screen,image,r,c,SQ_SIZE,num=2,den=3):
    label = p.transform.scale(image, ((SQ_SIZE * num) // den, (SQ_SIZE * num) // den))
    tHeight = label.get_rect().height
    tWidth = label.get_rect().width
    screen.blit(label,
                p.Rect((c + 1 / 2) * SQ_SIZE - tWidth / 2, (r + 1 / 2) * SQ_SIZE - tHeight / 2, SQ_SIZE,
                       SQ_SIZE))

# Inserts some text centered on a given square
def blittext(screen,text,font,r,c,SQ_SIZE):
    label = font.render(text, 1, p.Color("black"))
    tHeight = label.get_rect().height
    tWidth = label.get_rect().width
    screen.blit(label,
                p.Rect((c + 1 / 2) * SQ_SIZE - tWidth / 2, (r + 1 / 2) * SQ_SIZE - tHeight / 2, SQ_SIZE//3, SQ_SIZE//3))

def drawBoard(screen,board,mineboard,probboard,SQ_SIZE,status,display):
    for r in range(dimension(board)):
        for c in range(dimensionx(board)):
            val = board[r][c]
            if val == None:
                if status and mineboard[r][c]==1:
                    blitimage(screen,mine,r,c,SQ_SIZE,1,1)
                else:
                    blitimage(screen, notpressed, r, c, SQ_SIZE, 1, 1)
                    if display and probboard[r][c] != None:
                        blittext(screen,str(round(probboard[r][c]*100)),p.font.SysFont('Times New Roman',10),r,c,SQ_SIZE)
            elif type(val) == int:
                blitimage(screen, numbers[val], r, c, SQ_SIZE,1,1)
            elif val == '🚩':
                blitimage(screen,flag,r,c,SQ_SIZE,1,1)
    pass