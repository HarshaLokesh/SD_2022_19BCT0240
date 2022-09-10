# level 1
def display_player_grid(grid):
    print("Current Grid:")
    for player_row in grid:
        for player in player_row:
            print(player, end="        ")
        print()

def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return i, x.index(v)

def check_win(grid):
    pass

def moves_A(move):
    if move == "P1:F":
        r, c = index_2d(grid, "A-P1")
        print(r, c)


grid = [
['-',	'-'	,	'-'		,'-'	,	'-'], 
['-',	'-'	,	'-'		,'-'	,	'-'],
['-',	'-'	,	'-'		,'-'	,	'-'],
['-',	'-'	,	'-'		,'-'	,	'-'],
['-',	'-'	,	'-'		,'-'	,	'-']
]

if __name__ == '__main__':
    n = 5 # number of players is 5


    print("Player1 Input: ") #input names of pawns player A
    player_A = input()
    player_A = player_A.split(",") #input 5 player with comma for Player A
    #adding players to board
    for i in range(5):   
        grid[0][i] = player_A[i]
    display_player_grid(grid)

    print() #leaving lines
    print()

    print("Player2 Input: ") #input names of pawns player B
    player_B = input()
    player_B = player_B.split(",") #input 5 player with comma for Player B
    #adding players to board
    for i in range(5):
        grid[4][i] = player_B[i]
    display_player_grid(grid)

    moves_A("P1:F")
    