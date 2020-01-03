# ==================================================================
# MADE BY JACK HE
# Dec. 29th, 2019
# ==================================================================


import pygame
from random import randint
# initialize pygame
pygame.init()
run = True
# create screen
# Game loop

# exist is one of: TRUST THE RECIPE !!!
    # - None: meaning there is no square on screen (impossible as of right now)
    # - (Int, Int): a tuple representing x, y coordinate of the square on the screen
exist = [0, 0]

SIZE = (15, 15)

# speed is Int
# interp. as how fast the square moves across the screen
SPEED = SIZE[0]

WIDTH = 800
HEIGHT = 600
COLOR = (0, 0, 0)

foodX = WIDTH // 2 # will be randomized
foodY = HEIGHT // 2 # will be randomized
FOOD_COLOR = (255, 255, 255) # will be randomized
FOOD_SIZE = (25, 25)
CHAR_COLOR = (255, 0, 255)

# limit is length of snake
# CONSTRAINT: length of snake must be >= 1
limit = 1

# the length of the snake
queue = [] 

# initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
screen.fill(COLOR)
pygame.display.set_caption("Jack He Snake Game")

# font that will be used to display the current score to the player
FONT_SIZE = 32
font = pygame.font.Font('freesansbold.ttf', FONT_SIZE)
text = font.render('YOUR SCORE: 0', True, (255, 255, 255), COLOR) 
TEXT_RECT = text.get_rect()
TEXT_RECT.center = (WIDTH // 2, FONT_SIZE)
pygame.display.update()


# (Int, Int) -> Image
# draws a square onto the screen 
def drawRect(pos, size, color):
    coordinates = pygame.Rect((pos[0], pos[1]), (size[0], size[1]))
    pygame.draw.rect(screen, color, coordinates)
    pygame.display.update()

def placeFood(pos, size, color):
    coordinates = pygame.Rect((pos[0], pos[1]), (size[0], size[1]))
    pygame.draw.rect(screen, color, coordinates)

def erase(pos, size, color):
    coordinates = pygame.Rect(pos[0], pos[1], size[0], size[1])
    screen.fill(color, coordinates)

def up():
    if exist[1] - SPEED < FONT_SIZE:
        exist[1] = HEIGHT
    exist[1] -= SPEED
    queue.append(exist[:])
    drawRect(exist, SIZE, CHAR_COLOR) 

def down():
    if exist[1] + SPEED > HEIGHT:
        exist[1] = 0
    exist[1] += SPEED
    queue.append(exist[:])
    drawRect(exist, SIZE, CHAR_COLOR)

def left():
    if exist[0] - SPEED < 0:
        exist[0] = WIDTH 
    exist[0] -= SPEED
    queue.append(exist[:])
    drawRect(exist, SIZE, CHAR_COLOR)

def right():
    if exist[0] + SPEED > WIDTH:
        exist[0] = 0 
    exist[0] += SPEED
    queue.append(exist[:])
    drawRect(exist, SIZE, CHAR_COLOR)

mouse_is_pressed = False
move_right = True
move_left = False
move_down = False
move_up = False

def eatFood():
    global limit
    global foodX
    global foodY
    global FOOD_COLOR
    global CHAR_COLOR

    CHAR_COLOR = FOOD_COLOR[:]

    limit += 1
    foodX = randint(SPEED, WIDTH - SPEED)
    foodY = randint(SPEED + FONT_SIZE, HEIGHT - SPEED)
    FOOD_COLOR = (randint(10, 255), randint(10, 255), randint(10, 255))


def reset():
    global queue
    global limit
    print("collide!")
    for _ in range(len(queue)):
        erase(queue.pop(0), SIZE, COLOR)
    limit = 1
    erase([WIDTH // 4, 0], [WIDTH // 2, FONT_SIZE*2], COLOR)

# Controls the difficulty of this snake game
MARGIN_OF_ERROR = 25

# ============================ ============================ ============================
# ============================ ============================ ============================
# Start of Game Loop:


while run:
    visited = queue[:]
    if len(visited) >= 1:
        visited.pop()
    ateFood = (foodX - MARGIN_OF_ERROR <= exist[0] <= foodX + MARGIN_OF_ERROR) and (foodY - MARGIN_OF_ERROR <= exist[1] <= foodY + MARGIN_OF_ERROR)

    if len(queue) > limit:
        # maintains the size of the snake
        erase(queue.pop(0), SIZE, COLOR)

    if move_up:
        # check if next iteration will be a collision
        if exist in visited:
            reset()

        if ateFood:
            erase([foodX, foodY], FOOD_SIZE, COLOR)
            eatFood()
        up()

    elif move_down:
        # check if next iteration will be a collision
        if exist in visited:
            reset()

        if ateFood:
            erase([foodX, foodY], FOOD_SIZE, COLOR)
            eatFood()
        down()

    elif move_right:
        # check if next iteration will be a collision
        if exist in visited:
            reset()

        if ateFood:
            erase([foodX, foodY], FOOD_SIZE, COLOR)
            eatFood()
        right()

    elif move_left:
        # check if next iteration will be a collision
        if exist in visited:
            reset()
            limit = 1

        if ateFood:
            erase([foodX, foodY], FOOD_SIZE, COLOR)
            eatFood()

        left()
        
    # place random piece of food on the screen:
    placeFood([foodX, foodY], FOOD_SIZE, FOOD_COLOR)

    # display the current score to the player as a function of the length of the snake:
    points = limit * 10 - 10
    message = "YOUR SCORE: " + str(points)
    text = font.render(message, True, (255, 255, 255), COLOR)
    screen.blit(text, TEXT_RECT)

    # handle all the actions
    for event in pygame.event.get():
        action = event.type
        if action == pygame.QUIT:
            # quit button is pressed
            run = False

        elif action == pygame.MOUSEBUTTONDOWN:
            # mouse is pressed
            mouse_is_pressed = True

        elif action == pygame.MOUSEBUTTONUP:
            # mouse is released
            mouse_is_pressed = False

        elif action == pygame.KEYDOWN:
            # some keyboard button is pressed
            if event.key == pygame.K_SPACE:
                pass

            if event.key == pygame.K_w:
                print("up")
                move_up = True
                move_down = False
                move_right = False
                move_left = False
                
            elif event.key == pygame.K_a:
                print("left")
                move_up = False
                move_down = False
                move_right = False
                move_left = True

            elif event.key == pygame.K_s:
                print("down")
                move_up = False
                move_down = True
                move_right = False
                move_left = False
                
            elif event.key == pygame.K_d:
                print("right")
                move_up = False
                move_down = False
                move_right = True
                move_left = False