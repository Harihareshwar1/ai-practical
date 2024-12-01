import random

# Basic game setup
size = 4
grid = [['' for _ in range(size)] for _ in range(size)]

# Randomly place gold, Wumpus, and pit
gold_pos = (random.randint(0, size-1), random.randint(0, size-1))
wumpus_pos = (random.randint(0, size-1), random.randint(0, size-1))
pit_pos = (random.randint(0, size-1), random.randint(0, size-1))

# Start agent at (0,0)
agent_pos = (0, 0)
has_gold = False

def display_grid():
    print("\nGrid:")
    for i in range(size):
        for j in range(size):
            if (i, j) == agent_pos:
                print("A", end=" ")
            elif (i, j) == gold_pos:
                print("G", end=" ")
            elif (i, j) == wumpus_pos:
                print("W", end=" ")
            elif (i, j) == pit_pos:
                print("P", end=" ")
            else:
                print(".", end=" ")
        print()

def move_agent(direction):
    global agent_pos
    x, y = agent_pos
    if direction == "up" and x > 0:
        agent_pos = (x-1, y)
    elif direction == "down" and x < size - 1:
        agent_pos = (x+1, y)
    elif direction == "left" and y > 0:
        agent_pos = (x, y-1)
    elif direction == "right" and y < size - 1:
        agent_pos = (x, y+1)

def check_game_status():
    if agent_pos == wumpus_pos:
        print("You were eaten by the Wumpus! Game Over.")
        return True
    elif agent_pos == pit_pos:
        print("You fell into a pit! Game Over.")
        return True
    elif agent_pos == gold_pos:
        print("You found the gold! You Win!")
        return True
    return False

# Game loop
def play_game():
    global has_gold
    display_grid()
    
    while True:
        action = input("Enter action (up, down, left, right): ").strip().lower()
        move_agent(action)
        display_grid()
        
        if check_game_status():
            break

play_game()