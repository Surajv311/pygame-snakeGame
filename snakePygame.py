import pygame, sys
import time
import random
pygame.init()
white = (255, 255, 255)
black = (100, 0, 0)
red = (255, 0, 0)
gameWindow_width = 500
gameWindow_height = 500
gameDisplaySize = pygame.display.set_mode((gameWindow_width, gameWindow_height))
pygame.display.set_caption('Snake Game') # give the name of the game
clock = pygame.time.Clock() #
FPS = 8 # fps is frames per second
snake_size = 12 #snake_size is the size of the snake
noPixel = 0

def myquit():
   # when you want to quit the game
    pygame.quit()
    sys.exit(0)
font = pygame.font.SysFont(None, 25, bold=True)
def drawGrid():
    sizeGrd = gameWindow_width // snake_size
def snake(snake_size, snakelist):
    # x = 250 - (segment_width + segment_margin) * i
    for size in snakelist:
        pygame.draw.rect(gameDisplaySize, black, [size[0] + 5, size[1], snake_size, snake_size], 2)
def messageOnScreen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplaySize.blit(screen_text, [gameWindow_width / 2, gameWindow_height / 2])
def gameLoop():
    game_Exit = False
    game_Over = False
    x_Width = gameWindow_width / 2
    y_Height = gameWindow_height / 2
    changeIn_x = 0
    changeIn_y = 0
    snakelist = []
    snakeLength = 1
    random_food_X = round(random.randrange(0, gameWindow_width - snake_size) / 10.0) * 10.0 # food in x 
    random_food_Y = round(random.randrange(0, gameWindow_height - snake_size) / 10.0) * 10.0
    while not game_Exit:
        while game_Over == True:
            gameDisplaySize.fill(white)
            messageOnScreen("Game over!", black)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_Over = False
                    game_Exit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_Exit = True
                        game_Over = False
                    if event.key == pygame.K_c:
                        gameLoop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_Exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    myquit()
                leftArrow = event.key == pygame.K_LEFT
                rightArrow = event.key == pygame.K_RIGHT
                upArrow = event.key == pygame.K_UP
                downArrow = event.key == pygame.K_DOWN
                if leftArrow: #keyboard arrow commands 
                    changeIn_x = -snake_size
                    changeIn_y = noPixel
                elif rightArrow:
                    changeIn_x = snake_size
                    changeIn_y = noPixel
                elif upArrow:
                    changeIn_y = -snake_size
                    changeIn_x = noPixel
                elif downArrow:
                    changeIn_y = snake_size
                    changeIn_x = noPixel
            if x_Width >= gameWindow_width or x_Width < 0 or y_Height >= gameWindow_height or y_Height < 0:
                game_Over = True
        x_Width += changeIn_x
        y_Height += changeIn_y
        gameDisplaySize.fill(white)
        random_Food = 12
        print([int(random_food_X), int(random_food_Y), random_Food, random_Food])
        pygame.draw.rect(gameDisplaySize, red, [random_food_X, random_food_Y, random_Food, random_Food])
        allspriteslist = []
        allspriteslist.append(x_Width)
        allspriteslist.append(y_Height)
        snakelist.append(allspriteslist)
        if len(snakelist) > snakeLength:
            del snakelist[0]
        for eachSegment in snakelist[:-1]:
            if eachSegment == allspriteslist:
                game_Over = True
        snake(snake_size, snakelist)
        pygame.display.update()
        if x_Width >= random_food_X and x_Width <= random_food_X + random_Food:
            if y_Height >= random_food_Y and y_Height <= random_food_Y + random_Food:
                random_food_X = round(random.randrange(0, gameWindow_width - snake_size) / 10.0) * 10.0
                random_food_Y = round(random.randrange(0, gameWindow_height - snake_size) / 10.0) * 10.0
                snakeLength += 1
        clock.tick(FPS)
    pygame.quit()
    quit()
gameLoop()