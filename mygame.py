import math
import random
import pygame
from pygame import mixer

# from main import collision, explosionSound

#initilize the pygame.
pygame.init()

# creating the screen
screen = pygame.display.set_mode((800, 600))
running = True

# Setting the title of the game window
pygame.display.set_caption("MY SPACE GAME")

# Setting the icon of the window by downloading www.flaticon.com png image 32x32
icon = pygame.image.load('.\\spacegames\\ufo.png')
pygame.display.set_icon(icon)


#sound
mixer.music.load(".\\spacegames\\background.wav")
mixer.music.play(-1)

#player
playerimg = pygame.image.load('.\\spacegames\\player.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 3

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('.\\spacegames\\enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)


backimg=pygame.image.load('.\\spacegames\\background.png')

#bullet
bulletimg=pygame.image.load('.\\spacegames\\bullet.png')
#bullet ready state means not fire
#bullet fire state means currently fire
bulletX=0
bulletY=480
bullet_changeX=0
bullet_changeY=10
bullet_state='ready'

#score
score_value=0
font = pygame.font.Font('.\\FreeSans\\FreeSansBold.ttf', 32)
textX=10
textY=10

#game over
over_font=pygame.font.Font('.\\FreeSans\\FreeSansBold.ttf', 70)

# methods to draw image on the screen
def player(x, y):
    screen.blit(playerimg, (x, y))
    # here blit means draw


def enemy(x, y,i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state='fire'
    screen.blit(bulletimg, (x+15,y+10))

def iscollision(enemyX, enemyY, bulletX, bulletY):
    distance=math.sqrt(math.pow(enemyX-bulletX,2)+(math.pow(enemyY-bulletY,2)))

    if distance <27:
        return True
    else:
        return False

def show_score(x,y):
    score=font.render("Score:" + str(score_value),True,(255,255,255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text=over_font.render("GAME OVER",True,(255,255,255))
    screen.blit(over_text, (200, 250))

#spaceimage=pygame.image
# infinite loop for stop the window on the screen
while running:
    screen.fill((193, 118, 171))
    # playerX+=.2
    screen.blit(backimg,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -10
            if event.key == pygame.K_RIGHT:
                playerX_change = 10
            if event.key == pygame.K_SPACE:
                if bullet_state is 'ready':
                    bulletSound=mixer.Sound('.\\spacegames\\laser.wav')
                    bulletSound.play()
                    bulletX=playerX
                    fire_bullet(bulletX,bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX+=playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    for i in range(num_of_enemies):


        #game over
        if enemyY[i]>440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break


        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]


        collision=iscollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosionSound=mixer.Sound('.\\spacegames\\explosion.wav')
            explosionSound.play()
            bulletY=480
            bullet_state='ready'
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    if bulletY <=0:
        bulletY=480
        bullet_state='ready'

    if bullet_state == 'fire':
        fire_bullet(bulletX,bulletY)
        bulletY-=bullet_changeY
    player(playerX,playerY)
    show_score(textX,textY)
    pygame.display.update()

'''            
Setting background color. any thing that we want inside
to screen continuously, it will given in while loop.
screen.fill(r,g,b) any thing after change we need to update
the display           
'''









