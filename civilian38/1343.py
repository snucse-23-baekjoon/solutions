board = input()

if any(map(lambda x: len(x) % 2 == 1, board.split('.'))):
    print(-1)
else:
    while board:
        if board[0] == '.':
            board = board[1:]
            print('.', end='')
        else:
            length = 0
            while board and board[0] == 'X':
                length += 1
                board = board[1:]
            print('AAAA' * (length // 4) + 'BB' * ((length % 4) // 2),end='')  