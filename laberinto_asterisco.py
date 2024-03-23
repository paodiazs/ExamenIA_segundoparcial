import heapq
import tkinter as tk
import time
import math


class Laberinto:

    def __init__(self,laberinto,canvas):
        self.cola = []
        self.canvas = canvas
        self.laberinto = laberinto
        self.visitados = []
        self.current_state = None
        self.goal_state = None

        self.generarLaberinto()

    
    def generarLaberinto(self):
        for i,row in enumerate(self.laberinto):
            for j,column in enumerate(row):
                color = 'black' if column == '#' else 'white' if column == '.' else 'green' if column == 'E' else 'red' if column == 'S' else 'black'
                self.canvas.create_rectangle(j * 20, i * 20, (j + 1) * 20, (i + 1) * 20, fill=color)

                if(color == 'green'):
                    self.current_state = (i,j)
                elif(color == 'red'):
                    self.goal_state = (i,j)

        self.generarJugador()

        
    def generarJugador(self):
        i,j = self.current_state
        global personaje_id  
        personaje_id = canvas.create_oval(j * 20 + 5, i * 20 + 5, (j + 1) * 20 - 5, (i + 1) * 20 - 5, fill='blue')
        self.canvas.update()

        camino_solucion = self.asterisco_funcion()

        print(camino_solucion)
        self.imprimirCamino(camino_solucion)


    def imprimirCamino(self,camino_solucion):
        global personaje_id
        num_of_movs = 0
        for movimiento in camino_solucion:
            i,j = movimiento[0],movimiento[1]
            self.canvas.coords(personaje_id, j * 20 + 5, i * 20 + 5, (j + 1) * 20 - 5, (i + 1) * 20 - 5)
            self.canvas.update()
            num_of_movs += 1
            time.sleep(.2)

        print(num_of_movs)

        
    def revisarOpciones(self,estado):
        movimientos = []
        options = {"arriba":(1,0),"abajo":(-1,0),"izquierda":(0,-1),"derecha":(0,1)}

        i,j = estado
        for movimiento,coords in options.items():
            new_i,new_j = i + coords[0],j + coords[1]

            if (0 <= new_i < len(self.laberinto) and 0 <= new_j < len(self.laberinto[0])) and laberinto[i][j] != '#':
                movimientos.append(movimiento)

        return movimientos
    
    def euristicaFunction(self,state):
        return math.sqrt((state[0] - self.goal_state[0]) ** 2 + (state[1] - self.goal_state[1]) ** 2)
                

    def asterisco_funcion(self):
        options = {"arriba":(1,0),"abajo":(-1,0),"izquierda":(0,-1),"derecha":(0,1)}
        self.cola.append((0 + self.euristicaFunction(self.current_state), 0, self.current_state,[self.current_state]))

        while self.cola:
            dist,cost,estado,path = heapq.heappop(self.cola)
            self.visitados.append(estado)

            i, j = estado
            
            if self.laberinto[i][j] == 'S':
                return path
            
            for movimiento in self.revisarOpciones(estado):
                new_state = i + options[movimiento][0], j + options[movimiento][1]
                if new_state not in self.visitados:
                    new_cost = cost + 1
                    priority = new_cost + self.euristicaFunction(new_state)
                    heapq.heappush(self.cola, (priority, new_cost, new_state, path + [new_state]))

        return -1

        


laberinto = [
    "##################################################",
    "E............####################.........########",
    "#####.#####.#######...............#######....#####",
    "#####...............#####.#######.........########",
    "########.################.###########.############",
    "########.################.............############",
    "##.....#........#########.###########.############",
    "######...######.#########........####.........####",
    "########.######.#########.######.############.####",
    "#####....######......####.######.####.........####",
    "#####.##.###########......######......#######...S#",
    "##################################################"
]

ventana = tk.Tk()
ventana.title("Laberinto Examen | Recorrido por A* ")
canvas = tk.Canvas(ventana, width=len(laberinto[0]) * 20, height=len(laberinto) * 20)
canvas.pack()

main = Laberinto(laberinto,canvas)


ventana.mainloop()