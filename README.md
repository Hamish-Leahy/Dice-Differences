# Hexagon Game Simulator

This repository contains the **Hexagon Game Simulator**, a Python-based simulation game that showcases an automated gameplay experience on a hexagonal grid. The program features a GUI built using Tkinter, where a player moves automatically on a hexagonal board toward a randomly assigned goal. The game visually represents the player's progress on the board and highlights the winning condition.

## Features
- **Hexagonal Grid Layout**: The game board is represented as a hexagonal grid, displaying each cell as a labeled box.
- **Automatic Gameplay**: The player moves automatically toward the goal based on the shortest path.
- **GUI Display**: Real-time updates to the board show the player's path and current position, making gameplay easy to follow.
- **Win Notification**: A message box displays when the player reaches the goal.
- **Customizable Board Size**: The board size can be adjusted by modifying the `board_size` variable.

## Prerequisites
Ensure you have the following installed:
- Python 3.7+
- Tkinter (included with most Python installations)
- Pandas (for future data export functionality)

## Installation
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/hexagon-game-simulator.git
   cd hexagon-game-simulator
   ```
2. Install required dependencies (optional for Pandas):
   ```bash
   pip install pandas
   ```

## Usage
1. Run the `hexagon.py` file to start the game:
   ```bash
   python hexagon.py
   ```
2. The game window will open, and the player will begin moving on the hexagonal grid.
3. Watch the progress as the player moves automatically toward the goal. The board updates dynamically, showing the player's trail and current position.
4. A message box will notify you when the player reaches the goal.

## How It Works
- **Hexagonal Board Creation**: The board is constructed using Tkinter labels arranged in a staggered grid layout to create a hexagonal shape.
- **Player Movement**: The player starts at the center of the board and moves step-by-step toward the randomly generated goal. The movement direction is determined to minimize the distance to the goal.
- **Real-Time Updates**: The game updates the GUI after each move, displaying the player's path (".") and current position ("P").
- **Win Condition**: The simulation stops, and a message box is shown when the player reaches the goal.

## Customization
- **Board Size**: Modify the `board_size` variable in the `HexGameSimulator` class to change the board size.
- **Move Speed**: Adjust the delay between moves by modifying the `self.root.after()` method's delay value (e.g., 500 ms).

## Future Enhancements
- **Export Results**: Implement data export to track simulation results in a CSV or Excel format.
- **Custom Starting Positions**: Allow users to set custom starting points for the player.
- **Obstacle Placement**: Add functionality for placing obstacles on the board to create more complex paths.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributions
Contributions are welcome! Feel free to submit a pull request or open an issue if you have ideas for improvements or bug fixes.

## Contact
For any questions or feedback, please reach out to [yourname@example.com] or create an issue in this repository.
