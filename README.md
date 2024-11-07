# Math Game Simulator Suite

This repository contains Python-based simulations for three interactive math games, built to support learning and analysis for a math assessment. The games include **Dice Differences**, **First Down the Mountain**, and **Hexagon Game Simulator**, each featuring a unique gameplay mechanic that reinforces probability and strategic thinking concepts.

## Game Overview
### 1. Dice Differences
- **Description**: A game where players use counters to match dice roll differences. The simulation calculates the number of moves required to clear all counters and outputs data for analysis.
- **Features**:
  - GUI interface for inputting counter strategies.
  - Automatic gameplay simulation with visual output.
  - Results export to an Excel spreadsheet.

### 2. First Down the Mountain
- **Description**: Players place climbers at positions 2-12, rolling dice to move them down a mountain track. The goal is to see which climber reaches the bottom first.
- **Features**:
  - Visual representation of climber progress on a numbered track.
  - Automated simulation of games with results displayed in the GUI.
  - Win counts saved to an Excel file for further analysis.

### 3. Hexagon Game Simulator
- **Description**: A game set on a hexagonal board where a player moves toward a randomly selected goal. The player progresses automatically, displaying their path on the board.
- **Features**:
  - Hexagonal board layout in a Tkinter-based GUI.
  - Automatic gameplay with real-time position updates.
  - Notification upon reaching the goal.

## Prerequisites
Ensure the following are installed:
- Python 3.7+
- Tkinter (standard with most Python installations)
- Pandas (optional, for data export functionality)

## Installation
1. Clone this repository to your local machine:
   ```bash
   git clone [https://github.com/yourusername/math-game-simulator-suite.git](https://github.com/Hamish-Leahy/Dice-Differences/tree/main)
   cd math-game-simulator-suite
   ```
2. Install required dependencies:
   ```bash
   pip install pandas
   ```

## Usage
### Dice Differences
1. Run the `dice_differences.py` file:
   ```bash
   python dice_differences.py
   ```
2. Enter your counter strategy and number of games to simulate.
3. View the results in the GUI and save them to an Excel file.

### First Down the Mountain
1. Run the `first_down_the_mountain.py` file:
   ```bash
   python first_down_the_mountain.py
   ```
2. Enter the number of games to simulate and watch the climbers progress down the mountain.
3. Check the results saved in the generated Excel file.

### Hexagon Game Simulator
1. Run the `hexagon.py` file:
   ```bash
   python hexagon.py
   ```
2. Observe the player's movement on the hexagonal board toward the goal.
3. A message box will notify you when the player reaches the goal.

## Educational Relevance
These games serve as tools for understanding mathematical concepts such as:
- **Probability and Chance**: Simulate dice rolls and analyze results.
- **Strategic Decision-Making**: Choose strategies in Dice Differences to minimize moves.
- **Pathfinding and Movement**: Observe movement on a hexagonal grid and learn about efficient pathways.

## Customization
- **Adjust Game Settings**: Modify variables such as the number of counters, track lengths, and board size in the code.
- **Move Speed**: Change the delay between moves in the simulation to make gameplay faster or slower.

## Future Enhancements
- **Additional Metrics**: Add detailed statistical analysis to each game's results.
- **Obstacle Placement**: Introduce obstacles in the Hexagon Game Simulator for increased complexity.
- **Interactive User Input**: Allow users to customize starting positions and goal locations.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributions
Contributions are welcome! Submit a pull request or open an issue if you have ideas for improvements or bug fixes.

## Contact
For any questions or feedback, reach out to hamish@hamishleahy.com or create an issue in this repository.

