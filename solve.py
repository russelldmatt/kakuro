# |    |    |  0 | 1 |   |
# |    |    |  2 | 3 | 4 |
# |  5 |  6 |  7 | 8 | 9 |
# | 10 | 11 | 12 |   |   |
# |    | 13 | 14 |   |   |

sum_constraints = [
    # horizontal
    ([0,1], 8),
    ([2,3,4], 21),
    ([5,6,7,8,9], 18),
    ([10,11,12], 21),
    ([13,14], 11),
    # vertical
    ([5,10], 13),
    ([6,11,13], 8),
    ([0,2,7,12,14], 34),
    ([1,3,8], 16),
    ([4,9], 8),
]

def translate(board, row_or_col):
    return [ board[x] for x in row_or_col if board[x] ]

def how_many_missing(board, row_or_col):
    return len([ board[x] for x in row_or_col if not(board[x]) ])

def possibilities(board, pos):
    left = set(range(1,10))
    for (row_or_col, sum_) in sum_constraints:
        if pos in row_or_col:
            translated_row_or_col = translate(board, row_or_col)
            # remove anything that's already used in a row or col
            left = left.difference(set(translated_row_or_col))
            # also can't go over
            current_sum = sum(translated_row_or_col)
            left = { x for x in left if (x + current_sum) <= sum_ }
            # if you're the last one left, you better be exactly the diff
            if how_many_missing(board, row_or_col) == 1:
                left = left.intersection({ sum_ - current_sum })
    return left

def brute_force(board):
    def brute_force_loop(board, pos):
        if pos == len(board): return board # solved
        # print "----------------"
        # print "pos:", pos
        # print "board:", board
        ps = possibilities(board, pos)
        # print "possibilities:", ps
        if ps == {}: 
            return None
        else:
            for x in ps:
                board[pos] = x
                solved = brute_force_loop(board, pos + 1)
                if solved: return solved
            # none worked
            board[pos] = None
            return None
    return brute_force_loop(board, 0)

board = [None] * 15
print board
    
print possibilities(board, 0)
print brute_force(board)

