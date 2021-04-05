import pygame

pygame.init()

# RGB colors
RGB = (255, 255, 255)

# FPS
FPS = 120

# Velocity
VEL = 0.2

screen = pygame.display.set_mode((1000, 800)) # Resolution
pygame.display.set_caption("Retro Ping Pong ") # Name of the window
icon = pygame.image.load("basketball-ball.png") # Image of the window
pygame.display.set_icon(icon)

# Pallet1
def pallet1_stuff():
    pallet1_width, pallet1_height = 56, 90
    pallet_img = pygame.image.load("palet.png") # Image
    pallet_rotate = pygame.transform.rotate(pallet_img, 90) # Degrees
    pallet_size = pygame.transform.scale(pallet_rotate, (pallet1_width, pallet1_height)) # Scale
    screen.blit(pallet_size, (p1.x, p1.y)) # Coordonates

# Pallet2
def pallet2_stuff():
    pallet2_width, pallet2_height = 56, 90
    pallet_img = pygame.image.load("paletv2.png") # Image
    pallet_rotate = pygame.transform.rotate(pallet_img, 90) # Degrees
    pallet_size = pygame.transform.scale(pallet_rotate, (pallet2_width, pallet2_height)) #Scale
    screen.blit(pallet_size, (p2.x, p2.y)) # Coordonates

p1 = pygame.Rect(20, 400, 56, 90)
p2 = pygame.Rect(920, 400, 56, 90)

# Display running
running = True
while running:
    clock = pygame.time.Clock()
    screen.fill(RGB)
    for event in pygame.event.get():
        clock.tick(FPS)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                p1.y -= VEL
            if event.key == pygame.K_s:
                p1.y += VEL
            if event.key == pygame.K_UP:
                p2.y -= VEL
            if event.key == pygame.K_DOWN:
                p2.y += VEL
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                p1.y += 0
                p2.y += 0

    keys_pressed = pygame.key.get_pressed()

    pallet1_stuff()
    pallet2_stuff()
    # Update the screen each time..
    pygame.display.update()