import pygame
from pygame import color
from pygame.constants import JOYAXISMOTION

#Pong with Controller

pygame.init()

pygame.display.set_caption('Controller-Test')
screen = pygame.display.set_mode((500,500))

clock = pygame.time.Clock()

pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

my_square = pygame.Rect(50,50,50,50)
my_ball = pygame.Rect(10,10,10,10)
my_square_color = 0
colors = [pygame.Color("green"), pygame.Color("orange"), pygame.Color("blue"), pygame.Color("yellow")]
motion = [0, 0]
ball_speed = [5, 5]

run = True

while run:

    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
        elif event.type == pygame.JOYAXISMOTION:
            if event.axis < 2:
                motion[event.axis] = event.value
        elif event.type == pygame.JOYBUTTONDOWN:
            my_square_color = event.button
        elif event.type == pygame.JOYHATMOTION:
            if event.value == (-1,0):
                motion[0] -= 1
            if event.value == (0,1):
                motion[1] -= 1
            if event.value == (1,0):
                motion[0] += 1
            if event.value == (0,-1):
                motion[1] += 1
            if event.value == (-1,1):
                motion[0] -= 1
                motion[1] -= 1
            if event.value == (-1,-1):
                motion[0] -= 1
                motion[1] += 1
            if event.value == (1,-1):
                motion[0] += 1
                motion[1] += 1
            if event.value == (1,1):
                motion[0] += 1
                motion[1] -= 1
            if event.value == (0,0):
                motion[0] = 0
                motion[1] = 0

    # moving ball
    my_ball.x += ball_speed[0]
    my_ball.y += ball_speed[1]

    if my_ball.top <= 0 or my_ball.bottom >= 500:
        ball_speed[1] *= -1

    if my_ball.left <= 0 or my_ball.right >= 500:
        ball_speed[0] *= -1

    # moving square
    my_square.x += motion[0] * 10
    my_square.y += motion[1] * 10
    if my_square.top <= 0:
        my_square.top = 0
    if my_square.bottom >= 500:
        my_square.bottom = 500
    if my_square.left <= 0:
        my_square.left = 0
    if my_square.right >= 500:
        my_square.right = 500

    # collision
    collision_tolerance = 10
    if my_square.colliderect(my_ball):
        if abs(my_ball.top - my_square.bottom) < collision_tolerance and ball_speed[1] < 0:
            ball_speed[1] *= -1
        if abs(my_ball.bottom - my_square.top) < collision_tolerance and ball_speed[1] > 0:
            ball_speed[1] *= -1
        if abs(my_ball.right - my_square.left) < collision_tolerance and ball_speed[0] > 0:
            ball_speed[0] *= -1
        if abs(my_ball.left - my_square.right) < collision_tolerance and ball_speed[0] < 0:
            ball_speed[0] *= -1

    pygame.draw.rect(screen, colors[my_square_color], my_square)
    pygame.draw.ellipse(screen, colors[my_square_color], my_ball)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
