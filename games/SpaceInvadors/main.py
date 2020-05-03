import pygame

pygame.init()
# create screen use tuple to initialize the size of the screen
screen = pygame.display.set_mode((800, 600))

# title and icon
pygame.display.set_caption("Space Invaders")
# create the variable to load the image and then use the image
icon = pygame.image.load('technology.png')
pygame.display.set_icon(icon)

#initialzing the player
playerImg= pygame.image.load('player.png')
#initialize the position 
playerX = 370
playerY = 400
playerX_change= 0.1
playerY_change= 0.1
def player(x,y):
    screen.blit(playerImg,(x,y))


running = True
while running:
    screen.fill((0, 0, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # adding keystroke
        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_LEFT:
                print("left arraow pressed")
                playerX_change = -0.1

            if event.key ==pygame.K_RIGHT:
                playerX_change = 0.1
                print("left arraow pressed")
        if event.type == pygame.KEYUP:
            if event.key ==pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("Keystroke has been released ")
    playerX += playerX_change
    player(playerX,playerY)
    #necessary in order to update the screen else it will show previous data only
    pygame.display.update()