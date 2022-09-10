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


display_player_grid(grid)