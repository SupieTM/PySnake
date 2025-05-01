import pygame
from time import sleep
from random import randint
from more_itertools import locate

pygame.init()

WINDOWSIZE = [500, 500]
WINDOWCOLOR = (100, 100, 100)
BORDORCOLOR = [0, 0, 0]
BORDORSIZE = [0, 0] + WINDOWSIZE
BORDERWIDTH = 20
SNAKESIZE = 20
SNAKEBODYPARTS = 5
SNAKESPEED = 50
COLORSNAKE = [0, 255, 0]
COLORFOOD = [255, 0, 0]
STARTINGCORD = [((WINDOWSIZE[1] - BORDERWIDTH) / 2),
                ((WINDOWSIZE[0] - BORDERWIDTH) / 2)]
INITIALPOINTS = 0
INITALDIRECTION = 3
POINTTEXTCOLOR = [255, 255, 255]


class snake:
    def __init__(snake, xcord, ycord):
        snake.xcord = xcord
        snake.ycord = ycord

    def __init__(snake, bodypts, direction):
        snake.bodypts = bodypts
        snake.direction = direction


class food:
    def __init__(food, xcord, ycord, points):
        food.xcord = xcord
        food.ycord = ycord
        food.points = points


snake.bodypts = SNAKEBODYPARTS
snake.xcord = []
snake.ycord = []

for x in range(snake.bodypts, -1, -1):
    xcord = STARTINGCORD[0] - SNAKESIZE * x
    snake.xcord.append(xcord)

for y in range(snake.bodypts, -1, -1):
    ycord = STARTINGCORD[1]
    snake.ycord.append(ycord)

snake.direction = INITALDIRECTION
food.points = INITIALPOINTS

# Create screen
surface = pygame.display.set_mode(WINDOWSIZE)
pygame.display.set_caption("WIGGLY SNAK GAM")
surface.fill(WINDOWCOLOR)
pygame.draw.rect(surface, BORDORCOLOR, BORDORSIZE, BORDERWIDTH)

pygame.display.flip()


running = True


def mleft():
    snake.xcord.insert(len(snake.xcord), snake.xcord[-1] - SNAKESIZE)
    snake.ycord.insert(len(snake.ycord), snake.ycord[-1])
    snake.xcord = snake.xcord[(len(snake.xcord) - (snake.bodypts + 1))::]
    snake.ycord = snake.ycord[(len(snake.ycord) - (snake.bodypts + 1))::]
    pygame.draw.rect(surface, COLORSNAKE, rect=[
                     snake.xcord[-1], snake.ycord[-1], SNAKESIZE, SNAKESIZE])
    pygame.draw.rect(surface, WINDOWCOLOR, rect=[
                     snake.xcord[-(snake.bodypts + 1)], snake.ycord[-(snake.bodypts + 1)], SNAKESIZE, SNAKESIZE])
    pygame.display.update()


def mright():
    snake.xcord.insert(len(snake.xcord), snake.xcord[-1] + SNAKESIZE)
    snake.ycord.insert(len(snake.ycord), snake.ycord[-1])
    snake.xcord = snake.xcord[(len(snake.xcord) - (snake.bodypts + 1))::]
    snake.ycord = snake.ycord[(len(snake.ycord) - (snake.bodypts + 1))::]
    pygame.draw.rect(surface, COLORSNAKE, rect=[
                     snake.xcord[-1], snake.ycord[-1], SNAKESIZE, SNAKESIZE])
    pygame.draw.rect(surface, WINDOWCOLOR, rect=[
                     snake.xcord[-(snake.bodypts + 1)], snake.ycord[-(snake.bodypts + 1)], SNAKESIZE, SNAKESIZE])
    pygame.display.update()


def mup():
    snake.xcord.insert(len(snake.xcord), snake.xcord[-1])
    snake.ycord.insert(len(snake.ycord), snake.ycord[-1] + SNAKESIZE)
    snake.xcord = snake.xcord[(len(snake.xcord) - (snake.bodypts + 1))::]
    snake.ycord = snake.ycord[(len(snake.ycord) - (snake.bodypts + 1))::]
    pygame.draw.rect(surface, COLORSNAKE, rect=[
                     snake.xcord[-1], snake.ycord[-1], SNAKESIZE, SNAKESIZE])
    pygame.draw.rect(surface, WINDOWCOLOR, rect=[
                     snake.xcord[-(snake.bodypts + 1)], snake.ycord[-(snake.bodypts + 1)], SNAKESIZE, SNAKESIZE])
    pygame.display.update()


def mdown():
    snake.xcord.insert(len(snake.xcord), snake.xcord[-1])
    snake.ycord.insert(len(snake.ycord), snake.ycord[-1] - SNAKESIZE)
    snake.xcord = snake.xcord[(len(snake.xcord) - (snake.bodypts + 1))::]
    snake.ycord = snake.ycord[(len(snake.ycord) - (snake.bodypts + 1))::]
    pygame.draw.rect(surface, COLORSNAKE, rect=[
                     snake.xcord[-1], snake.ycord[-1], SNAKESIZE, SNAKESIZE])
    pygame.draw.rect(surface, WINDOWCOLOR, rect=[
                     snake.xcord[-(snake.bodypts + 1)], snake.ycord[-(snake.bodypts + 1)], SNAKESIZE, SNAKESIZE])
    pygame.display.update()


def gfood():
    pygame.draw.rect(surface, BORDORCOLOR, rect=[
                     0, 0, WINDOWSIZE[0], BORDERWIDTH])
    food.xcord = randint(
        0, ((WINDOWSIZE[0] - 2 * BORDERWIDTH) / SNAKESIZE) - 1) * SNAKESIZE + BORDERWIDTH
    food.ycord = randint(
        0, ((WINDOWSIZE[1] - 2 * BORDERWIDTH) / SNAKESIZE) - 1) * SNAKESIZE + BORDERWIDTH

    if food.xcord in snake.xcord[len(snake.xcord) - (snake.bodypts):len(snake.xcord) - 1:] and food.ycord in snake.ycord[len(snake.ycord) - (snake.bodypts):len(snake.ycord) - 1:]:
        print('check')
        xfood = index_xcheck(snake.xcord[len(
            snake.xcord) - (snake.bodypts):len(snake.xcord) - 1:], food.xcord)
        yfood = index_xcheck(snake.ycord[len(
            snake.ycord) - (snake.bodypts):len(snake.ycord) - 1:], food.ycord)

        while common_element(xfood, yfood) > 0:
            food.xcord = randint(
                0, ((WINDOWSIZE[0] - 2 * BORDERWIDTH) / SNAKESIZE) - 1) * SNAKESIZE + BORDERWIDTH
            food.xcord = randint(
                0, ((WINDOWSIZE[0] - 2 * BORDERWIDTH) / SNAKESIZE) - 1) * SNAKESIZE + BORDERWIDTH
            xfood = index_xcheck(snake.xcord[len(
                snake.xcord) - (snake.bodypts):len(snake.xcord) - 1:], food.xcord)
            yfood = index_xcheck(snake.ycord[len(
                snake.ycord) - (snake.bodypts):len(snake.ycord) - 1:], food.ycord)

    pygame.draw.rect(surface, COLORFOOD, rect=[
                     food.xcord, food.ycord, SNAKESIZE, SNAKESIZE])
    font = pygame.font.Font('freesansbold.ttf', 20)
    txt = font.render(str(food.points), True, POINTTEXTCOLOR)
    txtrect = txt.get_rect()
    txtrect.center = (WINDOWSIZE[0] // 2, 10)
    surface.blit(txt, txtrect)
    food.points += 1
    pygame.display.flip()


gfood()

# 1 = left
# 2 = up
# 3 = right
# 4 = down


def leftkey():
    if snake.direction == 2:
        snake.direction = 1
    if snake.direction == 4:
        snake.direction = 1


def rightkey():
    if snake.direction == 2:
        snake.direction = 3
    if snake.direction == 4:
        snake.direction = 3


def upkey():
    if snake.direction == 1:
        snake.direction = 2
    if snake.direction == 3:
        snake.direction = 2


def downkey():
    if snake.direction == 1:
        snake.direction = 4
    if snake.direction == 3:
        snake.direction = 4


def index_xcheck(list2check, value):
    index = locate(list2check, lambda x: x == value)
    return (list(index))


def common_element(list1, list2):
    common = 0
    for i in list1:
        for b in list2:
            if i == b:
                common += 1

    return (common)


def endingscreen():
    pygame.draw.rect(surface, BORDORCOLOR, rect=(
        0, 0, WINDOWSIZE[0], WINDOWSIZE[1]))
    font = pygame.font.Font('freesansbold.ttf', 20)
    txt = font.render("You Failed", True, POINTTEXTCOLOR)
    pttxt = font.render(str(food.points - 1), True, POINTTEXTCOLOR)
    txtrect = txt.get_rect()
    txtrect.center = (WINDOWSIZE[0] // 2, WINDOWSIZE[-1] // 2)
    ptrect = pttxt.get_rect()
    ptrect.center = (WINDOWSIZE[0] // 2,
                     WINDOWSIZE[-1] // 2 - WINDOWSIZE[-1] * .15)
    surface.blit(txt, txtrect)
    surface.blit(pttxt, ptrect)
    pygame.display.flip()
    sleep(3)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                leftkey()
            elif event.key == pygame.K_d:
                rightkey()
            elif event.key == pygame.K_w:
                upkey()
            elif event.key == pygame.K_s:
                downkey()

    if snake.direction == 1:
        mleft()
    if snake.direction == 2:
        mdown()
    if snake.direction == 3:
        mright()
    if snake.direction == 4:
        mup()
    if snake.xcord[-1] == food.xcord and snake.ycord[-1] == food.ycord:
        snake.bodypts += 1
        gfood()

    if snake.xcord[-1] < (0 + BORDERWIDTH) or snake.xcord[-1] >= (WINDOWSIZE[0] - BORDERWIDTH) or snake.ycord[-1] < (0 + BORDERWIDTH) or snake.ycord[-1] >= (WINDOWSIZE[0] - BORDERWIDTH):
        print('failed')
        running = False
        endingscreen()

    if snake.xcord[-1] in snake.xcord[len(snake.xcord) - (snake.bodypts):len(snake.xcord) - 1:] and snake.ycord[-1] in snake.ycord[len(snake.ycord) - (snake.bodypts):len(snake.ycord) - 1:]:
        x = index_xcheck(snake.xcord[len(
            snake.xcord) - (snake.bodypts):len(snake.xcord) - 1:], snake.xcord[-1])
        y = index_xcheck(snake.ycord[len(
            snake.ycord) - (snake.bodypts):len(snake.ycord) - 1:], snake.ycord[-1])
        if common_element(x, y) > 0:
            print('Failed2')
            running = False
            endingscreen()

    sleep(10 / SNAKESPEED)
