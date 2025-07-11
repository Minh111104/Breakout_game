# Breakout Game

A classic Breakout game implemented in Python using the Turtle graphics library. Break all the blocks with your ball while keeping it from falling off the bottom of the screen!

## Features

- **Classic Breakout Gameplay**: Control a paddle to bounce a ball and destroy blocks
- **Heart System**: Start with 5 hearts - lose one each time the ball falls off screen
- **Score System**: Earn 10 points for each block destroyed
- **High Score Tracking**: Your best score is saved and persists between game sessions
- **Dynamic Ball Physics**: Ball angle changes based on where it hits the paddle
- **Start Screen**: Press SPACE to begin playing
- **Restart Option**: After game over, press SPACE to play again or ESC to quit

## How to Play

1. **Start the Game**: Run `main.py` and press SPACE to start
2. **Control the Paddle**: Use LEFT and RIGHT arrow keys to move the paddle
3. **Objective**: Destroy all blocks by bouncing the ball into them
4. **Avoid Losing Hearts**: Don't let the ball fall off the bottom of the screen
5. **Win Condition**: Clear all blocks to win the game
6. **Restart**: After game over, press SPACE to restart or ESC to quit

## Installation & Requirements

### Prerequisites

- Python 3.x
- Turtle graphics library (included with Python)

### Running the Game

1. Clone or download this repository
2. Navigate to the game directory
3. Run the main file:

   ```bash
   python main.py
   ```

## File Structure

```bash

Breakout_game/
├── main.py          # Main game loop and logic
├── paddle.py        # Paddle class and movement
├── ball.py          # Ball class and physics
├── block.py         # Block creation and management
├── scoreboard.py    # Score tracking and display
├── highscore.txt    # High score storage (created automatically)
└── README.md        # This file
```

## Game Controls

- **LEFT Arrow**: Move paddle left
- **RIGHT Arrow**: Move paddle right
- **SPACE**: Start game / Restart after game over
- **ESC**: Quit game (from restart screen)

## Game Mechanics

- **Ball Physics**: The ball bounces off walls, paddle, and blocks
- **Paddle Interaction**: Ball direction changes based on impact position on paddle
- **Block Destruction**: Each block gives 10 points when destroyed
- **Lives System**: 5 hearts total, lose one when ball falls off screen
- **High Score**: Automatically saved to `highscore.txt`

## Future Enhancements

Potential features that could be added:

- Power-ups (larger paddle, multiple balls, etc.)
- Multiple levels with different block arrangements
- Sound effects
- Different block types with varying point values
- Increasing difficulty levels

## License

This project is created for educational purpose.

---

**Enjoy playing Breakout!** 🎮
