import random
import sys
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.metrics import dp
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty, BooleanProperty
from kivy.graphics.vertex_instructions import Line
from kivy.graphics.context_instructions import Color
from kivy.graphics import Rectangle
from kivy.graphics import Ellipse

from kivy.config import Config             #Change the window size
Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '760')


#Board class will init the board wich is a matrix 15x15x3
#on the first level the matrix will store the letter it contains, if the value is 0 it means there's no letter
#on second level the matrix wil the color of the field, rules about colors can be seen bellow
#on third level matrix stores the buttons from the GUI, every square from the board is a button

#def foo(a: type_param, b: type_param) -> return_type:
 
class Board():
    '''
    Board creeaza tabla de joc si imparte cartile de joc
    '''
    def __init__(self) -> None:
        """
        constructor clasa board, initializeaza tabla de joc
        """
        self.board = [[[0 for i in range(3)]for j in range(15)]for k in range(15)]
        """Alb - nu modifica valoarea literelor asezate pe ele
            RED - tripleaza valoarea cuvantului daca o litera a acestuia este plasata pe un astfel de camp
            YELLOW - dubleaza valoarea cuvantului daca o litera a acestuia este plasata pe un astfel de camp
            BLUE - tripleaza valoarea literelor depuse pe ele
            GREEN - dubleaza valoarea literelor depuse pe ele"""
        for i in range(3):
            for j in range(3):
                self.board[i*7][j*7][1] = "R"
        self.board[7][7][1] = 0
        
        for i in range(4):
            for j in range(4):
                self.board[1+i*4][1+j*4][1] = "B"

        for i in range(1,5):
            self.board[i][i][1] = "Y"
            self.board[i][14-i][1] = "Y"
            self.board[14-i][i][1] = "Y"
            self.board[14-i][14-i][1] = "Y"

        self.board[0][3][1] = "G"
        self.board[3][0][1] = "G"
        self.board[0][11][1] = "G"
        self.board[3][14][1] = "G"
        self.board[11][0][1] = "G"
        self.board[14][3][1] = "G"
        self.board[14][11][1] = "G"
        self.board[11][14][1] = "G"

        self.board[2][6][1] = "G"
        self.board[2][8][1] = "G"
        self.board[3][7][1] = "G"
        self.board[6][2][1] = "G"
        self.board[8][2][1] = "G"
        self.board[7][3][1] = "G"
        self.board[12][8][1] = "G"
        self.board[12][6][1] = "G"
        self.board[11][7][1] = "G"
        self.board[8][12][1] = "G"
        self.board[6][12][1] = "G"
        self.board[7][11][1] = "G"

        self.board[6][6][1] = "G"
        self.board[6][8][1] = "G"
        self.board[8][6][1] = "G"
        self.board[8][8][1] = "G"

        """A1= 11 buc.; B9= 2; C1= 5; D2= 4; E1= 9; F8= 2.; G9= 2; H10 = 1; I1 = 10; J10= 1; L1= 4;  #Romanian version
         M4= 3; N1= 6; O1= 5; P2= 4; R1= 7; S1= 5; T1= 7; U1= 6; V8= 2; Z10= 1; X10= 1; Joli= 2."""

        self.points = {"A":1, "B":3, "C":3, "D":2, "E":1, "F":4, "G":2, "H":4, "I":1, "J":8,"K":5, "L":1, "M":3, "N":1, "O":1, "P":3,"Q":10, "R":1, "S":1, "T":1, "U":1, "V":4, "W":4, "Y":4, "Z":10, "X":8}
        self.frequency = {"A":9, "B":2, "C":2, "D":4, "E":12, "F":2, "G":3, "H":2, "I":9, "J":1, "K":1, "L":4, "M":2, "N":6, "O":8, "P":2, "Q":1, "R":6, "S":4, "T":6, "U":4, "V":2, "W":2, "X":1,"Y":2,"Z":1}
        self.letters = []
        for letter in self.frequency:          #we make the deck of cards using letter frequency
            for i in range(self.frequency[letter]):
                self.letters.append(letter)
        random.shuffle(self.letters)

    def give_player_7_letters(self, player: object) -> None:
        """
        -player primeste la inceputul jocului 7 carti
        :param player: obiect din clasa Player
        :return: None
        """
        for i in range(7):
            player.letters.append(self.letters.pop())
        player.nr_letters = 7

    def give_player_letters(self, player: object) -> None:
        """
        -player primeste carti in timpul jocului pana are 7 carti in mana
        :param player: obiect din clasa Player
        :return: None
        """
        if len(self.letters) < 7 - player.nr_letters:          #if there are less than 7-player.nr_letters letters remained 
            print(self.letters)
            print(player.nr_letters)
            nr=player.nr_letters
            for i in range(len(self.letters)):                 
                player.letters.append(self.letters.pop())
            player.nr_letters = nr + len(self.letters)
        else: 
            for i in range(player.nr_letters, 7):
                player.letters.append(self.letters.pop())
            player.nr_letters = 7


#Player class contains the letters available for the palyer
class Player():
    '''
    reprezinta un jucator, contine informatii despre cartile de joc detinute de jucator
    '''
    def __init__(self) -> None:
        """
        -constructor clasa Player, initializeaza parametrii pt player
        :return: None
        """
        self.letters = []            
        self.letter_buttons = []     #list with tiles (buttons)
        self.nr_letters = 0


#Game class contains info about the match
class Game():
    '''
    gestioneaza regulile jocului
    '''
    def __init__(self) -> None:
        """
        constructor clasa Game, manageriaza jocul
        """
        self.player_score = 0
        self.round = 0     #in the first round player must to place a word in the middle
        self.computer_score = 0
        self.game_over = 0
        self.turn = 0               # 0=player, 1=computer, first will be the player
        self.letters_left = 98     #game will begin with 100 letters available
        self.selected_tile_value = 0  #when player clicks on a tile this variable will store the letter selected, by default it will pe 0
        self.selected_tile_id = -1    #store id of the pressed tile, by default it is -1
        self.tiles_played_this_round = []    #stores tiles in order they were played this round
        self.tiles_coordinates_this_round = []          #stores tiles coordintes from current round, list of tuples
        self.tiles_ids_played_this_round = []        #all tiles ids played this round
        self.player_tiles = []         #the 7 tiles from the bottom 
        self.words_formed_this_round = []  
        self.nr_of_pass = 0      #if pass is pressed 3 times without placing tiles game is over     

    def verify_tiles_placement(self) -> str:       #this functions verifies if a tile was placed correctly, i and j are coordinates of tile's placement
        """
        verifica daca cartile au fost asezate corect pe tabla in momentul in care se apasa butonul play, returneaza un mesaj corespunzator
        :return: string
        """
        ############# FIRST ROUND PLACEMENT #######################
        
        correct_placement = False
        if self.round == 0:    #if this is first round
            for i,j in self.tiles_coordinates_this_round:
                if i==7 and j==7:
                    correct_placement = True
                    break    
            if correct_placement == False:   #if is first round and no word in the middle return WRONG PLACEMENT
                print("MIDDLE SQUARE")
                return "WRONG PLACEMENT"    
    
        ############## TILES ON THE SAME LINE OR COLUMN #########################
        
        if len(G.tiles_played_this_round) >= 1:   #if this round were played more than one tile
            correct_placement = True     
            i,j = G.tiles_coordinates_this_round[0]
            for x,y in G.tiles_coordinates_this_round:          #verify if all tiles are placed on the same horizontal row 
                if i != x:
                    correct_placement = False
            if correct_placement == False:
                correct_placement = True
                for x,y in G.tiles_coordinates_this_round:      #verify if all tiles are placed on the same vertical collumn 
                    if j != y:        
                        correct_placement = False
                        print("TILES ON THE SAME LINE")
                        return "WRONG PLACEMENT"


    ############## NO SPACES BETWEEN TILES ###############################
        space_between = False
        G.tiles_coordinates_this_round.sort(key = lambda x: x[0])   #sort coordintes by first element (x axis)
        if len(G.tiles_coordinates_this_round)>1:
            x,y = G.tiles_coordinates_this_round[0]
        for i in range(1,len(G.tiles_coordinates_this_round)): 
            if G.tiles_coordinates_this_round[i][0] - x != 1:               #if the tiles placed this are not next to each other
                space_between = True
                for j in range(x, G.tiles_coordinates_this_round[i][0]):    # then we verify it in the space bwtween them are already tiles from previous rounds
                    if B.board[j][y][0] == 0:         #if there's no tile it means there's a gap between tiles placed this round
                        print("NO SPACES BETWEEN TILES")
                        return "WRONG PLACEMENT"

            #we do the same for the y axis 
        G.tiles_coordinates_this_round.sort(key = lambda x: x[1])   #sort coordintes by second element (y axis)
        if len(G.tiles_coordinates_this_round)>1:
            x,y = G.tiles_coordinates_this_round[0]
        for i in range(1,len(G.tiles_coordinates_this_round)): 
            if G.tiles_coordinates_this_round[i][1] - y != 1:               #if the tiles placed this are not next to each other
                space_between = True
                for j in range(y, G.tiles_coordinates_this_round[i][1]):    # then we verify it in the space bwtween them are already tiles from previous rounds
                    if B.board[x][j][0] == 0:         #if there's no tile it means there's a gap between tiles placed this round
                        print("NO SPACES BETWEEN TILES")
                        return "WRONG PLACEMENT"

    ############## NO SPACES BETWEEN WORDS ####################################
    #we check if there's at leas one tile placed this round that has at least one neighbour on x axis and at least one neighbour on y axis
    #this check is done only if it is not the first round
        
        if self.round > 0:
            correct_placement = False
            nr_empty_neighbours = 0
            for x,y in G.tiles_coordinates_this_round:
                #check if the tile is on the edge or in the corner
                if x==0 and y == 0:    #corner left up
                    if B.board[0][1][0] !=0 or B.board[1][0][0] != 0:
                        correct_placement = True 
                        if B.board[0][1][0]==0:
                            nr_empty_neighbours+=1
                        if B.board[1][0][0]==0:
                            nr_empty_neighbours+=1
                        correct_placement = True          
                elif x==0 and y==14:    #corner right up
                    if B.board[0][13][0] !=0 or B.board[1][14][0] != 0:
                        correct_placement = True 
                        if B.board[0][13][0]==0:
                            nr_empty_neighbours+=1
                        if B.board[1][14][0]==0:
                            nr_empty_neighbours+=1
                        correct_placement = True 
                elif x==14 and y==0:      #corner left down
                    if B.board[13][0][0] !=0 or B.board[14][1][0] != 0:
                        correct_placement = True
                        if B.board[13][0][0]==0:
                            nr_empty_neighbours+=1
                        if B.board[14][1][0]==0:
                            nr_empty_neighbours+=1
                        correct_placement = True                        
                elif x==14 and y==14:     #corner right down
                    if B.board[13][14][0] !=0 or B.board[14][13][0] != 0:
                        correct_placement = True  
                        if B.board[13][14][0]==0:
                            nr_empty_neighbours+=1
                        if B.board[14][13][0]==0:
                            nr_empty_neighbours+=1
                        correct_placement = True                         
                elif x==0:      #up edge
                    if B.board[x+1][y][0] != 0 or B.board[x][y+1][0] != 0 or B.board[x][y-1][0] != 0:
                        correct_placement = True 
                        if B.board[x+1][y][0]==0:
                            nr_empty_neighbours+=1
                        if B.board[x][y+1][0]==0:
                            nr_empty_neighbours+=1
                        if B.board[x][y-1][0]==0:
                            nr_empty_neighbours+=1
                        correct_placement = True                          
                elif x==14:     #down edge
                    if  B.board[x-1][y][0] != 0 or B.board[x][y+1][0] != 0 or B.board[x][y-1][0] != 0:
                        correct_placement = True 
                        if B.board[x-1][y][0]==0:
                            nr_empty_neighbours+=1
                        if B.board[x][y+1][0]==0:
                            nr_empty_neighbours+=1
                        if B.board[x][y-1][0]==0:
                            nr_empty_neighbours+=1
                        correct_placement = True                            
                elif y==0:      #left edge
                    if B.board[x+1][y][0] != 0 or B.board[x-1][y][0] != 0 or B.board[x][y+1][0] != 0:
                        correct_placement = True 
                        if B.board[x+1][y][0]==0:
                            nr_empty_neighbours+=1
                        if B.board[x-1][y][0]==0:
                            nr_empty_neighbours+=1
                        if B.board[x][y+1][0]==0:
                            nr_empty_neighbours+=1
                        correct_placement = True      
                elif y==14:     #right edge
                    if B.board[x+1][y][0] != 0 or B.board[x-1][y][0] != 0 or B.board[x][y-1][0] != 0:
                        correct_placement = True
                        if B.board[x+1][y][0]==0:
                            nr_empty_neighbours+=1
                        if B.board[x-1][y][0]==0:
                            nr_empty_neighbours+=1
                        if B.board[x][y-1][0]==0:
                            nr_empty_neighbours+=1
            
                elif B.board[x+1][y][0] != 0 or B.board[x-1][y][0] != 0 or B.board[x][y+1][0] != 0 or B.board[x][y-1][0] != 0:
                    correct_placement = True
                    if B.board[x-1][y][0] == 0: 
                        nr_empty_neighbours+=1 
                    if B.board[x+1][y][0] == 0:  
                        nr_empty_neighbours+=1 
                    if B.board[x][y-1][0] == 0:
                        nr_empty_neighbours+=1 
                    if B.board[x][y+1][0] == 0:
                        nr_empty_neighbours+=1 
         
            if nr_empty_neighbours == 6+2*(len(G.tiles_played_this_round)-2) and space_between == False:    #If it is an "island"
                correct_placement == False

        if ((correct_placement == True) or (len(G.tiles_played_this_round) == 0)):
            self.round+=1
            return "CORRECT PLACEMENT" 
        else: 
            print("LAST CHECK")
            return "WRONG PLACEMENT"


    #This function extracts all words formed this round that include the tiles played this round
    def extract_words(self) -> None:
        '''
        extrage toate cuvintele de pe tabla care s-au format cu cartile asezate in runda curenta
        :return: None
        '''
        for i in range(15):
            for j in range(15):
                print(B.board[i][j][0], end=" ")
            print()
        
        for i,j in G.tiles_coordinates_this_round:
            new_word = ""
            x = i
            while B.board[i-1][j][0] != 0:    #while above this played tile we have letters placed on board
                i-=1
            while B.board[i][j][0] != 0:
                new_word += str(B.board[i][j][0])
                i+=1
                if i==15:
                    break
            if len(new_word)>1 and new_word not in self.words_formed_this_round:
                self.words_formed_this_round.append(new_word)
            new_word = "" 

            i = x
            while B.board[i][j-1][0] != 0:    #while at left of this played tile we have letters placed on board
                j-=1
            while B.board[i][j][0] != 0:
                new_word += str(B.board[i][j][0])
                j+=1
                if j==15:
                    break
            if len(new_word)>1 and new_word not in self.words_formed_this_round:
                self.words_formed_this_round.append(new_word)
             
        print("LIST")
        print(self.words_formed_this_round)


    #this function search words in dictionary.txt
    def search_words(self) -> None:
        '''
        cauta cuvintele formate in dictionar, daca nu sunt corecte se reia runda, daca sunt corecte se calculeaza scorul
        :return: None
        '''
        for w in G.words_formed_this_round:
            if w not in words:                #if the word doesen't exist show a message
                for i,j in G.tiles_coordinates_this_round:
                    B.board[i][j][0] = 0              # 0 = default value
                    B.board[i][j][2].text = ""        #erase tile from board
                    B.board[i][j][2].background_color = (1,1,1,1)   #background color
                    B.board[i][j][2].disabled = False     #enable button
                    B.board[i][j][2].color = (1,1,1,1)   #text color
                
                for i in range(15):
                    for j in range(15):
                        if B.board[i][j][0] == 0:   #if the square is not occupied by a tile then recolor the board were nedded
                            if B.board[i][j][1] == 'R':  #if color off square is red then text of the button will be TW
                                B.board[i][j][2].text = "TW"           #TW = triple word, it will triple the score of the entire word
                                B.board[i][j][2].background_color = (1,0,0,1)
                            elif B.board[i][j][1] == 'Y':
                                B.board[i][j][2].text = "DW"          #DW = double word score
                                B.board[i][j][2].background_color = (1,1,0.2,1)
                            elif B.board[i][j][1] == 'B':
                                B.board[i][j][2].text = "TL"          #TL = triple letter score
                                B.board[i][j][2].background_color = (0,0,1,1)
                            elif B.board[i][j][1] == 'G':
                                B.board[i][j][2].text = "DL"          #DL = double letter score
                                B.board[i][j][2].background_color = (0,1,0,1)
                if B.board[7][7][0] == 0:  #if the middle square is not occupied reset its color
                    B.board[7][7][2].background_color = (1,0.4,0.69,1)
                
                    
                for id in reversed(G.tiles_ids_played_this_round):
                    for tile in G.player_tiles:
                        if tile.id == id:
                            if len(G.tiles_played_this_round)>0:
                                tile.text = G.tiles_played_this_round.pop()         #Give tiles back to the player
                            tile.disabled = False  
                            break  
                
                G.tiles_coordinates_this_round = []        #Reset all info about tiles played this round
                G.tiles_played_this_round = []
                G.tiles_ids_played_this_round = []
                G.selected_tile_value = 0
                G.selected_tile_id = -1
                G.words_formed_this_round = [] 

               
            else:
                self.calculate_score()     #All words have been found
                G.nr_of_pass = 0    #reset nr of pass bc words have been formed
                for word in G.words_formed_this_round:    #add words to the panel with last words played
                    A.words =str(A.words + str("\n") + str(word))
                    nr_lines = A.words.count('\n')
                    if nr_lines == 15:    #if there's too many lines we reset list of last words played
                        A.words = ""

                if G.turn == 1:             #at this point the words were finds and we'll change the turn to player2
                    G.turn = 0
                    A.turn = "Player1 turn"
                    i=0  #index  
                    for b in G.player_tiles:
                        b.text = P.letters[i]
                        i+=1
                    G.words_formed_this_round = []
                else: 
                    G.turn = 1        
                    A.turn = "Player2 turn"
                    i=0  #index  
                    for b in G.player_tiles:
                        b.text = P2.letters[i]
                        i+=1
                    G.words_formed_this_round=[]
                               
                #C.play()                   #call function play of cumputer class
            if len(B.letters) == 0:
                score_player1 = A.score_player1.split()
                score_player2 = A.score_player2.split()
                if int(score_player1[1]) > int(score_player2[1]):
                    A.turn = "Player1 win"
                else:
                    A.turn = "Player2 win"
                G.game_over = 1
                for b in P.letter_buttons:    #disable tiles
                    b.disabled = True
                

    #this function calculates the score
    def calculate_score(self) -> None:
        '''
        calculeaza scorul cuvintelor formate in runda curenta
        '''
        score = 0
        for w in G.words_formed_this_round:
            for c in w:
                score+=B.points[c]
        for i,j in G.tiles_coordinates_this_round:                      #Cases when we double or triple score of a letter
            if B.board[i][j][0] != 0:
                if B.board[i][j][1] == "B" or  B.board[i][j][1] == "R":
                    score += 2*(B.points[B.board[i][j][0]])
                if B.board[i][j][1] == "Y" or  B.board[i][j][1] == "G":
                    score += B.points[B.board[i][j][0]]
        if G.turn == 0: #player1
            prev_score = A.score_player1.split()                           #we add the new score with the previous one
            A.score_player1 = "Score: " + str(score + int(prev_score[1]))     #A is the instance of the App, it contains score_text variablie whose label with the score is bind to in kv file
        else:   #player2 turn
            prev_score = A.score_player2.split()                            
            A.score_player2 = "Score: " + str(score + int(prev_score[1])) 

'''         
class Computer():
    def __init__(self):
        self.letters = []            
        self.letter_buttons = []     #list with tiles (buttons)
        self.nr_letters = 0

    def play(self):    #this function will put a word on table
        #first we'll select a random tile from the board (placed in previous rounds)
        letters_on_board = []     #list with all the letters from the board
        for i in range(15):
            for j in range(15):
                if B.board[i][j][0]!=0:
                    letters_on_board.append(B.board[i][j][0])
        x = 0  #letter coordinates
        y = 0
        letter = random.choice(letters_on_board)    #we chosed a random letter and we'll try to form a word with this letter and letters from computer stack
        for i in range(15):                   #take coordinates of the letter
            for j in range(15):
                if B.board[i][j][0] == letter:
                    x = i
                    y = j

        computer_available_letters = self.letters
        computer_available_letters.append(letter)

        print("CHOSED LETTER")
        print(letter)
        print("LETTERS")
        print(computer_available_letters)
        ten_possible_words = []  #this is a list with 10 possible words to be formed (if there are less it's ok)
        count = 0
        for w in words:       #we search a word in dictionary that can be formed with our letters
            letters_from_word = []  #split the word in letters
            for ch in w:
                letters_from_word.append(ch)
            if set(letters_from_word).issubset(set(computer_available_letters)) and letter in set(letters_from_word) and w not in ten_possible_words and len(w)>1:            
                count+=1
                ten_possible_words.append(w)
            if count == 10:
                break
        print(ten_possible_words)
        #we have a list with possible words to be formed and we chose one of them
        selected_word = ten_possible_words[0]
        index = selected_word.index(letter)       #index of letter in word
        print(index)
        if B.board[x-1][y][0]==0:   #if above selected letter there's no letters
            if x - index >=0:       #there's space above to fit the word
                if x + (len(selected_word)-index) < 15:  #if there's space bellow the selected letter
                    for i in range(x-index, x+(len(selected_word)-index)):
                        B.board[i][y][0] = selected_word[i-(x-index)]        
            

                    


        G.turn = 0  #change turn to player
'''

class ScrabbleApp(App): 
    '''
    aplicatia kivy, creeaza interfata si o ruleaza 
    '''
    score_player1 = StringProperty("Player1: 0")
    score_player2 = StringProperty("Player2: 0")
    turn = StringProperty("Player1 turn")
    words = StringProperty("")
    pass

class MainWidget(BoxLayout):
    '''
    widgetul principal din fisierul kv care contine layouturile
    '''
    pass


class BoardGrid(GridLayout):
    '''
    interfata grafica pentru gridul de joc
    '''
    def __init__(self, **kwargs) -> None:
        '''
        creeaza butoanele de pe tabla de joc
        :param **kwargs: nu contine nimic, specific librariei kivy, fara nu functioneaza
        '''
        super().__init__(**kwargs)
        for i in range(15):
            for j in range(15):
                b = Button(text = "")
                if B.board[i][j][1] == 'R':  #if color off square is red then text of the button will be TW
                    b.text = "TW"           #TW = triple word, it will triple the score of the entire word
                    b.background_color = (1,0,0,1)
                elif B.board[i][j][1] == 'Y':
                    b.text = "DW"          #DW = double word score
                    b.background_color = (1,1,0.2,1)
                elif B.board[i][j][1] == 'B':
                    b.text = "TL"          #TL = triple letter score
                    b.background_color = (0,0,1,1)
                elif B.board[i][j][1] == 'G':
                    b.text = "DL"          #DL = double letter score
                    b.background_color = (0,1,0,1)
                
                b.id = (i,j)      #id of the button will be the coordinates from the board grid (tuple)
                B.board[i][j][2] = b    #add button to the board matrix
                b.bind(on_press = self.on_button_click)
                self.add_widget(b)
        
        B.board[7][7][2].background_color = (1,0.4,0.69,1)  #MIDDLE OF THE BOARD WILL HAVE COLOR PINK


    def on_button_click(self, instance: Button) -> None: #instance is the button pressed (obj) from the board
        '''
        butonul preia textul de la cartea asezata pe el
        :param instance: butonul in sine, pentru a-l putea modifica
        :return: None
        '''
        if G.selected_tile_value != 0 and G.selected_tile_value != "":    #if the player selected a tile        
            i,j = instance.id       #get coordinates of the button, they are represented by button's id
            G.tiles_played_this_round.append(G.selected_tile_value)      #save tiles played this round
            G.tiles_coordinates_this_round.append((i,j))
            G.tiles_ids_played_this_round.append(G.selected_tile_id)

            instance.background_color = (0.95,0.95,0.95,1)   #background color
            instance.disabled = True     #disable button
            instance.color = (0,0,0,1)   #text color

            for b in P.letter_buttons:          #disabling button representing the player's played tile
                if str(b.id) == str(G.selected_tile_id):
                    b.text = ""
                    b.disabled = True    
                   
            instance.text = str(G.selected_tile_value) #update text of the selected button
            B.board[i][j][0] = G.selected_tile_value   #update the board matrix with the value it holds
            G.selected_tile_value = 0     #reset selected_tile to not be able to put the same tile on board multiple times



         
    
class Tiles(GridLayout):
    '''
    cartile din "mana" jucatorului
    '''
    def __init__(self, **kwargs)->None:
        """
        creeaza 7 butoane cu valorile cartilor jucatorului
        :param **kwargs: specific librariei kivy pt a instantia clasa layout
        :return: None
        """
        super().__init__(**kwargs)
        for i in range(7):   #adding 7 tiles that player has
            l = Button(text = P.letters[i], on_press = self.on_button_click)
            l.id = i
            self.add_widget(l)
            P.letter_buttons.append(l)     #add buttons to player buttons list 
            G.player_tiles.append(l)        #store all 7 buttons(tiles)
    
    def on_button_click(self, instance: Button) -> None:
        '''
        cand se apasa se tine minte valoarea(textul) butonului apasat
        :param instance: butonul apasat este dat ca referinta
        :return: None
        '''
        G.selected_tile_value = instance.text  #get text of the pressed button
        G.selected_tile_id = instance.id       #get id of the pressed button
        

    

#Header class from GUI
class Header(BoxLayout):
    """
    interfata grafica la partea superioara a interfetei grafice
    """
    pass


        
#this is the panel from right which contains a list with last words played and 4 buttons (GUI)
class Right(BoxLayout):
    """
    interfata grafica la panelul din dreapta cu last words played si 3 butoane
    """
    def on_button_play_click(self) -> None:   #when click on play button
        """daca cartile au fost asezate gresit se reseteaza runda, daca au fost asezate corect se extrag cuvintele si se cauta in dictionar
        :return: None
        """
        if G.game_over != 1:      #if the game is still running
            print(G.tiles_played_this_round)
            if G.verify_tiles_placement() == "WRONG PLACEMENT" :  #if tiles were placed wrong we reset the round
                    #remove tiles placed this round on the board and give it back the player
                for i,j in G.tiles_coordinates_this_round:
                    B.board[i][j][0] = 0              # 0 = default value
                    B.board[i][j][2].text = ""        #erase tile from board
                    B.board[i][j][2].background_color = (1,1,1,1)   #background color
                    B.board[i][j][2].disabled = False     #enable button
                    B.board[i][j][2].color = (1,1,1,1)   #text color
                
            
                for i in range(15):
                    for j in range(15):
                        if B.board[i][j][0] == 0:   #if the square is not occupied by a tile then recolor the board were nedded
                            if B.board[i][j][1] == 'R':  #if color off square is red then text of the button will be TW
                                B.board[i][j][2].text = "TW"           #TW = triple word, it will triple the score of the entire word
                                B.board[i][j][2].background_color = (1,0,0,1)
                            elif B.board[i][j][1] == 'Y':
                                B.board[i][j][2].text = "DW"          #DW = double word score
                                B.board[i][j][2].background_color = (1,1,0.2,1)
                            elif B.board[i][j][1] == 'B':
                                B.board[i][j][2].text = "TL"          #TL = triple letter score
                                B.board[i][j][2].background_color = (0,0,1,1)
                            elif B.board[i][j][1] == 'G':
                                B.board[i][j][2].text = "DL"          #DL = double letter score
                                B.board[i][j][2].background_color = (0,1,0,1)
                if B.board[7][7][0] == 0:  #if the middle square is not occupied reset its color
                    B.board[7][7][2].background_color = (1,0.4,0.69,1)
                
                    
                for id in reversed(G.tiles_ids_played_this_round):
                    for tile in G.player_tiles:
                        if tile.id == id:
                            if len(G.tiles_played_this_round)>0:
                                tile.text = G.tiles_played_this_round.pop()         #Give tiles back to the player
                            tile.disabled = False  
                            break  
            else:    #If the placement was CORRECT
                nr = 0
                try:
                    for i in G.tiles_ids_played_this_round:
                        if i-nr < len(P.letters):
                            if i<0:  #to avoid list index out of range
                                i=0 
                            del P.letters[i-nr]
                        nr+=1                #remove played tiles from the stack
                except Exception as e:
                    print(str(e)) 
                   # print(i-nr)
                  #  print(P.letters)
                   # print(G.tiles_ids_played_this_round) 
                   # exit(1)  

                P.nr_letters = len(P.letters)    #how many letters left in players stack
                B.give_player_letters(P)    #refill the player's stack with letters 
            
                n = len(P.letters)      #how many letters player has
                if n<7:
                    for i in range(n):
                        G.player_tiles[i].text = P.letters[i]
                    for i in range(7):
                        G.player_tiles[i].disabled = False
                else:
                    for i in range(7):
                        G.player_tiles[i].text = P.letters[i]
                        G.player_tiles[i].disabled = False

        
            
            G.extract_words() 
            G.search_words()
            #Reset variables about the tiles played this round bc we finished our turn
            G.tiles_coordinates_this_round = []
            G.tiles_played_this_round = []
            G.tiles_ids_played_this_round = []
            G.selected_tile_value = 0
            G.selected_tile_id = -1
            G.words_formed_this_round = [] 

            

        
            """            
            for i in range(15):
                for j in range(15):
                    print(B.board[i][j][0], end=" ")
                print()
            """
    #Button clear deletes the tiles placed this round on board and gives it back to the player, it doesen't change turn
    def on_button_clear_click(self) -> None:
        """
        se sterg toate cartile asezate pe tabla in runda curenta
        :return: None
        """
        for i,j in G.tiles_coordinates_this_round:
            B.board[i][j][0] = 0              # 0 = default value
            B.board[i][j][2].text = ""        #erase tile from board
            B.board[i][j][2].background_color = (1,1,1,1)   #background color
            B.board[i][j][2].disabled = False     #enable button
            B.board[i][j][2].color = (1,1,1,1)   #text color
        
    
        for i in range(15):
            for j in range(15):
                if B.board[i][j][0] == 0:   #if the square is not occupied by a tile then recolor the board were nedded
                    if B.board[i][j][1] == 'R':  #if color off square is red then text of the button will be TW
                        B.board[i][j][2].text = "TW"           #TW = triple word, it will triple the score of the entire word
                        B.board[i][j][2].background_color = (1,0,0,1)
                    elif B.board[i][j][1] == 'Y':
                        B.board[i][j][2].text = "DW"          #DW = double word score
                        B.board[i][j][2].background_color = (1,1,0.2,1)
                    elif B.board[i][j][1] == 'B':
                        B.board[i][j][2].text = "TL"          #TL = triple letter score
                        B.board[i][j][2].background_color = (0,0,1,1)
                    elif B.board[i][j][1] == 'G':
                        B.board[i][j][2].text = "DL"          #DL = double letter score
                        B.board[i][j][2].background_color = (0,1,0,1)
        if B.board[7][7][0] == 0:  #if the middle square is not occupied reset its color
            B.board[7][7][2].background_color = (1,0.4,0.69,1)
           
            
        for id in reversed(G.tiles_ids_played_this_round):
            for tile in G.player_tiles:
                if tile.id == id:
                    if len(G.tiles_played_this_round)>0:
                        tile.text = G.tiles_played_this_round.pop()         #Give tiles back to the player
                    tile.disabled = False  
                    break  
        
        G.tiles_coordinates_this_round = []        #Reset all info about tiles played this round
        G.tiles_played_this_round = []
        G.tiles_ids_played_this_round = []
        G.selected_tile_value = 0
        G.selected_tile_id = -1
        G.words_formed_this_round = [] 
        #Button pass finishes the turn without doing anyting
    def on_button_pass_click(self) -> None:
        """se schimba tura catre celalalt player
        :return: None
        """
        if G.turn == 1:
            A.turn = "Player1 turn"
            G.turn = 0
            i=0  #index                   #change tiles to the other player
            for b in G.player_tiles:
                b.text = P.letters[i]
                i+=1

        else:
            A.turn = "Player2 turn"
            G.turn = 1                    #change tiles to the other player
            i=0  #index  
            for b in G.player_tiles:
                b.text = P2.letters[i]
                i+=1
        G.nr_of_pass +=1    #increment nr of pass, when it is equal to three game is over
        if G.nr_of_pass == 3:     #if we passed the round 3 times
            score_player1 = A.score_player1.split()
            score_player2 = A.score_player2.split()
            if int(score_player1[1]) > int(score_player2[1]):
                A.turn = "Player1 win"
            elif int(score_player1[1]) < int(score_player2[1]):
                A.turn = "Player2 win"
            else:
                A.turn = "Draw"
            G.game_over = 1
            for b in P.letter_buttons:    #disable tiles
                b.disabled = True
            


B = Board()
P = Player()
G = Game() 
#C = Computer()     #computer in progress
P2 = Player()      #player2
 
B.give_player_7_letters(P)
B.give_player_7_letters(P2)



global words                      #These are all the words from scrabble dictionary
words = []
f = open("dictionary.txt", "r")
#f = open(sys.argv[1], "r")          #this line is if we want to give as parameter the dictionary file
for x in f:
    words.append(x[:-2])         #last two characters are '\n'
f.close()


#P.letters = ['A', 'C', 'C', 'O', 'U', 'N', 'T']     #used for fixing a bug
#P2.letters = ['B', 'S', 'O', 'L', 'U', 'T', 'E']
 
A = ScrabbleApp()
A.run()

 