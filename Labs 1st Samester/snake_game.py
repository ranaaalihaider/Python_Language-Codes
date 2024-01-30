import random
import os
import time

# Set up the screen size
WIDTH = 20
HEIGHT = 20

# Define symbols
EMPTY = '.'
SNAKE_BODY = 'O'
FOOD = '*'

# Define directions
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

# Function to display the game board
def display_board(board, score):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console screen
    print('Snake Game')
    print('Score:', score)
    for row in board:
        print(' '.join(row))

# Function to initialize the game board
def initialize_board():
    board = [[EMPTY] * WIDTH for _ in range(HEIGHT)]
    board[HEIGHT // 2][WIDTH // 2] = SNAKE_BODY  # Snake's initial position
    return board

# Function to generate food on the board
def generate_food(board):
    while True:
        x = random.randint(0, WIDTH - 1)
        y = random.randint(0, HEIGHT - 1)
        if board[y][x] == EMPTY:
            board[y][x] = FOOD
            break

# Main function to run the game
def main():
    board = initialize_board()
    snake = [(HEIGHT // 2, WIDTH // 2)]
    direction = RIGHT
    score = 0

    generate_food(board)
    display_board(board, score)

    while True:
        # Move the snake
        head = snake[0]
        y, x = head
        if direction == UP:
            y -= 1
        elif direction == DOWN:
            y += 1
        elif direction == LEFT:
            x -= 1
        elif direction == RIGHT:
            x += 1

        # Check for collisions
        if y < 0 or y >= HEIGHT or x < 0 or x >= WIDTH or board[y][x] == SNAKE_BODY:
            print('Game Over!')
            print('Your score:', score)
            break

        # Check for food
        if board[y][x] == FOOD:
            score += 1
            generate_food(board)
        else:
            tail = snake.pop()
            ty, tx = tail
            board[ty][tx] = EMPTY

        # Update snake's position
        snake.insert(0, (y, x))
        board[y][x] = SNAKE_BODY

        # Display board
        display_board(board, score)

        # Pause for a moment
        time.sleep(0.1)

        # Get user input
        try:
            direction = input("Enter direction (up/down/left/right): ").lower()
            if direction not in [UP, DOWN, LEFT, RIGHT]:
                direction = RIGHT  # default to right if invalid input
        except KeyboardInterrupt:
            print('\nGame Over!')
            print('Your score:', score)
            break

if __name__ == "__main__":
    main()
