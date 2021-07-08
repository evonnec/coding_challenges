#!/usr/bin/env python3

# https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

# Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overpopulation.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

input_board = [[0, 0, 0, 0], 
               [0, 1, 1, 0], 
               [0, 1, 1, 0], 
               [0, 0, 0, 0]]
input_board2 = [[0, 0, 0, 0, 0], 
                [0, 0, 1, 0, 0], 
                [0, 0, 1, 0, 0], 
                [0, 0, 1, 0, 0], 
                [0, 0, 0, 0, 0]]

outpt_board2 = [[0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0], 
                [0, 1, 1, 1, 0], 
                [0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0]]
# rows are m, columns are n

# generate next board function

def generate_next_board(board):
    next_board = []
    for ind_m, m in enumerate(board):
        new_row = []
        for ind_cell, cell in enumerate(m):
            num_of_neighbors = count_neighbors(ind_m, ind_cell, board)
            if cell == 1:
                if num_of_neighbors < 2 or num_of_neighbors > 3:
                    new_row.append(0)
                elif num_of_neighbors == 2 or num_of_neighbors == 3:
                    new_row.append(1)
            elif cell == 0:
                if num_of_neighbors == 3:
                    new_row.append(1)
                else:
                    new_row.append(0)
        next_board.append(new_row)
        # print(ind_m, new_row, next_board)
    print(next_board)
    return next_board
    
# count neighbors of a specific cell in order to determine how many neighbors live

def count_neighbors(r, c, board):
    # count_neighbors(0, 0, board)
    
    # iterate thru list of lists m x n board.
    # assign cells an address (maybe)
    
    # index to the top left, top middle, top right --> count live cells
    # index to the same row left, same row right --> add more live cells maybe
    # index to the bottom left, bottom middle, bottom right --> add last live cells
    # r, c
    # r-1, c-1; r-1 c; r-1, c+1; r c-1, r c+1; r+1, c-1, r+1, c, r+1, c+1
    # print("this is count neighbors for r: " + str(r) + ", c: " + str(c))
    neighbor_count = 0
    # for r_ind, c_ind in [[r-1, c-1], [r-1, c], [r-1,c+1], [r, c-1], [r,c+1], [r+1, c-1], [r+1,c], [r+1,c+1]]:
    for r_add, c_add in [(r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1)]:
        try:
            if board[r_add][c_add]:
                if board[r_add][c_add] == 1:
                    neighbor_count += 1
                    print("<<neighbor count: " + str(neighbor_count) + " for board location (" + str(r_add) + ", " + str(c_add) + ")>>")
        except (IndexError):
            print("board location (" + str(r_add) + ", " + str(c_add) + ") doesn't exist, moving on")
            continue
    print(neighbor_count)
    return neighbor_count
    

print(generate_next_board(generate_next_board(generate_next_board(input_board2))))

assert generate_next_board(generate_next_board(generate_next_board(input_board2))) == outpt_board2
