
# level 1


grid = [
['-',	'-'	,	'-'		,'-'	,	'-'], 
['-',	'-'	,	'-'		,'-'	,	'-'],
['-',	'-'	,	'-'		,'-'	,	'-'],
['-',	'-'	,	'-'		,'-'	,	'-'],
['-',	'-'	,	'-'		,'-'	,	'-']
]
# display GUI grid for the game
def display_player_grid(grid):
    print("Current Grid:")
    for player_row in grid:
        for player in player_row:
            if player == "-":
                print(player, end="                    ")
            else:
                print(player, end="                 ")
        print()

def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return i, x.index(v)

#check winner of game
def check_win(grid):
    list_of_B = ["B-P1","B-P2","B-P3","B-P4","B-P5"]
    list_of_A = ["A-P1","A-P2","A-P3","A-P4","A-P5"]
    
    for r in grid:
        for c in r:
            if c in list_of_B:
                i = 1
                
                 

    for r in grid:
        for c in r:
            if c in list_of_A:
                j = 1
                
    if i != 1:
        return "A"
    if j != 1:
        return "B"
    
    

def moves_A_level1():
    list_of_B = ["B-P1","B-P2","B-P3","B-P4","B-P5"]

    
    print("Enter PLAYER A move:") # Enter exact characters P1:F, P2:F, P1:L, etc.....
    move = input()

    
    # P1

    if move == "P1:F":
        r, c = index_2d(grid, "A-P1")
        if (grid[r-1][c] == '-' or (grid[r-1][c] in list_of_B)) and r>0:
            grid[r-1][c] = "A-P1"
            grid[r][c] = '-'

    if move == "P1:B":
        r, c = index_2d(grid, "A-P1")
        if (grid[r+1][c] == '-' or (grid[r+1][c] in list_of_B)) and r<4:
            grid[r+1][c] = "A-P1"
            grid[r][c] = '-'
    
    if move == "P1:R":
        r, c = index_2d(grid, "A-P1")
        if (grid[r][c+1] == '-' or (grid[r][c+1] in list_of_B)) and c<4:
            grid[r][c+1] = "A-P1"
            grid[r][c] = '-'

    if move == "P1:L":
        r, c = index_2d(grid, "A-P1")
        if (grid[r][c-1] == '-' or (grid[r][c-1] in list_of_B)) and c>0:
            grid[r][c-1] = "A-P1"
            grid[r][c] = '-'
        
    # P2
    
    if move == "P2:F":
        r, c = index_2d(grid, "A-P2")
        if (grid[r-1][c] == '-' or (grid[r-1][c] in list_of_B)) and r>0:
            grid[r-1][c] = "A-P2"
            grid[r][c] = '-'

    if move == "P2:B":
        r, c = index_2d(grid, "A-P2")
        if (grid[r+1][c] == '-' or (grid[r+1][c] in list_of_B)) and r<4:
            grid[r+1][c] = "A-P2"
            grid[r][c] = '-'
    
    if move == "P2:R":
        r, c = index_2d(grid, "A-P2")
        if (grid[r][c+1] == '-' or (grid[r][c+1] in list_of_B)) and c<4:
            grid[r][c+1] = "A-P2"
            grid[r][c] = '-'

    if move == "P2:L":
        r, c = index_2d(grid, "A-P2")
        if (grid[r][c-1] == '-' or (grid[r][c-1] in list_of_B)) and c>0:
            grid[r][c-1] = "A-P2"
            grid[r][c] = '-'

    # P3
    
    if move == "P3:F":
        r, c = index_2d(grid, "A-P3")
        if (grid[r-1][c] == '-' or (grid[r-1][c] in list_of_B)) and r>0:
            grid[r-1][c] = "A-P3"
            grid[r][c] = '-'

    if move == "P3:B":
        r, c = index_2d(grid, "A-P3")
        if (grid[r+1][c] == '-' or (grid[r+1][c] in list_of_B)) and r<4:
            grid[r+1][c] = "A-P3"
            grid[r][c] = '-'
    
    if move == "P3:R":
        r, c = index_2d(grid, "A-P3")
        if (grid[r][c+1] == '-' or (grid[r][c+1] in list_of_B)) and c<4:
            grid[r][c+1] = "A-P3"
            grid[r][c] = '-'

    if move == "P3:L":
        r, c = index_2d(grid, "A-P3")
        if (grid[r][c-1] == '-' or (grid[r][c-1] in list_of_B)) and c>0:
            grid[r][c-1] = "A-P3"
            grid[r][c] = '-'

    # P4
    
    if move == "P4:F":
        r, c = index_2d(grid, "A-P4")
        if (grid[r-1][c] == '-' or (grid[r-1][c] in list_of_B)) and r>0:
            grid[r-1][c] = "A-P4"
            grid[r][c] = '-'

    if move == "P4:B":
        r, c = index_2d(grid, "A-P4")
        if (grid[r+1][c] == '-' or (grid[r+1][c] in list_of_B)) and r<4:
            grid[r+1][c] = "A-P4"
            grid[r][c] = '-'
    
    if move == "P4:R":
        r, c = index_2d(grid, "A-P4")
        if (grid[r][c+1] == '-' or (grid[r][c+1] in list_of_B)) and c<4:
            grid[r][c+1] = "A-P4"
            grid[r][c] = '-'

    if move == "P4:L":
        r, c = index_2d(grid, "A-P4")
        if (grid[r][c-1] == '-' or (grid[r][c-1] in list_of_B)) and c>0:
            grid[r][c-1] = "A-P4"
            grid[r][c] = '-'

    # P5
    
    if move == "P5:F":
        r, c = index_2d(grid, "A-P5")
        if (grid[r-1][c] == '-' or (grid[r-1][c] in list_of_B)) and r>0:
            grid[r-1][c] = "A-P5"
            grid[r][c] = '-'

    if move == "P5:B":
        r, c = index_2d(grid, "A-P5")
        if (grid[r+1][c] == '-' or (grid[r+1][c] in list_of_B)) and r<4:
            grid[r+1][c] = "A-P5"
            grid[r][c] = '-'
    
    if move == "P5:R":
        r, c = index_2d(grid, "A-P5")
        if (grid[r][c+1] == '-' or (grid[r][c+1] in list_of_B)) and c<4:
            grid[r][c+1] = "A-P5"
            grid[r][c] = '-'

    if move == "P5:L":
        r, c = index_2d(grid, "A-P5")
        if (grid[r][c-1] == '-' or (grid[r][c-1] in list_of_B)) and c>0:
            grid[r][c-1] = "A-P5"
            grid[r][c] = '-'

   


def moves_B_level1():
    list_of_A = ["A-P1","A-P2","A-P3","A-P4","A-P5"]

    print("Enter PLAYER B move:") # Enter exact characters P1:F, P2:F, P1:L, etc.....
    move = input()
    
    # P1

    if move == "P1:B":
        r, c = index_2d(grid, "B-P1")
        if (grid[r-1][c] == '-' or (grid[r-1][c] in list_of_A)) and r>0:
            grid[r-1][c] = "B-P1"
            grid[r][c] = '-'

    if move == "P1:F":
        
        r, c = index_2d(grid, "B-P1")
        print(r,c)
        if (grid[r+1][c] == '-' or (grid[r+1][c] in list_of_A)) and r<4:
            grid[r+1][c] = "B-P1"
            grid[r][c] = '-'
    
    if move == "P1:L":
        r, c = index_2d(grid, "B-P1")
        if (grid[r][c+1] == '-' or (grid[r][c-1] in list_of_A)) and c<4:
            grid[r][c+1] = "B-P1"
            grid[r][c] = '-'

    if move == "P1:R":
        r, c = index_2d(grid, "B-P1")
        if (grid[r][c-1] == '-' or (grid[r][c-1] in list_of_A)) and c>0:
            grid[r][c-1] = "B-P1"
            grid[r][c] = '-'
        
    # P2
    
    if move == "P2:B":
        r, c = index_2d(grid, "B-P2")
        if (grid[r-1][c] == '-' or (grid[r-1][c] in list_of_A)) and r>0:
            grid[r-1][c] = "B-P2"
            grid[r][c] = '-'

    if move == "P2:F":
        r, c = index_2d(grid, "B-P2")
        if (grid[r+1][c] == '-' or (grid[r+1][c] in list_of_A)) and r<4:
            grid[r+1][c] = "B-P2"
            grid[r][c] = '-'
    
    if move == "P2:L":
        r, c = index_2d(grid, "B-P2")
        if (grid[r][c+1] == '-' or (grid[r][c+1] in list_of_A)) and c<4:
            grid[r][c+1] = "B-P2"
            grid[r][c] = '-'

    if move == "P2:R":
        r, c = index_2d(grid, "B-P2")
        if (grid[r][c-1] == '-' or (grid[r][c-1] in list_of_A)) and c>0:
            grid[r][c-1] = "B-P2"
            grid[r][c] = '-'

    # P3
    
    if move == "P3:B":
        r, c = index_2d(grid, "B-P3")
        if (grid[r-1][c] == '-' or (grid[r-1][c] in list_of_A)) and r>0:
            grid[r-1][c] = "B-P3"
            grid[r][c] = '-'

    if move == "P3:F":
        r, c = index_2d(grid, "B-P3")
        if (grid[r+1][c] == '-' or (grid[r+1][c] in list_of_A)) and r<4:
            grid[r+1][c] = "B-P3"
            grid[r][c] = '-'
    
    if move == "P3:L":
        r, c = index_2d(grid, "B-P3")
        if (grid[r][c+1] == '-' or (grid[r][c+1] in list_of_A)) and c<4:
            grid[r][c+1] = "B-P3"
            grid[r][c] = '-'

    if move == "P3:R":
        r, c = index_2d(grid, "B-P3")
        if (grid[r][c-1] == '-' or (grid[r][c-1] in list_of_A)) and c>0:
            grid[r][c-1] = "B-P3"
            grid[r][c] = '-'

    # P4
    
    if move == "P4:B":
        r, c = index_2d(grid, "B-P4")
        if (grid[r-1][c] == '-' or (grid[r-1][c] in list_of_A)) and r>0:
            grid[r-1][c] = "B-P4"
            grid[r][c] = '-'

    if move == "P4:F":
        r, c = index_2d(grid, "B-P4")
        if (grid[r+1][c] == '-' or (grid[r+1][c] in list_of_A)) and r<4:
            grid[r+1][c] = "B-P4"
            grid[r][c] = '-'
    
    if move == "P4:L":
        r, c = index_2d(grid, "B-P4")
        if (grid[r][c+1] == '-' or (grid[r][c+1] in list_of_A)) and c<4:
            grid[r][c+1] = "B-P4"
            grid[r][c] = '-'

    if move == "P4:R":
        r, c = index_2d(grid, "B-P4")
        if (grid[r][c-1] == '-' or (grid[r][c-1] in list_of_A)) and c>0:
            grid[r][c-1] = "B-P4"
            grid[r][c] = '-'

    # P5
    
    if move == "P5:B":
        r, c = index_2d(grid, "B-P5")
        if (grid[r-1][c] == '-' or (grid[r-1][c] in list_of_A)) and r>0:
            grid[r-1][c] = "B-P5"
            grid[r][c] = '-'

    if move == "P5:F":
        r, c = index_2d(grid, "B-P5")
        if (grid[r+1][c] == '-' or (grid[r+1][c] in list_of_A)) and r<4:
            grid[r+1][c] = "B-P5"
            grid[r][c] = '-'
    
    if move == "P5:L":
        r, c = index_2d(grid, "B-P5")
        if (grid[r][c+1] == '-' or (grid[r][c+1] in list_of_A)) and c<4:
            grid[r][c+1] = "B-P5"
            grid[r][c] = '-'

    if move == "P5:R":
        r, c = index_2d(grid, "B-P5")
        if (grid[r][c-1] == '-' or (grid[r][c-1] in list_of_A)) and c>0:
            grid[r][c-1] = "B-P5"
            grid[r][c] = '-'

   
     


if __name__ == '__main__':
    n = 5 # number of players is 5

    print("Player1 Input: ") #input names of pawns player A
    player_B = input()
    player_B = player_B.split(",") #input 5 player with comma for Player A
    #adding players to board
    for i in range(5):   
        grid[0][i] = "B-"+player_B[i]
    display_player_grid(grid)

    print() #leaving lines
    print()

    print("Player2 Input: ") #input names of pawns player B
    player_A = input()
    player_A = player_A.split(",") #input 5 player with comma for Player B
    #adding players to board
    for i in range(5):
        grid[4][i] = "A-"+player_A[i]
    display_player_grid(grid)


    while(True):

        moves_A_level1()
        if check_win(grid) == "A":
            print("Player A won")
            break
        if check_win(grid) == "B":
            print("Player B won")
            break

        display_player_grid(grid)

        moves_B_level1()
        if check_win(grid) == "A":
            print("Player A won")
            break
        if check_win(grid) == "B":
            print("Player B won")
            break

        display_player_grid(grid)


