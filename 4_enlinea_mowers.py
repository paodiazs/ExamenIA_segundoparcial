import random

class JuegoCuatro:
    def _init_(self):
        self.tablero = [[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' ']]
        self.turno = random.choice([1, 2])

        self.mostrarTablero()

    def mostrarTablero(self):
        for i, fila in enumerate(self.tablero):
            print(' ' + ' | '.join(fila))
            if i < len(self.tablero) - 1:
                print('---------------')

        if not self.checkWinner('1') and not self.checkWinner('2') and not self.checkEmpate():
            if self.turno == 1:
                self.turnoJugador()
            else:
                self.turnoMinMax()

    def turnoJugador(self):
        print("Turno Jugador")
        j = input("Ingresar la columna: ")

        if not j.isdigit() or int(j) < 0 or int(j) > 3:
            print("Columna no valida")
            self.turnoJugador()

        j = int(j)

        for i, row in enumerate(reversed(self.tablero)):
            if self.tablero[i][j] == ' ':
                self.tablero[i][j] = '1'
                self.turno = 2
                self.mostrarTablero()

    def turnoMinMax(self):
        state = float('-inf')
        best_move = None

        for j in range(4):
            for i, row in enumerate(reversed(self.tablero)):
                if self.tablero[i][j] == ' ':
                    self.tablero[i][j] = '2'
                    puntos = self.min_function()
                    self.tablero[i][j] = ' '

                    if puntos > state:
                        state = puntos
                        best_move = (i, j)

        if best_move:
            fila, columna = best_move
            self.tablero[fila][columna] = '2'
            self.turno = 1
            self.mostrarTablero()

    def min_function(self):
        if self.checkWinner('2'):
            return 1
        elif self.checkWinner('1'):
            return -1
        elif self.checkEmpate():
            return 0
        
        min_state = float('inf')

        for i, row in enumerate(self.tablero):
            for j, column in enumerate(row):
                if self.tablero[i][j] == ' ':
                    self.tablero[i][j] = '1'
                    puntos = self.max_function()
                    self.tablero[i][j] = ' '

                    min_state = min(min_state, puntos)

        return min_state
    
    def max_function(self):
        if self.checkWinner('2'):
            return 1
        elif self.checkWinner('1'):
            return -1
        elif self.checkEmpate():
            return 0
        
        max_state = float('-inf')

        for i, row in enumerate(self.tablero):
            for j, column in enumerate(row):
                if self.tablero[i][j] == ' ':
                    self.tablero[i][j] = '2'
                    puntos = self.min_function()
                    self.tablero[i][j] = ' '

                    max_state = max(max_state, puntos)

        return max_state
    
    def checkWinner(self, player):
        # Comprobación de filas
        for row in self.tablero:
            if row[0] == row[1] == row[2] == row[3] == player:
                return True

        # Comprobación de columnas
        for col in range(4):
            if self.tablero[0][col] == self.tablero[1][col] == self.tablero[2][col] == self.tablero[3][col] == player:
                return True

        # Comprobación de diagonales
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == self.tablero[3][3] == player:
            return True
        if self.tablero[0][3] == self.tablero[1][2] == self.tablero[2][1] == self.tablero[3][0] == player:
            return True

        return False

    def checkEmpate(self):
        for row in self.tablero:
            for cell in row:
                if cell == ' ':
                    return False
        return True

juego = JuegoCuatro()