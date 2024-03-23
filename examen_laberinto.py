import queue #Cola para la estructura que se usa en la búsqueda BFS
import tkinter as tk # Biblioteca para la interfaz gráfica
import time #Biblioteca que nos ayudará para la espera

"""
    La clase de Laberinto tiene un constructor el cual se llamara al principio con intencion de inicializar las variables

    cola = estructura utilizada para la búsqueda en amplitud
    canvas = utilizando tkinter se crea un lienzo 
    laberinto = lista de cadenas, generada por generador de laberintos
    visitados = lista vacía inicialmente que gaurdará los espacios visitados al recorrer el laberinto, para no repetir posiciones
    current_state = en esta variable se irá guardando la posicion
    """
class Laberinto:
    def __init__(self,laberinto,canvas):
        self.cola = queue.Queue()
        self.canvas = canvas
        self.laberinto = laberinto
        self.visitados = []
        self.current_state = None

        self.generarLaberinto()

    """
    Funcion generarLaberinto()
    Genera una cuadrícula dentro de la ventana canvas, iterando por cada fila y columna, determinamos el color de un rectangulo
    Este color se asignará de acuerdo al símbolo que tenga en su interior

    Después de la asignación, mandamos a llamar la función generarJugador()
    """
    
    def generarLaberinto(self):
        for i,row in enumerate(self.laberinto):
            for j,column in enumerate(row):
                color = 'black' if column == '#' else 'white' if column == '.' else 'green' if column == 'E' else 'red' if column == 'S' else 'black'
                self.canvas.create_rectangle(j * 20, i * 20, (j + 1) * 20, (i + 1) * 20, fill=color)

                if(color == 'green'): #El color verde representa el punto de inicio y asignamos a nuestro current state las coordenadas de ese punto
                    self.current_state = (i,j)

        self.generarJugador()

    """
    Función generarJugador()
    Dado nuestro current_state, creamos un circulo relleno color azul que simulara a nuestro jugador, inicialmente tiene las coordenadas del punto de inicio

    Posterior a ello, mandamos a llamar a nuestra función bfs que nos dará el camino solución
    E imprimimos el camino
    """
    def generarJugador(self):
        i,j = self.current_state
        global personaje_id  
        personaje_id = canvas.create_oval(j * 20 + 5, i * 20 + 5, (j + 1) * 20 - 5, (i + 1) * 20 - 5, fill='blue')
        self.canvas.update()

        camino_solucion = self.bfs_solution()
        print(camino_solucion)
        self.imprimirCamino(camino_solucion)

    """
    Función revisarOpciones
    Evalúa de los 4  movimientos posibles cuál es válido y los actualiza en la lista movimientos 

    parámetros
    estado: mandando desde BFS nos dice la posición actual en la que estemos

    Regresa un arreglo con los movimientos permitidos, es decir, los hijos o los siguientes estados
    
    """  
    #valida que las coordenadas esten dentro de los rangos permitidos y que no sean pared, representada por #

    def revisarOpciones(self,estado):
        movimientos = []
        options = {"arriba":(1,0),"abajo":(-1,0),"izquierda":(0,-1),"derecha":(0,1)}

        i,j = estado
        for movimiento,coords in options.items():
            new_i,new_j = i + coords[0],j + coords[1]

            if (0 <= new_i < len(self.laberinto) and 0 <= new_j < len(self.laberinto[0])) and laberinto[i][j] != '#': 
                movimientos.append(movimiento)

        return movimientos
                
    """
    Función bfs_solution()
    Realiza la búsqueda por amplitud utilizando una cola y una arreglo de visitados que nos permite no hacer movimiento repetidos

    options lo que hace es mapear las coordenadas con su nombre de movimiento
    Utiliza una cola en la cuál se guarda el estado actual, así como una lista de estados

    Se hace un ciclo que nos dice que mientras la cola no esté vacía
    De la cola vamos a obtener el primer elemento que llamaremos como estado y el segundo será la lista que llamaremos path
    Se añade a visitados el estado, es decir, la posicion en la que nos encontremos

    Se pregunta si la posición es igual a S, es decir el estado meta, si si lo es, regresamos el camino generado por la cola


    Regresa un arreglo de coordenadas en las que se debe de mover el jugador para llegar a la salida, si no lo encuentra, retorna -1

    """
    def bfs_solution(self):        
        options = {"arriba":(1,0),"abajo":(-1,0),"izquierda":(0,-1),"derecha":(0,1)}
        self.cola.put((self.current_state,[self.current_state]))

        while not self.cola.empty():
            estado,path = self.cola.get()
            self.visitados.append(estado)
            i,j = estado

            
            if(self.laberinto[i][j] == 'S'):
                return path
            
            for movimiento in self.revisarOpciones(estado):
                new_state = i + options[movimiento][0],j + options[movimiento][1]
                if new_state not in self.visitados:
                    self.cola.put((new_state,path + [new_state]))

        return -1
    """
    Función imprimirCamino
    Esta función imprime el arreglo de coordenadas devuelto por nuestra función bfs, convirtiendo las coordenadas de acuerdo a la configuración de nuestro canvas
    Utilizando un canvas update para actualziar el contenido de la ventana y con un time.sleep de 0.2 para una mejor visualización

    Parámetros
    self, camino_solcuion = es el arreglo de coordenadas regresado por nuestra función BFS

    """
    def imprimirCamino(self,camino_solucion):
        global personaje_id
        num_of_movs = 0
        for movimiento in camino_solucion:
            i,j = movimiento[0],movimiento[1]
            self.canvas.coords(personaje_id, j * 20 + 5, i * 20 + 5, (j + 1) * 20 - 5, (i + 1) * 20 - 5)
            self.canvas.update()
            num_of_movs += 1 #longitud del camino
            time.sleep(.2)

        print("La longitud del camino es: ",num_of_movs)

"""
E: Entrada

S: Salida

"." (punto) : Camino transitable

"#" (gato, hashtag): Muros o paredes
"""    


laberinto = [
    "##################################################",
    "E............####################.........########",
    "#####.#####.#######......#####....#######....#####",
    "#####.......#.......#####.#######.........########",
    "########.################.###########.############",
    "########.################.............############",
    "##.....#........#########.###########.############",
    "######...######.#########........####.........####",
    "########.######.#########.######.############.####",
    "#####....######......####.######.####......##.####",
    "#####.##.###########......######......#######...S#",
    "##################################################"
]

#Creamos la ventana principal
#Le asignamos un título a la venta
#De acuerdo a las longitudes de las filas y columnas del laberinto se crea el canvas
#Guardamos el lienzo dentro de la ventaana
#Creamos una instancia del Laberinto y la asignamos a main, pasando como parámetros el laberinto generado y el canvas creado
#Inicializamos

ventana = tk.Tk()
ventana.title("Laberinto con BFS | Examen IA | Segundo Parcial")
canvas = tk.Canvas(ventana, width=len(laberinto[0]) * 20, height=len(laberinto) * 20)
canvas.pack()

main = Laberinto(laberinto,canvas)


ventana.mainloop()

