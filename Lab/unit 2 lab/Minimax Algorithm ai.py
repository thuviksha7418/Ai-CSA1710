board = [' '] * 9

def display():
    for i in range(0, 9, 3):
        print(board[i], '|', board[i+1], '|', board[i+2])

player = 'X'

for turn in range(9):
    display()
    pos = int(input("Enter position (1-9): ")) - 1

    if pos < 0 or pos > 8 or board[pos] != ' ':
        print("Invalid position! Try again.")
        continue

    board[pos] = player

    win = False
    for a, b, c in [(0,1,2), (3,4,5), (6,7,8),
                    (0,3,6), (1,4,7), (2,5,8),
                    (0,4,8), (2,4,6)]:
        if board[a] == board[b] == board[c] == player:
            win = True

    if win:
        display()
        print(player, "wins!")
        break

    player = 'O' if player == 'X' else 'X'

else:
    display()
    print("Game Draw!")
