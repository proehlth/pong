import pygame, sys, random

#pong with keyboard and controller

def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score, score_time
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    if ball.left <= 0:
        player_score += 1
        score_time = pygame.time.get_ticks()

    if ball.right >= screen_width:
        opponent_score += 1
        score_time = pygame.time.get_ticks()

    if ball.colliderect(opponent):
        ball_speed_x *= -1
        player_sound.play()

    collision_tolerance = 10
    if ball.colliderect(player):
        if abs(ball.top - player.bottom) < collision_tolerance and ball_speed_y < 0:
            ball_speed_y *= -1
        if abs(ball.bottom - player.top) < collision_tolerance and ball_speed_y > 0:
            ball_speed_y *= -1
        if abs(ball.right - player.left) < collision_tolerance and ball_speed_x > 0:
            ball_speed_x *= -1
        if abs(ball.left - player.right) < collision_tolerance and ball_speed_x < 0:
            ball_speed_x *= -1
        player_sound.play()

def player_animation():
    player.y += player_speed[1]
    player.x += player_speed[0]
    if player.top <= 0:
        player.top = 5
    elif player.right >= screen_width:
        player.right = screen_width - 5
    elif player.left <= 0:
        player.left = 5
    elif player.bottom >= screen_height:
        player.bottom = screen_height - 5

def opponent_ai():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 5
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height -5

def ball_start():
    global ball_speed_x, ball_speed_y, score_time

    current_time = pygame.time.get_ticks()

    ball.center = (screen_width/2, screen_height/2)
    
    if 700 <current_time - score_time < 1400:
        number_three = countdown_font_100.render("3", True, light_grey)
        screen.blit(number_three,(screen_width/2-30, screen_height/2-200))
    if 1400 < current_time - score_time < 2100:
        number_two = countdown_font_100.render("2", True, light_grey)
        screen.blit(number_two,(screen_width/2-30, screen_height/2-200))
    if 2100 < current_time - score_time < 2800:
        number_one = countdown_font_150.render("Get ready!", True, light_grey)
        screen.blit(number_one,(screen_width/2-280, screen_height/2-200))
    if current_time - score_time < 2800:
        ball_speed_x = 0
        ball_speed_y = 0
    else:
        ball_speed_y = 7 * random.choice((1,-1))
        ball_speed_x = 7 * random.choice((1,-1))
        score_time = None


pygame.init()
clock = pygame.time.Clock()

pygame.mixer.init()
pygame.mixer.music.load("assets/backgroundmusic.ogg")
pygame.mixer.music.play(loops=-1)

pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Pong")

height = pygame.display.Info().current_h
width = pygame.display.Info().current_w

ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 30, screen_height/2 - 70, 20, 140)
opponent = pygame.Rect(10,screen_height/2 -70, 20, 140)

bg_color = pygame.Color("black")
bg = pygame.image.load("assets/starfield.gif")
light_grey = (255, 255, 255)

#Sound
player_sound = pygame.mixer.Sound("assets/pong_player.wav")
goal_sound = pygame.mixer.Sound("assets/goal.wav")
restart_sound = pygame.mixer.Sound("assets/restart.wav")

ball_speed_x = 5 * random.choice((1,-1))
ball_speed_y = 5 * random.choice((1,-1))

player_speed = [0,0]
opponent_speed = 7

player_score = 0
opponent_score = 0
game_font = pygame.font.Font("assets/leddisplay.ttf",100)
countdown_font_100 = pygame.font.Font("assets/badaboom.ttf", 100)
countdown_font_150 = pygame.font.Font("assets/badaboom.ttf", 150)

score_time = pygame.time.get_ticks()
ball_start()

# starfield
#create the locations of the stars for when we animate the background
star_field_slow = []
star_field_medium = []
star_field_fast = []

for slow_stars in range(50): #birth those plasma balls, baby
    star_loc_x = random.randrange(0, width)
    star_loc_y = random.randrange(0, height)
    star_field_slow.append([star_loc_x, star_loc_y]) #i love your balls

for medium_stars in range(35):
    star_loc_x = random.randrange(0, width)
    star_loc_y = random.randrange(0, height)
    star_field_medium.append([star_loc_x, star_loc_y])

for fast_stars in range(15):
    star_loc_x = random.randrange(0, width)
    star_loc_y = random.randrange(0, height)
    star_field_fast.append([star_loc_x, star_loc_y])

#define some commonly used colours
WHITE = (255, 255, 255)
LIGHTGREY = (192, 192, 192)
DARKGREY = (128, 128, 128)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.JOYAXISMOTION:
            if event.axis < 2:
                player_speed[event.axis] = event.value * 7
        elif event.type == pygame.JOYBUTTONDOWN:
            my_square_color = event.button
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed[1] += 7
            if event.key == pygame.K_UP:
                player_speed[1] -= 7
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed[1] -= 7
            if event.key == pygame.K_UP:
                player_speed[1] += 7

    ball_animation()
    player_animation()
    opponent_ai()

    screen.fill(bg_color)
    #screen.blit(bg,(0,0))

    for star in star_field_slow:
        star[1] += 1
        if star[1] > height:
            star[0] = random.randrange(0, width)
            star[1] = random.randrange(-20, -5)
        pygame.draw.circle(screen, DARKGREY, star, 3)

    for star in star_field_medium:
        star[1] += 2
        if star[1] > height:
            star[0] = random.randrange(0, width)
            star[1] = random.randrange(-20, -5)
        pygame.draw.circle(screen, LIGHTGREY, star, 2)

    for star in star_field_fast:
        star[1] += 3
        if star[1] > height:
            star[0] = random.randrange(0, width)
            star[1] = random.randrange(-20, -5)
        pygame.draw.circle(screen, YELLOW, star, 1)



    pygame.draw.rect(screen, light_grey, player,  10, 4)
    pygame.draw.rect(screen, light_grey, opponent, 10, 4)
    pygame.draw.ellipse(screen, light_grey, ball)
    
    if score_time:
        ball_start()

    player_text = game_font.render(f"{player_score}", True, light_grey)
    screen.blit(player_text,(screen_width*3/4-100,screen_height/2+150))
    opponent_text = game_font.render(f"{opponent_score}", True, light_grey)
    screen.blit(opponent_text,(screen_width/4+30,screen_height/2+150))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()