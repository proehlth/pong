import pygame

def quadrat_anim(x,y):
    quadrat.x += x
    quadrat.y += y

pygame.init()

fps = 60
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Controller-Test")
clock = pygame.time.Clock()

quadrat = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
quadrat_speed_x = 0
quadrat_speed_y = 0

bg_color = pygame.Color('black')
fg_color = pygame.Color('white')

pygame.joystick.init()

controller = pygame.joystick.Joystick(0)
controller.init()
print(controller.get_guid())
print(controller.get_power_level())
print(controller.get_numhats())
print(controller.get_hat(0))

running = True
motion = [0,0]

while running:
    for event in pygame.event.get(): # User did something.
        if event.type == pygame.QUIT: # If user clicked close.
            running = False # Flag that we are done so we exit this loop.
        elif event.type == pygame.JOYBUTTONDOWN:
            if event.button == 0:
                fg_color = pygame.Color('green')
            if event.button == 1:
                fg_color = pygame.Color('orange')
            if event.button == 2:
                fg_color = pygame.Color('blue')
            if event.button == 3:
                fg_color = pygame.Color('yellow')
        elif event.type == pygame.JOYBUTTONUP:
            fg_color = pygame.Color('white')
        elif event.type == pygame.JOYAXISMOTION:
            print(event)
            if event.axis < 2:
                motion[event.axis] = event.value
        elif event.type == pygame.JOYHATMOTION:
            print(controller.get_hat(0))
            if event.value == (-1,0):
                quadrat_speed_x -= 7
            if event.value == (0,1):
                quadrat_speed_y -= 7
            if event.value == (1,0):
                quadrat_speed_x += 7
            if event.value == (0,-1):
                quadrat_speed_y += 7
            if event.value == (-1,1):
                quadrat_speed_x -= 7
                quadrat_speed_y -= 7
            if event.value == (-1,-1):
                quadrat_speed_x -= 7
                quadrat_speed_y += 7
            if event.value == (1,-1):
                quadrat_speed_x += 7
                quadrat_speed_y += 7
            if event.value == (1,1):
                quadrat_speed_x += 7
                quadrat_speed_y -= 7
            if event.value == (0,0):
                quadrat_speed_y = 0
                quadrat_speed_x = 0
            

    quadrat_anim(quadrat_speed_x, quadrat_speed_y)

    screen.fill(bg_color)
    pygame.draw.rect(screen, fg_color, quadrat)
    pygame.display.flip()

    clock.tick(fps)

pygame.quit()

    