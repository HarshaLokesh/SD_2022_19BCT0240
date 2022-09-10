# level 1


grid = [
['-',	'-'	,	'-'		,'-'	,	'-'], 
['-',	'-'	,	'-'		,'-'	,	'-'],
['-',	'-'	,	'-'		,'-'	,	'-'],
['-',	'-'	,	'-'		,'-'	,	'-'],
['-',	'-'	,	'-'		,'-'	,	'-']
]

def display_player_grid(grid):
    print("Current Grid:")
    for player_row in grid:
        for player in player_row:
            if player == "-":
                print(player, end="                    ")
            else:
                print(player, end="                ")
        print()

def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return i, x.index(v)

def check_win(grid):
    list_of_B = ["B-P1","B-P2","B-P3","B-P4","B-P5"]
    list_of_A = ["A-P1","A-P2","A-P3","A-P4","A-P5"]
    for i in range(5):
        if(any(("B-P1","B-P2","B-P3","B-P4","B-P5") in sub for sub in grid)):
            print("NOSDFSDf")
    pass
    

def moves_A_level1(move):
    list_of_B = ["B-P1","B-P2","B-P3","B-P4","B-P5"]
    if move == "P1:F":
        r, c = index_2d(grid, "A-P1")
        if grid[r-1][c] == '-' or list_of_B.includes(grid[r-1][c]):
            grid[r-1][c] = "A-P1"
            grid

    if move == "P1:B":
        r, c = index_2d(grid, "A-P1")
        if grid[r][c] == '-' or list_of_B.includes(grid[r][c]):
            grid[r][c] = "A-P1"
        


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

    moves_A_level1("P1:F")
    
    #check_win(grid)
    
    