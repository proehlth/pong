import pygame, sys, random

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

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1
        player_sound.play()

def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 5
    if player.bottom >= screen_height:
        player.bottom = screen_height-5

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
        number_three = countdown_font_100.render("3", False, light_grey)
        screen.blit(number_three,(screen_width/2-30, screen_height/2-200))
    if 1400 < current_time - score_time < 2100:
        number_two = countdown_font_100.render("2", False, light_grey)
        screen.blit(number_two,(screen_width/2-30, screen_height/2-200))
    if 2100 < current_time - score_time < 2800:
        number_one = countdown_font_150.render("Get ready!", False, light_grey)
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

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Pong")

ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(10,screen_height/2 -70, 10, 140)

bg_color = pygame.Color("black")
bg = pygame.image.load("assets/grass.jpg")
light_grey = (200, 200, 200)

#Sound
player_sound = pygame.mixer.Sound("assets/pong_player.wav")
goal_sound = pygame.mixer.Sound("assets/goal.wav")
restart_sound = pygame.mixer.Sound("assets/restart.wav")

ball_speed_x = 5 * random.choice((1,-1))
ball_speed_y = 5 * random.choice((1,-1))

player_speed = 0
opponent_speed = 7

player_score = 0
opponent_score = 0
game_font = pygame.font.Font("assets/leddisplay.ttf",100)
countdown_font_100 = pygame.font.Font("assets/badaboom.ttf", 100)
countdown_font_150 = pygame.font.Font("assets/badaboom.ttf", 150)

score_time = pygame.time.get_ticks()
ball_start()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -=7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    ball_animation()
    player_animation()
    opponent_ai()

    screen.fill(bg_color)
    screen.blit(bg,(0,0))
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height))
    
    if score_time:
        ball_start()

    player_text = game_font.render(f"{player_score}", False, light_grey)
    screen.blit(player_text,(screen_width*3/4-30,screen_height/2+150))
    opponent_text = game_font.render(f"{opponent_score}", False, light_grey)
    screen.blit(opponent_text,(screen_width/4-30,screen_height/2+150))

    pygame.display.flip()
    clock.tick(60)