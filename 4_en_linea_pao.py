    # Check vertical
    for row in range(3):
        for col in range(7):
            if board[row][col] == player and board[row+1][col] == player and board[row+2][col] == player and board[row+3][col] == player:
                return True

    # Check diagonals
    for row in range(3):
        for col in range(4):
            if board[row][col] == player and board[row+1][col+1] == player and board[row+2][col+2] == player and board[row+3][col+3] == player:
                return True
            if board[row][col+3] == player and board[row+1][col+2] == player and board[row+2][col+1] == player and board[row+3][col] == player:
                return True

    return False

#verifica que sea empate
def is_draw(board):
    return not any(0 in row for row in board)

#funcion que da el movimiento del usuario
def player_move(board):
  #mientras sea True
    while True:
        try:
            col = int(input("Select a column (0-6): "))
            if 0 <= col <= 6 and board[0][col] == 0: #ingresa un numero de columna para poner tu primer movimiento
                break
            else:
                print("Invalid move. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
  #por cada fila en orden ascendente 
    for row in range(5, -1, -1):
        if board[row][col] == 0 : # si el recuadro de la cuadricula tiene 0
            board[row][col] = 1 #cambialo a 1
            break


#funcion con el algoritmo minmax
def minmax(board, depth, is_maximizing, max_depth):
    if depth == max_depth or check_win(board, 1) or check_win(board, 2) or is_draw(board):
        if check_win(board, 2): #2 es  AI por lo tnato le damos el valor máximo de 10
            return 10
        elif check_win(board, 1): # 1 es el jugador, -10
            return -10
        else:
            return 0 # 0 es empate

    if is_maximizing:
        max_eval = float('-inf')
        for col in range(7):
            if board[0][col] == 0:
                for row in range(5, -1, -1):
                    if board[row][col] == 0:
                        board[row][col] = 2
                        eval = minmax(board, depth + 1, False, max_depth)
                        board[row][col] = 0
                        max_eval = max(max_eval, eval)
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for col in range(7):
            if board[0][col] == 0:
                for row in range(5, -1, -1):
                    if board[row][col] == 0:
                        board[row][col] = 1
                        eval = minmax(board, depth + 1, True, max_depth)
                        board[row][col] = 0
                        min_eval = min(min_eval, eval)
                        break
        return min_eval

def ai_move(board, max_depth):
    best_col = None
    for col in range(7):
        for row in range(5, -1, -1):  # Itera desde la fila 5 hasta la fila 0 en cada columna
            if board[row][col] == 0:  # Verifica si el espacio está vacío
                best_col = col
                break  # Encuentra la fila más baja disponible y sale del bucle de fila
        if best_col is not None:
            break  # Si se encontró una columna disponible, sale del bucle de columna

    return best_col


def main():
    board = np.zeros((6, 7), dtype=int)
    current_player = 1

    while True:
        display_board(board)

        if current_player == 1:
            player_move(board)
        else:
            ai_depth = 4  # Choose the depth for the AI's search
            col = ai_move(board, ai_depth)
            board[board[:, col].argmin()][col] = 2

        if check_win(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_draw(board):
            display_board(board)
            print("It's a draw!")
            break

        current_player = 3 - current_player

if __name__ == "__main__":
    main()
