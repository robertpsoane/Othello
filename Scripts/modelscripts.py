''' Model scripts

These scripts are used by the game model at on load to generate global 
variables which it will use throughout the game.

I have put them in a separate file to keep the model code looking tidier.

'''


def makeGradingStrategy():
    '''
    Function to make a grading matrix, inspired by code here
    https://github.com/yuxuan006/Othello/blob/ac33536bc35c7e50da93aab937e3dfee
    5c258a7f/yuchai.py#L19
    '''
    board = []
    for i in range(8):
        row = []
        for j in range(8):
            if (i, j) in CORNERS:
                row.append(10)
            elif (i, j) in OFF_CORNERS:
                row.append(-2)
            elif (i, j) in EDGES:
                row.append(2)
            else:
                row.append(1)
        board.append(row)
    return board

# Important Model Variables
GRID = {
'G2I' : {'row': {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, 
                '8': 7},
        'col':{'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6,
                'H': 7},
        },
'I2G':{'row': {'0': '1', '1': '2', '2': '3', '3': '4', '4': '5',
                '5': '6', '6': '7', '7': '8'},
    'col': {'0': 'A', '1': 'B', '2': 'C', '3': 'D', '4': 'E', '5': 'F',
                '6': 'G', '7': 'H', }
        }
} 
COLOUR = {
    'b': 'Black',
    'w': 'White'
}
SHIFTS = [-1, 0, 1]


# Setting up 'global' variables. 
CENTRE_LEFT, CENTRE_RIGHT = 3, 4
CORNERS = [
    (0, 0),
    (0, 7),
    (7, 0),
    (7, 7)
]

OFF_CORNERS = [(1, 0), (0, 1), (1, 1),
                (0, 6), (1, 7), (6, 6),
                (6, 0), (7, 1), (6, 1),
                (6, 7), (7, 6), (6, 6)]

EDGES = []
for i in [0, 7]:
    for j in range(8):
        EDGES.append((i, j))

for j in [0, 7]:
    for i in range(8):
        EDGES.append((i, j))

EDGES = list(set(EDGES))
CORNER_BONUS = 30
DEFAULT_DEPTH = 5

GRADING_STRATEGY = makeGradingStrategy()
