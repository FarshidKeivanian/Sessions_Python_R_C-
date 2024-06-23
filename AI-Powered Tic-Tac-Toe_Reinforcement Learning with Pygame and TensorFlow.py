# pip install pygame numpy tensorflow

import sys
import random
import numpy as np
import pygame
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 300, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tic-Tac-Toe')

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Game variables
board = [0] * 9  # Represents a 3x3 grid
game_over = False
player_turn = True  # True if player's turn, False for AI

# Neural Network for the AI Player
model = Sequential()
model.add(Dense(64, input_dim=9, activation='relu'))  # Input layer for 9 board positions
model.add(Dense(64, activation='relu'))  # Hidden layer
model.add(Dense(9, activation='linear'))  # Output layer for each move's Q-value
model.compile(loss='mse', optimizer=Adam())

def draw_board():
    screen.fill(white)
    for i in range(1, 3):
        pygame.draw.line(screen, black, (0, 100 * i), (300, 100 * i), 3)
        pygame.draw.line(screen, black, (100 * i, 0), (100 * i, 300), 3)

    for index, value in enumerate(board):
        x = (index % 3) * 100 + 50
        y = (index // 3) * 100 + 50
        if value == 1:
            pygame.draw.line(screen, black, (x - 25, y - 25), (x + 25, y + 25), 2)
            pygame.draw.line(screen, black, (x + 25, y - 25), (x - 25, y + 25), 2)
        elif value == -1:
            pygame.draw.circle(screen, black, (x, y), 34, 2)

def check_win():
    # Define win positions as horizontal, vertical, and diagonal indices
    win_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
        (0, 4, 8), (2, 4, 6)  # Diagonal
    ]
    for a, b, c in win_positions:
        if board[a] == board[b] == board[c] != 0:
            return board[a]
    if 0 not in board:
        return 'Draw'  # If no empty spaces and no winner
    return None

def best_move():
    empty_cells = [i for i in range(9) if board[i] == 0]
    if not empty_cells:
        return None
    move = random.choice(empty_cells)  # Random move for simplicity
    return move

# Main game loop
while not game_over:
    draw_board()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and player_turn:
            x, y = pygame.mouse.get_pos()
            index = (x // 100) + (y // 100) * 3
            if board[index] == 0:
                board[index] = 1  # Player's move
                if check_win() is not None:
                    game_over = True
                player_turn = False

    if not player_turn and not game_over:
        ai_move = best_move()
        if ai_move is not None:
            board[ai_move] = -1  # AI's move
            if check_win() is not None:
                game_over = True
        player_turn = True

    pygame.display.flip()

if game_over:
    print("Game Over. Result:", check_win())
    pygame.time.wait(2000)  # Delay to see the final board
    pygame.quit()
    sys.exit()
