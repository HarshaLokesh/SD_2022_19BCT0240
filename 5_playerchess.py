# level 1
def display_player_grid(grid):
    for player_row in grid:
        for player in player_row:
            print(player, end=" ")
        print()


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
    
    print("Player2 Input: ") #input names of pawns player B
    player_B = input()
    player_B = player_B.split(",") #input 5 player with comma for Player B

    
    #adding players to board
    for i in range(5):   
        grid[0][i] = player_A[i]
    for i in range(5):
        grid[4][i] = player_B[i]

    display_player_grid(grid)
    