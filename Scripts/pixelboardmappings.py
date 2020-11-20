''' 
Scripts to map between pixels and boards
These functions are used to create and map between pixels and 0-7 grid 
references.
'''
EDGE_BORDER = 7
UPPER_BORDER = 55
INNER_BORDER = 5
HALF_SQUARE = 25
J0 = EDGE_BORDER + HALF_SQUARE
I0 = UPPER_BORDER + HALF_SQUARE
DIFF = 2 * HALF_SQUARE + INNER_BORDER


def board2Pixel():
    M = []
    for i in range(8):
        row = []
        for j in range(8):
            position = (J0 + (j * DIFF), I0 + (i * DIFF))
            row.append(position)
        M.append(row)
    return M


def pixel2Board(x, y):
    zerod_j = x - EDGE_BORDER
    zerod_i = y - UPPER_BORDER
    index_j = (zerod_j // DIFF)
    index_i = (zerod_i // DIFF) 
    if  (index_j + INNER_BORDER < DIFF) and (index_j >= 0) and (index_j <= 7):
        if (index_i + INNER_BORDER < DIFF) and (index_i >= 0) and (index_i <= 7):
            return True, index_i, index_j
    return False, False, False