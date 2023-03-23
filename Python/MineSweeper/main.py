import random
from tkinter import *


root = Tk()
root.title("MineSweeper")




def menu_init():
    easy = Button(menu, text = "Easy", padx=15, command= lambda x="easy": change_difficulty(x) )
    medium = Button(menu, text = "Medium", padx=10, command= lambda x="medium": change_difficulty(x) )
    hard = Button(menu, text = "Hard", padx=15, command= lambda x="hard": change_difficulty(x) )

    global timer 
    global seconds
    timer = Label(menu, text=int(seconds))
    timer.grid(row=1, column=1, columnspan=3)

    easy.grid(row=2, column=1)
    medium.grid(row=2, column=2)
    hard.grid(row=2, column=3)

 

def update_timer():
    global timer 
    global id
    s = int(timer.cget("text"))
    if (s == 0) or (s == "Game Over!"):
        timer.config(text="Game Over!")
        timer.after_cancel(id)
        game_over()
    else:
        s = int(s) - 1
        timer.config(text=int(s))
        id = timer.after(1000, update_timer)


def change_difficulty(dif):
    global difficulty    
    difficulty = dif
 
    for widget in  game.winfo_children():
        widget.destroy()
 
    game.pack_forget()
    init_board()

    #stop the old timer
    global timer 
    timer.after_cancel(id) 
    timer.config(text="") 

    global start_game
    start_game = False  #we restart the game

    menu_init()
    


   

def init_board():  
    #init variables
    global rows, columns, bombs, difficulty, seconds, fields_left
    if difficulty == "easy":
        rows = 8; columns = 8; bombs = 10; seconds = 60; fields_left = 54
    elif difficulty == "medium":
        rows = 16; columns = 16; bombs = 40; seconds = 300; fields_left = 216
    elif difficulty == "hard":
        rows = 16; columns = 32; bombs = 99; seconds = 1500; fields_left = 413
    
    for i in range(rows):
        for j in range(columns):
            board[i][j][2] = 0 #every field is initialized with 0 = no bomb
            board[i][j][3] = 0 #every field is initialized with 0 = unvisited
            board[i][j][1] = 0


    #create buttons for each field in board matrix
    for i in range(rows):
        for j in range(columns):
            board[i][j][0] = Button(game, text = "  ", padx=10, pady=6, bg="#e6e6e6", command = lambda a=i, b=j: click(a,b))
            board[i][j][0].grid(row=i, column=j)



#this function generates random bombs and is called after the first field is clicked excluding posibility to generate a bomb on the first field clicked
def set_bombs(i,j):  
    global bombs, rows, columns  
    #generate random bombs
    for b in range(bombs):
        row = random.randint(0,rows-1)
        col = random.randint(0,columns-1)
        if (board[row][col][2] == 1) or ((row == i) & (col == j)):
            while (board[row][col][2] == 1) or ((row == i) & (col == j)):
                row = random.randint(0,rows)
                col = random.randint(0,columns)
        board[row][col][2] = 1
        board[row][col][1] = "*"


def neighbours(i,j):
    #how many bombs are nearby
    global rows, columns
    count = 0
    if (board[i][j-1][2] == 1) & (j!=0):
        count+=1
    if (j!=columns-1) & (board[i][j+1][2] == 1):
        count+=1
    if (board[i-1][j][2] == 1) & (i!=0):
        count+=1
    if (board[i-1][j-1][2] == 1) & (j!=0) & (i!=0):
        count+=1
    if (board[i-1][j+1][2] == 1) & (i!=0) & (j!=columns-1):
        count+=1
    if (i!=rows-1) & (board[i+1][j][2] == 1):
        count+=1
    if (board[i+1][j-1][2] == 1) & (i!=rows-1) & (j!=0):
        count+=1
    if (i!=rows-1) & (j!=columns-1) & (board[i+1][j+1][2] == 1):
        count+=1
    return count


def zero_bombs_field(i,j):
    if board[i][j-1][3] != 1:
        click(i, j-1)
    if board[i][j+1][3] != 1:
        click(i, j+1)
    if board[i-1][j][3] != 1:
        click(i-1,j)
    if board[i+1][j][3] != 1:
        click(i+1,j)
    if board[i-1][j-1][3] != 1:
        click(i-1, j-1)
    if board[i-1][j+1][3] != 1:
        click(i-1, j+1)
    if board[i+1][j-1][3] != 1:
        click(i+1,j-1)
    if board[i+1][j+1][3] != 1:
        click(i+1,j+1)
     
  

def game_over():
    global timer, game
    timer.config(text="Game Over!")
    timer.after_cancel(id)
    for w in game.winfo_children():
         w.configure(state="disabled")


def win():
    global timer, game
    timer.config(text="You Win!")
    timer.after_cancel(id)
    for w in game.winfo_children():
         w.configure(state="disabled")



def click(i,j):
   
    global start_game, rows, columns, fields_left
    if start_game == False:
        print(str(i)+" "+str(j))
        set_bombs(i,j)
        #print board in terminal with numbers 0=safe, 1=bomb    
        for a in range(rows):
            for b in range(columns):
                print(board[a][b][2], end=" ")
            print()
        start_game = True
        update_timer()    #the timer starts when we first click a field
        
    
    if (i>=0) & (i<rows) & (j>=0) & (j<columns):
        fields_left-=1
        howManyBombs = neighbours(i, j)
        if howManyBombs == 1:
            text_color = "#3333ff"
        elif howManyBombs == 2:
            text_color = "#00cc00"
        elif howManyBombs == 3:
            text_color = "#ff1a1a"
        elif howManyBombs == 4:
            text_color = "#996600"
        elif howManyBombs == 5:
            text_color = "#e6e600"
        elif howManyBombs == 6:
            text_color = "#4d0099"
        elif howManyBombs == 7:
            text_color = "#284d00"
        else:
            text_color = "#000000"

        if board[i][j][1] == "*":
            board[i][j][0] = Button(game, text = str(board[i][j][1]), padx=10, pady=6, bg="#bfbfbf", fg="#000000", disabledforeground="#000000" ,state="disabled" )
        elif howManyBombs == 0:
            board[i][j][0] = Button(game, text = "  ", padx=10, pady=6, bg="#bfbfbf", state="disabled")
        else:
            board[i][j][0] = Button(game, text = str(howManyBombs), padx=10, pady=6, bg="#bfbfbf", fg="#000000", disabledforeground=text_color , state="disabled" )
        
        board[i][j][3] = 1 #visited
        if (howManyBombs == 0) & (board[i][j][2] != 1):
            zero_bombs_field(i, j)
        
        if board[i][j][2] == 1:
            game_over()
        elif fields_left == 0:
            win()
        
        board[i][j][0].grid(row=i, column=j)
   

global game
global menu 
game = LabelFrame(root, borderwidth = 0, highlightthickness = 0)
menu = LabelFrame(root, borderwidth = 0, highlightthickness = 0)
menu.grid()
game.grid()

global difficulty
difficulty = "easy" #easy 8x8, 10 bombs
                    #medium 16x16, 40 bombs
                    #hard 16x32, 99 bombs
global rows 
rows = 8
global columns
columns = 8 
global bombs
bombs = 10
global seconds
seconds = 60  #easy 60 seconds, medium 300, hard 1500

global start_game
start_game = False #becomes True when we first click a field

global fields_left



global board
board  = [[[[0]for x in range(4)]for x in range(33)]for x in range(17)] 
#depth level 0 is for buttons, level 1 is for characters " " and "*", level 2 is for terminal (0 safe field, 1 bomb), level 3 is for visited and unvisited


menu_init()
init_board() 
#change_difficulty("easy")

root.mainloop()