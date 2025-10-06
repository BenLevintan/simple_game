# 🐌 Platformer Adventure

A lightweight 2D side-scrolling platformer game built using **Python** and **Pygame**. This project features animated characters, gravity-based jumping mechanics, dynamic enemies (snails), flying birds, collision detection, and a minimal UI displaying survival time.

---

## 🎮 Game Overview

In **Platformer Adventure**, you control a main character trying to survive by dodging moving snails while navigating across a horizontal scrolling scene. The game increases in difficulty over time as more enemies appear.

- Smooth player movement with gravity and jumping  
- Basic AI-controlled enemies and background birds  
- Sprite flipping based on movement direction  
- Collision-based game over condition  
- Pixel-style visuals and custom font support

---

## 📁 Project Structure

```
├── main.py # Main game loop
├── npcs.py # Classes for Snail, Birds, and Player (simple)
├── plater.py # Advanced Player class using sprite animations
├── utils.py # Helper functions for loading and flipping sprites
├── requirements.txt # Project dependencies
├── .venv/ # Virtual environment (excluded via .gitignore)
├── .gitignore # Ignore unnecessary files and folders
├── assets/
│ ├── background1.png
│ ├── ground1.png
│ ├── fonts/
│ │ └── Pixle_Font.ttf
│ ├── characters/
│ │ ├── birds.png
│ │ ├── snail.png
│ │ └── main3.png
│ └── MainCharacters/
│ └── MaskDude/ # Animated sprite sheets for advanced player
```

---

## 🛠️ Installation & Setup

### 1. Prerequisites

- Python **3.11.4** (or compatible version)  
- `pygame` library

### 2. Install Pygame

You can install Pygame via pip:

```bash
pip install pygame
```

### 3. Clone the Repository

```bash
git clone https://github.com/BenLevintan/simple_game.git
pip install -r requirements.txt
```

Or simply download the project folder and extract it.

### 4. Run the Game

```bash
python main.py
```

---

## 🎮 Controls

| Key         | Action     |
|-------------|------------|
| `→` (Right) | Move right |
| `←` (Left)  | Move left  |
| `↑` (Up)    | Jump       |
| `ESC`       | Exit game  |

---

## 🔧 Features

- 🎨 Pixel-based sprite graphics with flipping support  
- 🐌 Multiple enemy types (with increasing speed)  
- 🐦 Animated birds for visual depth  
- 📦 Modular design using classes  
- 💀 Game over when colliding with snails or falling off screen  
- ⏱️ Timer showing how long the player survived

---

## 📚 Code Highlights

- **Collision Detection**  
  - Snail vs Player: Game over on collision  
  - Ground collision stops fall

- **Gravity and Jumping**  
  - Physics-based jump with gravity accumulation

- **Asset Loading**  
  - Dynamic sprite loading using `utils.py`

---

## 👨‍💻 Contributors

- [Your Name Here] – Developer & Designer

---

## 🚀 Future Improvements (Optional)

- Add background music and sound effects  
- Improve player animation system integration (use `plater.py`)  
- Level progression and scoring  
- Pause/Restart functionality  
- Add power-ups and new enemy types

---

**Enjoy the game! Happy jumping! 🎉**
