import tkinter as tk
from tkinter import ttk
import random
import pandas as pd
from datetime import datetime

class FirstDownTheMountain:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("First Down the Mountain Simulator")
        self.root.geometry("800x600")
        
        self.track_length = 10  # Length of the mountain track for each climber
        self.climbers = {i: 0 for i in range(2, 13)}  # Positions 2-12, all start at the top
        self.wins = {i: 0 for i in range(2, 13)}      # Tracks wins for each climber
        self.setup_gui()
    
    def setup_gui(self):
        # Simulation controls
        control_frame = tk.Frame(self.root)
        control_frame.pack(pady=10)
        
        tk.Label(control_frame, text="Number of games to simulate:").grid(row=0, column=0)
        self.num_games_entry = ttk.Entry(control_frame, width=10)
        self.num_games_entry.insert(0, "100")  # Default to 100 games
        self.num_games_entry.grid(row=0, column=1, padx=5)
        
        self.start_button = ttk.Button(control_frame, text="Start Simulation", command=self.start_simulation)
        self.start_button.grid(row=0, column=2, padx=5)
        
        # Display for each climber’s progress down the mountain
        self.track_frame = tk.Frame(self.root)
        self.track_frame.pack(pady=10)
        
        tk.Label(self.track_frame, text="Climbers' Progress:").pack()
        
        # Track display organized by climbers
        self.track_labels = {}
        for i in range(2, 13):
            label_text = self.get_track_display(i)
            label = tk.Label(self.track_frame, text=label_text, font=("Arial", 10))
            label.pack(anchor="w")
            self.track_labels[i] = label
        
        # Status label for displaying winner
        self.status_label = tk.Label(self.root, text="Click 'Start Simulation' to begin.")
        self.status_label.pack(pady=10)
    
    def roll_dice(self):
        """Roll two dice and return their sum."""
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        return die1 + die2
    
    def get_track_display(self, climber):
        """Generate a string representation of the track for a given climber."""
        position = self.climbers[climber]
        track = ["." for _ in range(self.track_length)]
        track[position] = str(climber)  # Mark the climber's position on the track
        return f"Climber {climber}: " + " ".join(track)
    
    def update_track_display(self):
        """Update the track display for each climber."""
        for i in range(2, 13):
            label_text = self.get_track_display(i)
            self.track_labels[i].config(text=label_text)
    
    def simulate_single_game(self):
        """Simulate a single game and determine the winning climber."""
        # Reset climbers' positions to start at the top
        self.climbers = {i: 0 for i in range(2, 13)}
        
        # Run the game until one climber reaches the end of the track
        while True:
            roll_sum = self.roll_dice()
            self.climbers[roll_sum] += 1
            
            # Update track display for each climber
            self.update_track_display()
            
            # Check if this climber has won
            if self.climbers[roll_sum] >= self.track_length:
                self.wins[roll_sum] += 1
                return roll_sum
    
    def start_simulation(self):
        """Start the simulation for the specified number of games."""
        num_games = int(self.num_games_entry.get())
        
        # Run the simulation for the specified number of games
        for _ in range(num_games):
            winner = self.simulate_single_game()
            self.status_label.config(text=f"Climber {winner} won this game!")
        
        # Save the results to a spreadsheet
        self.save_to_spreadsheet()
        self.status_label.config(text="Simulation complete! Results saved to Excel.")
    
    def save_to_spreadsheet(self):
        """Save the simulation results to an Excel spreadsheet."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"first_down_the_mountain_results_{timestamp}.xlsx"
        
        # Create a DataFrame to hold the results
        results_data = {
            "Climber": list(self.wins.keys()),
            "Wins": list(self.wins.values())
        }
        df = pd.DataFrame(results_data)
        
        # Save to Excel
        with pd.ExcelWriter(filename) as writer:
            df.to_excel(writer, sheet_name="Results", index=False)
        
        print(f"Results saved to {filename}")
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = FirstDownTheMountain()
    game.run()
