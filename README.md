# 🐍🎮 SnakeByte-Game

Welcome to **SnakeByte**, a fun and interactive remake of the classic Snake Game, built using Python’s `turtle` graphics module!

The player controls the snake that moves continuously around a square arena, consuming randomly generated food items to grow in length. With each piece of food eaten, the snake increases in size and the player's score goes up. The challenge intensifies as the snake becomes longer, increasing the risk of collisions with its own tail or the boundaries of the game area.

The game uses precise distance-based detection to determine whether the snake eats the food or collides with a wall or itself. If the snake’s head comes close enough to the food, it registers as “eaten” and a new segment is added to the snake. If the snake's head crosses the visible boundary (`±280` on either axis) or touches any part of its own tail, the game ends instantly.

Together, these components create a complete and responsive gameplay experience using only Python’s built-in libraries. The entire game is structured with clean, modular, object-oriented design patterns. It features real-time input handling, collision detection, animated graphics, and a dynamic score display—delivered through the powerful yet simple `turtle` module.

---

## 🌟 Development Milestones

This game was built using object-oriented Python, incrementally adding core features in stages:

| Step | Feature                              | Status |
|------|--------------------------------------|--------|
| 1    | Create the snake body                | ✅     |
| 2    | Move the snake with keyboard events  | ✅     |
| 3    | Generate random food on screen       | ✅     |
| 4    | Detect collision with food           | ✅     |
| 5    | Add scoreboard                       | ✅     |
| 6    | Detect collision with wall           | ✅     |
| 7    | Detect collision with snake tail     | ✅     |

---

## 🖼️ Visual Output

Below are sample outputs from this program:

<img width="400" alt="Screenshot 2025-07-08 at 23 57 57" src="https://github.com/user-attachments/assets/ab27feb3-6a67-4708-a7cb-71cbad6cc235" />

---

## 🚀 Gameplay Overview

- 🎮 Arrow key controls: Up, Down, Left, Right  
- 🍎 Randomly spawned food with custom sprite  
- 🧠 Intelligent collision handling  
- 💯 Score tracking  
- 💥 Game over when snake hits wall or itself  

---

## 🐍 Snake Class

The `Snake` class defines the snake's appearance, movement, and growth behavior.

### 🔹 Attributes

- `snake_color`: Defines the visual color of the snake.
- `snake_shape`: Uses a custom `.gif` sprite to represent each segment.
- `segment`: A list holding each turtle segment that forms the body.
- `head`: A reference to the first segment of the snake, used for direction and collision checks.

### 🔹 Core Methods (Snake Behavior)

- `__init__()`: Initializes the snake with three segments and sets the head.
- `create_snake()`: Adds the initial segments at predefined start positions.
- `add_segment(position)`: Adds a new segment (square) at a specific position.
- `extend_segment()`: Appends a new segment to the tail when the snake eats food.
---

### 🎮 Movement Control Methods (Triggered by Key Events)

- `move_snake()`: Moves the snake forward by updating each segment's position in order.
- `move_up()`: Changes direction to "up" if not already moving "down".
- `move_down()`: Changes direction to "down" if not already moving "up".
- `move_left()`: Changes direction to "left" if not already moving "right".
- `move_right()` : Changes direction to "right" if not already moving "left".
---

## 🍎 Food Class

The `Food` class is responsible for displaying a food item on the screen:

- Displays a custom food image
- Automatically refreshes when eaten by the snake
- Food is randomly placed on the screen using random `x` and `y` coordinates.
- The snake "eats" the food when its head comes close enough, using:
  <br><br>
  ```python
  if snake.head.distance(food) < 15:

---

## 🧱 Wall Collision Detection

- The screen has visible borders: <code>x = ±280</code>, <code>y = ±280</code>.
- If the snake's head crosses these limits:
  <br><br>
  ```python
  if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
---

## 🌀 Tail Collision Detection

- As the snake grows, the risk of self-collision increases. Each frame, the game checks whether the head is too close to any of its own segments except the head itself. A distance less than 10 units triggers a Game Over:
  <br><br>
  ```python
  for segment in snake.segments[1:]:
    if head.distance(segment) < 10:
---

## 💯 Scoreboard

A `Scoreboard` in the top corner tracks how many food items have been eaten. Every time food is consumed, the score increases by 1. If a collision with a wall or tail occurs, the game stops and displays a “Game Over” message to user.

- Increments score on each food collision
- Shows a “Game Over” message if the snake hits the wall or itself

---

## 📁 Project Structure

```text
📁 SnakeByte-game/
│
├── main.py           # Main game loop and controls
├── snake.py          # Snake class logic
├── food.py           # Food class logic
├── scoreboard.py     # Score and game over logic
├── square.gif        # Custom snake body sprite
└── snake_food.gif    # Custom food sprite
└── background.gif    # Custom background
