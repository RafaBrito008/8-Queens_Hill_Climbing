import tkinter as tk
from tkinter import Button, Label, Frame
import random
from tkinter import messagebox

DIMENSION = 8  # Dimensiones del tablero (8x8)
SIZE = 50  # Tamaño de cada casilla en píxeles

class Chessboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("8 Reinas")
        
        self.board = [[None for _ in range(DIMENSION)] for _ in range(DIMENSION)]
        self.queens = []
        
        # Crear el canvas para dibujar el tablero y las reinas
        self.canvas = tk.Canvas(self, width=SIZE*DIMENSION, height=SIZE*DIMENSION)
        self.canvas.pack(pady=20)
        
        self.control_frame = Frame(self)
        self.control_frame.pack(pady=10)
        
        # Botón para mezclar las reinas
        self.shuffle_button = Button(self.control_frame, text="Mezclar", command=self.place_queens_randomly)
        self.shuffle_button.grid(row=0, column=0, padx=10)
        
        # Botón para aplicar Hill Climbing Estocástico
        self.next_step_button = Button(self.control_frame, text="Siguiente", command=self.hill_climbing_step)
        self.next_step_button.grid(row=0, column=1, padx=10)
        
        self.conflict_label = Label(self.control_frame, text="Conflictos: 0", font=("Arial", 12))
        self.conflict_label.grid(row=0, column=2, padx=20)
        
        self.draw_board()
        self.place_queens_randomly()

    def update_conflict_label(self):
        positions = [int(self.canvas.coords(queen)[1] / SIZE - 0.5) for queen in self.queens]
        conflicts = self.count_conflicts(positions)
        self.conflict_label.config(text=f"Conflictos: {conflicts}")

    def draw_board(self):
        for row in range(DIMENSION):
            for col in range(DIMENSION):
                x1, y1 = col * SIZE, row * SIZE
                x2, y2 = x1 + SIZE, y1 + SIZE
                
                color = "white" if (row + col) % 2 == 0 else "black"
                
                self.board[row][col] = self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

    def place_queens_randomly(self):
        # Eliminar las reinas actuales
        for queen in self.queens:
            self.canvas.delete(queen)
        
        self.queens.clear()
        
        positions = list(range(DIMENSION))
        random.shuffle(positions)

        for col, row in enumerate(positions):
            self.place_queen(row, col)
        self.update_conflict_label()

    def place_queen(self, row, col):
        x, y = (col + 0.5) * SIZE, (row + 0.5) * SIZE
        queen = self.canvas.create_text(x, y, text="♛", font=("Arial", int(SIZE/1.5)), fill="red")
        self.queens.append(queen)

    def count_conflicts(self, positions):
        # Cuenta los conflictos entre reinas basado en sus posiciones
        conflicts = 0
        for i in range(DIMENSION):
            for j in range(i+1, DIMENSION):
                if j >= len(positions):  # Añade esta línea
                    continue
                if positions[i] == positions[j]:
                    conflicts += 1
                if abs(positions[i] - positions[j]) == abs(i - j):
                    conflicts += 1
        return conflicts

    def get_neighbors(self, positions):
        # Devuelve todos los vecinos posibles (movimientos de una reina a otra fila)
        neighbors = []
        for col in range(DIMENSION):
            for row in range(DIMENSION):
                if row != positions[col]:
                    new_positions = positions.copy()
                    new_positions[col] = row
                    neighbors.append(new_positions)
        return neighbors

    def hill_climbing_step(self):
        # Aplica un paso del algoritmo Hill Climbing Estocástico
        positions = [int(self.canvas.coords(queen)[1] / SIZE - 0.5) for queen in self.queens]
        
        neighbors = self.get_neighbors(positions)
        current_conflicts = self.count_conflicts(positions)

        # Verificar si hemos encontrado una solución
        if current_conflicts == 0:
            messagebox.showinfo("¡Éxito!", "El tablero está resuelto")
            return
            
        # Evaluar todos los vecinos y guardar aquellos que mejoren el estado actual
        better_neighbors = []
        for neighbor in neighbors:
            if self.count_conflicts(neighbor) < current_conflicts:
                better_neighbors.append(neighbor)

        # Si no hay vecinos mejores, hemos encontrado una solución o un óptimo local
        if not better_neighbors:
            print("Optimo local alcanzado. Reintentando...")
            self.place_queens_randomly()
            return

        # Seleccionar aleatoriamente uno de los vecinos mejores
        next_positions = random.choice(better_neighbors)
        
        # Actualizar el tablero
        for queen in self.queens:
            self.canvas.delete(queen)
        self.queens.clear()
        for col, row in enumerate(next_positions):
            self.place_queen(row, col)

            self.update_conflict_label()


if __name__ == "__main__":
    app = Chessboard()
    app.mainloop()