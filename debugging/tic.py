#!/usr/bin/python3

def print_board(board):
    """
    Print the current state of the board.
    
    Parameters:
    board (list of list of str): The 3x3 board with 'X', 'O', or ' '.
    
    Returns:
    None
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Check if there's a winner on the board.
    
    Parameters:
    board (list of list of str): The 3x3 board with 'X', 'O', or ' '.
    
    Returns:
    bool: True if there's a winner, False otherwise.
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_draw(board):
    """
    Check if the board is full and there's no winner, indicating a draw.
    
    Parameters:
    board (list of list of str): The 3x3 board with 'X', 'O', or ' '.
    
    Returns:
    bool: True if the game is a draw, False otherwise.
    """
    for row in board:
        if " " in row:
            return False
    return not check_winner(board)

def tic_tac_toe():
    """
    Main function to run the Tic-Tac-Toe game.
    
    Parameters:
    None
    
    Returns:
    None
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while True:
        print_board(board)
        
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
            
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid input. Please enter row and column as 0, 1, or 2.")
                continue

            if board[row][col] == " ":
                board[row][col] = player
                
                if check_winner(board):
                    print_board(board)
                    print(f"Player {player} wins!")
                    break

                if is_draw(board):
                    print_board(board)
                    print("The game is a draw!")
                    break
                
                # Switch player
                player = "O" if player == "X" else "X"
            else:
                print("That spot is already taken! Try again.")
        
        except ValueError:
            print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    tic_tac_toe()
