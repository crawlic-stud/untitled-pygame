import pygame
import random

pygame.init()
displayWidth = 500
displayHeight = 500
win = pygame.display.set_mode((displayWidth, displayHeight))

pygame.display.set_caption('POOPRUN')

clock = pygame.time.Clock()

playerX = 50
playerY = displayHeight - 60
playerWidth = 50
playerHeight = 50
playerSpeed = 5

bullets = []

isJump = False
jumpCount = 10

left = False
right = False
animCount = 0
lastMove = 'right'

walkRight = [pygame.image.load('sprites/right (4).png'),
             pygame.image.load('sprites/right (5).png'), pygame.image.load('sprites/right (6).png'), pygame.image.load('sprites/right (7).png'), pygame.image.load('sprites/right (8).png'),
             pygame.image.load('sprites/right (9).png'), pygame.image.load('sprites/right (10).png'), pygame.image.load('sprites/right (11).png'), pygame.image.load('sprites/right (12).png'),
             pygame.image.load('sprites/right (13).png'), pygame.image.load('sprites/right (14).png'), pygame.image.load('sprites/right (15).png')]

walkLeft = [pygame.image.load('sprites/left (4).png'),
            pygame.image.load('sprites/left (5).png'), pygame.image.load('sprites/left (6).png'), pygame.image.load('sprites/left (7).png'), pygame.image.load('sprites/left (8).png'),
            pygame.image.load('sprites/left (9).png'), pygame.image.load('sprites/left (10).png'), pygame.image.load('sprites/left (11).png'), pygame.image.load('sprites/left (12).png'),
            pygame.image.load('sprites/left (13).png'), pygame.image.load('sprites/left (14).png'), pygame.image.load('sprites/left (15).png')]

playerStand = [pygame.image.load('sprites/front (1).png'), pygame.image.load('sprites/front (2).png'), pygame.image.load('sprites/front (3).png'),
               pygame.image.load('sprites/front (4).png'), pygame.image.load('sprites/front (5).png')]

fire1 = [pygame.image.load('sprites/fire1.png'), pygame.image.load('sprites/fire2.png'), pygame.image.load('sprites/fire3.png'), pygame.image.load('sprites/fire4.png'),
         pygame.image.load('sprites/fire5.png'), pygame.image.load('sprites/fire5.png'), pygame.image.load('sprites/fire4.png'), pygame.image.load('sprites/fire3.png'),
         pygame.image.load('sprites/fire2.png'), pygame.image.load('sprites/fire1.png')]

fire2 = [pygame.image.load('sprites/fire11.png'), pygame.image.load('sprites/fire22.png'), pygame.image.load('sprites/fire33.png'), pygame.image.load('sprites/fire44.png'),
         pygame.image.load('sprites/fire55.png'), pygame.image.load('sprites/fire55.png'), pygame.image.load('sprites/fire44.png'), pygame.image.load('sprites/fire33.png'),
         pygame.image.load('sprites/fire22.png'), pygame.image.load('sprites/fire11.png')]

fire3 = [pygame.image.load('sprites/fire111.png'), pygame.image.load('sprites/fire222.png'), pygame.image.load('sprites/fire333.png'), pygame.image.load('sprites/fire444.png'),
         pygame.image.load('sprites/fire555.png'), pygame.image.load('sprites/fire555.png'), pygame.image.load('sprites/fire444.png'), pygame.image.load('sprites/fire333.png'),
         pygame.image.load('sprites/fire222.png'), pygame.image.load('sprites/fire111.png')]


class Spike:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


    def move(self, speed):
        if self.x >= -self.width:
            self.x -= speed
        else:
            if choice():
                self.x = displayWidth + 50 + random.randrange(0, 50)
            else:
                self.x = displayWidth + random.randrange(100, 300)

    def checkPos(self):
        if self.x < -self.width:
            return True
        else:
            return False

class Shoot:
    def __init__(self, x, y, facing):
        self.x = x
        self.y = y
        self.facing = facing
        self.vel = 5 * facing  # velocity

    def draw(self, win):
        win.blit(pygame.image.load('sprites/poop.png'), (self.x, self.y))

def choice():
    check = random.randint(0, 5)
    if check == 0:
        return True
    else:
        return False

def drawWindow():
    global animCount
    win.fill((0, 0, 0))

    # win.blit(background, (0, 0)) - for background

    if animCount + 1 >= 60:
        animCount = 0

    if left:
        win.blit(walkLeft[animCount // 5], (playerX, playerY))
        animCount += 1
    elif right:
        win.blit(walkRight[animCount // 5], (playerX, playerY))
        animCount += 1
    else:
        win.blit(playerStand[animCount // 12], (playerX, playerY))
        animCount += 1

    for bullet in bullets:
        bullet.draw(win)

def jump():
    global playerY, jumpCount, isJump

    if jumpCount >= -10:
        if jumpCount < 0:
            playerY += (jumpCount ** 2) // 1.5
        else:
            playerY -= (jumpCount ** 2) // 1.5
        jumpCount -= 1
    else:
        isJump = False
        jumpCount = 10

#def shooting(bullets)

def createSpikes(spikes, x=500):
    spikes.append(Spike(x + 100, displayHeight - 90, 30, 80))
    spikes.append(Spike(x + 300, displayHeight - 60, 40, 50))
    spikes.append(Spike(x + 550, displayHeight - 75, 50, 65))

def drawSpikes(spikes, speed=6):
    for spike in spikes:
        if spike.width == 30:
            win.blit(fire1[animCount//6], (spike.x, spike.y))
        elif spike.width == 40:
            win.blit(fire2[animCount//6], (spike.x, spike.y))
        elif spike.width == 50:
            win.blit(fire3[animCount//6], (spike.x, spike.y))
        spike.move(speed)

def printText(message, x, y, fontColor = (255, 255, 255), font = '21002.ttf', fontSize = 30):
    font = pygame.font.Font(font, fontSize)
    text = font.render(message, True, fontColor)
    win.blit(text, (x, y))

def pause():
    paused = True
    while paused:
        clock.tick(60)

        printText('PAUSED. Press ENTER to continue', 20, 200)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            paused = False

        pygame.display.update()



def checkCollision(spikes):
    for spike in spikes:
        if playerY + playerHeight >= spike.y:
            if spike.x <= playerX < spike.x + spike.width:
                return True
            elif spike.x <= playerX + playerWidth < spike.x + spike.width:
                return True
    return False

def gameOver(points):
    win.blit(pygame.image.load('sprites/oof.png'), (0, 0))
    while True:
        clock.tick(60)

        if highScore(points):
            printText('NEW BEST SCORE!!!', 80, 200, fontSize=40, fontColor=(255, 255, 0))

        printText('GAME OVER', 110, 90, fontSize=50)
        printText(('your score: ' + str(points)), 175, 150, fontSize=20)
        printText(('Best score: ' + open('highscore.txt', 'r').read()), 174, 175, fontColor=(255, 255, 0), fontSize=20)
        printText('R - restart', 185, 250, fontSize=25)
        printText('ESC - exit', 185, 275, fontSize=25)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            restart()
        elif keys[pygame.K_ESCAPE]:
            pygame.quit()

        pygame.display.update()

def moveLeft():
    global left, right, lastMove, playerX, playerSpeed
    if playerX > 5:
        left = True
        right = False
        lastMove = 'left'
        playerX -= playerSpeed

def moveRight():
    global left, right, lastMove, playerX, playerWidth, playerSpeed
    if playerX < (500 - playerWidth - 5):
        left = False
        right = True
        lastMove = 'right'
        playerX += playerSpeed

def stand():
    global left, right
    left = False
    right = False

def restart():
    global playerY, playerX, spikes, bullets
    playerX = 50
    playerY = displayHeight - 60
    runGame(points=0, spikes=[])

def highScore(points):
    if int(open('highscore.txt', 'r').read()) < points:
        file = open('highscore.txt', 'w')
        file.write(str(points))
        return True

# TODO fix collisions
# TODO add hearts as a healing
# TODO add shooting


"""""
    for bullet in bullets:
        if 0 < bullet.x < 500:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_e]:
        if lastMove == 'right':
            facing = -1
        else:
            facing = 1

        if len(bullets) < 10:
            bullets.append(Shoot(round(playerX + playerWidth // 2), round(playerY + playerHeight - 15), facing))

""" # shooting

def runGame(points=0, lives=20, spikes=[]):
    global isJump
    obstacleSpeed = 6
    run = True
    best = open('highscore.txt', 'r').read()
    while run:

        clock.tick(60)
        points += 1

        if points == 1:
            createSpikes(spikes)
        elif points == 1000:
            obstacleSpeed = 7
        elif points == 2000:
            obstacleSpeed = 8
        elif points == 3000:
            obstacleSpeed = 9
        elif points == 5000:
            obstacleSpeed = 10


        # bugfix
        if playerY > displayHeight - 60:
            restart()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            pause()

        if keys[pygame.K_a]:
            moveLeft()
        elif keys[pygame.K_d]:
            moveRight()
        else:
            stand()

        if not isJump:
            if keys[pygame.K_SPACE]:
                isJump = True
        else:
            jump()

        drawWindow()

        drawSpikes(spikes, obstacleSpeed)

        if checkCollision(spikes):
            if lives == 0:
                gameOver(points)
            else:
                win.blit(pygame.image.load('sprites/oof.png'), (0, 0))
                lives -= 1

        printText(('HP: ' + str(lives)), 0, 30, fontSize=20)
        printText(('your score: ' + str(points)), 0, 0, fontSize=20)
        printText(('best score: ' + best), 330, 0, fontSize=20)

        pygame.display.update()

if __name__ == '__main__':
    runGame()

pygame.quit()