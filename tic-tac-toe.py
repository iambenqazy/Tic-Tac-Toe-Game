import random


def display_board(board):
    """
    This function prints a tic-tac-toe board
    like below:
    test_board = ['#','X','O','X','O','X','O','X','O','X']
     X | O | X
    ---|---|---
     O | X | O
    ---|---|---
     X | O | X
    """
    board = board[1:]
    h_sep = '-' * 3

    for i in reversed(range(3)):
        print(f"{board[i * 3]:^3}|{board[i * 3 + 1]:^3}|{board[i * 3 + 2]:^3}")

        if i != 0:
            print(f"{h_sep:^3}|{h_sep:^3}|{h_sep:^3}")


def player_input():
    """
    OUTPUT = (Player 1 marker, Player 2 marker)
    """

    mark_input = ''
    mark_list = ['X', 'O']

    # check if user input is in mark_list
    while not mark_input in mark_list:
        mark_input = input("Player 1, select your mark either 'X' or 'O'")[0].upper()

    if mark_input == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


def place_marker(board, marker, position):
    position_list = list(range(1, 10))

    if position in position_list:
        board[position] = marker
        return board
    else:
        print(
            f"The number entered '{position}' is out of range on the board. "
            f"\nPlease enter a valid number between (1 and 9).")


def win_check(board, mark):
    """
        This function checks for wins on the board

        r_win = [[7,8,9],[4,5,6],[1,2,3]]
        c_win = [[1,4,7],[2,5,8],[3,6,9]]
        d_win = [[1,5,9],[3,5,7]]

    """

    board_ = [el == mark for el in board]

    if (any([
        all(board_[1:4]),
        all(board_[4:7]),
        all(board_[7:10]),
        all(board_[slice(1, 8, 3)]),
        all(board_[slice(2, 9, 3)]),
        all(board_[slice(3, 10, 3)]),
        all(board_[slice(1, 10, 4)]),
        all(board_[slice(3, 8, 2)])
    ])):
        return True
    return False


def choose_first_player():
    flip = random.randint(0, 1)

    if flip == 0:
        return "Player 1"
    else:
        return "Player 2"


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    # Board is full so we return True
    return True


def player_choice(board, player):
    position = 0

    while position not in list(range(1, 10)) or not space_check(board, position):
        if player == 'Player 1':
            position = int(input("Player 1, choose a position (1-9): "))
        else:
            position = int(input("Player 2, choose a position (1-9): "))

    return position


def replay():
    choice = input("Play again? Enter Yes or No: ").upper()

    return choice == 'YES'


# while loop to keep running the game
print("Welcome to TIC-TAC-TOE")

if __name__ == '__main__':

    while True:

        # play the game

        # set everything up (board, who is first, choose marker X,O)
        the_board = [' '] * 10
        player1_marker, player2_marker = player_input()

        turn = choose_first_player()
        print(f"{turn} will go first.")

        play_game = input("Ready to play? Yes or No").upper()

        if play_game == 'YES':
            game_on = True
        else:
            game_on = False

        while game_on:

            if turn == 'Player 1':

                # Player one turn

                # show the board
                display_board(the_board)

                # choose a position
                position = player_choice(the_board, turn)

                # place the marker on the position
                place_marker(the_board, player1_marker, position)

                # check if they won
                if win_check(the_board, player1_marker):
                    display_board(the_board)
                    print("Player 1 has WON!!")
                    game_on = False

                # or check if there is a tie
                elif full_board_check(the_board):
                    display_board(the_board)
                    print("Tie Game!")
                    game_on = False

                # if no tie and no win, then next player's turn
                else:
                    turn = 'Player 2'

            else:
                # Player two turn

                # show the board
                display_board(the_board)

                # choose a position
                position = player_choice(the_board, turn)

                # place the marker on the position
                place_marker(the_board, player2_marker, position)

                # check if they won
                if win_check(the_board, player2_marker):
                    display_board(the_board)
                    print("Player 2 has WON!!")
                    game_on = False

                # or check if there is a tie
                elif full_board_check(the_board):
                    display_board(the_board)
                    print("Tie Game!")
                    game_on = False

                # if no tie and no win, then next player's turn
                else:
                    turn = 'Player 1'

        if not replay():
            break
        # Break out of the while loop on replay()
