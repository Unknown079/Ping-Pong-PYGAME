import pygame

pygame.init()

# RGB colors
RGB = (224, 224, 224)

# FPS
FPS = 80

# HEIGHT AND WIDTH
s_width, s_height = 1000, 800

screen = pygame.display.set_mode((s_width, s_height)) # Resolution
pygame.display.set_caption("Retro Ping Pong") # Name of the window
icon = pygame.image.load("basketball-ball.png") # Image of the window
pygame.display.set_icon(icon)

# Pallet1
def pallet1_stuff(p1):
    pallet1_width, pallet1_height = 56, 90 # Height and width of the pallet
    pallet_img = pygame.image.load("palet.png") # Image
    pallet_rotate = pygame.transform.rotate(pallet_img, 90) # Degrees
    pallet_size = pygame.transform.scale(pallet_rotate, (pallet1_width, pallet1_height)) # Scale
    screen.blit(pallet_size, (p1.x, p1.y)) # Coordonates

# Pallet2
def pallet2_stuff(p2):
    pallet2_width, pallet2_height = 56, 90 # Height and width of the pallet
    pallet2_img = pygame.image.load("paletv2.png") # Image
    pallet2_rotate = pygame.transform.rotate(pallet2_img, 90) # Degrees
    pallet2_size = pygame.transform.scale(pallet2_rotate, (pallet2_width, pallet2_height)) #Scale
    screen.blit(pallet2_size, (p2.x, p2.y)) # Coordonates..

# Ball
def ball_stuff(ball1):
    b1_width, b1_height = 35, 35 # height and the width of the ball
    ball_img = pygame.image.load("soccer-ball.png") # Image
    ball1_size = pygame.transform.scale(ball_img, (b1_width, b1_height)) # Scale
    screen.blit(ball1_size, (ball1.x, ball1.y)) # Coordonates..

# Movement
def players_movement(p1, p2, keys_pressed):
    if keys_pressed[pygame.K_w]:
        p1.y -= 11
    if keys_pressed[pygame.K_s]:
        p1.y += 11
    if keys_pressed[pygame.K_UP]:
        p2.y -= 11
    if keys_pressed[pygame.K_DOWN]:
        p2.y += 11

# yeah.. :)
def ball_movement():
    global x_speed, y_speed
    ball1.y += y_speed
    ball1.x += x_speed

    # Collision with the border
    if ball1.bottom >= s_height or ball1.top <= 0:
        y_speed *= -1

    # Collision with the ball
    collision_tolerance = 10
    if ball1.colliderect(p2):
        if abs(p2.top - ball1.bottom) < collision_tolerance:
            y_speed *= -1
        if abs(p2.bottom - ball1.top) < collision_tolerance:
            y_speed *= -1
        if abs(p2.right - ball1.left) < collision_tolerance:
            x_speed *= -1
        if abs(p2.left - ball1.right) < collision_tolerance:
            x_speed *= -1
    if ball1.colliderect(p1):
        if abs(p1.top - ball1.bottom) < collision_tolerance:
            y_speed *= -1
        if abs(p1.bottom - ball1.top) < collision_tolerance:
            y_speed *= -1
        if abs(p1.right - ball1.left) < collision_tolerance:
            x_speed *= -1
        if abs(p1.left - ball1.right) < collision_tolerance:
            x_speed *= -1
p1 = pygame.Rect(20, 400, 56, 90)
p2 = pygame.Rect(920, 400, 56, 90)
ball1 = pygame.Rect(500, 400, 35, 35)
x_speed, y_speed = 6, 6

# Display running
running = True
clock = pygame.time.Clock()
while running:
    clock.tick(FPS)
    screen.fill(RGB)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Boundaries of P1
    if p1.y <= 0:
        p1.y = 0
    elif p1.y >= 710:
        p1.y = 710

    # Boundaries of P2
    if p2.y <= 0:
        p2.y = 0
    elif p2.y >= 710:
        p2.y = 710


    keys_pressed = pygame.key.get_pressed()

    players_movement(p1, p2, keys_pressed)
    pallet1_stuff(p1)
    pallet2_stuff(p2)
    ball_stuff(ball1)
    ball_movement()

    # Update the screen each time..
    pygame.display.update()