import tkinter as tk
import random

class HexGameSimulator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Hexagon Game Simulator")
        self.root.geometry("600x600")
        
        self.board_size = 5  # Size of the hexagonal grid (5x5 in this example)
        self.create_hex_board()
        self.simulate_game()
    
    def create_hex_board(self):
        """Creates a hexagonal board layout using a grid of labels."""
        self.cells = {}  # Dictionary to hold cell references
        for row in range(self.board_size):
            # Calculate column offset for hexagonal layout
            offset = abs((self.board_size // 2) - row)
            for col in range(self.board_size - offset):
                actual_col = col + offset  # Adjust column position for hexagonal shape
                cell_label = tk.Label(self.root, text=" ", width=4, height=2, borderwidth=1, relief="solid")
                cell_label.grid(row=row, column=actual_col, padx=5, pady=5)
                self.cells[(row, actual_col)] = cell_label  # Store cell reference for updates
    
    def simulate_game(self):
        """Automatically simulates gameplay on the hexagonal board."""
        player_positions = [(self.board_size // 2, self.board_size // 2)]  # Start in the center
        goal_position = (random.randint(0, self.board_size-1), random.randint(0, self.board_size-1))  # Random goal
        
        # Highlight the goal position on the board
        goal_label = self.cells[goal_position]
        goal_label.config(bg="yellow", text="Goal")
        
        def make_move():
            """Move the player towards the goal automatically."""
            current_position = player_positions[-1]
            row, col = current_position
            
            # Calculate next position by moving toward the goal
            if row < goal_position[0]: row += 1
            elif row > goal_position[0]: row -= 1
            if col < goal_position[1]: col += 1
            elif col > goal_position[1]: col -= 1
            
            # Update player position
            player_positions.append((row, col))
            self.update_board_display(player_positions)
            
            # Check for win condition
            if (row, col) == goal_position:
                self.root.after(1000, lambda: tk.messagebox.showinfo("Game Over", "Player reached the goal!"))
            else:
                self.root.after(500, make_move)  # Continue moving every 500ms
        
        make_move()
    
    def update_board_display(self, positions):
        """Updates the GUI to show player position on the hex board."""
        # Reset all cells first
        for cell in self.cells.values():
            cell.config(bg="white", text=" ")
        
        # Update player trail positions
        for pos in positions[:-1]:
            if pos in self.cells:
                self.cells[pos].config(bg="lightblue", text=".")
        
        # Update current player position
        current_position = positions[-1]
        if current_position in self.cells:
            self.cells[current_position].config(bg="blue", text="P")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = HexGameSimulator()
    game.run()
