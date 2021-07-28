import pygame
import random

pygame.init()
display_width = 500
display_height = 500
win = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('POOPRUN')

clock = pygame.time.Clock()

player_x = 50
player_y = display_height - 60
player_width = 50
player_height = 50
player_speed = 5

bullets = []

is_jump = False
jump_count = 10

left = False
right = False
anim_count = 0
last_move = 'right'

walk_right = [pygame.image.load('sprites/right (4).png'),
              pygame.image.load('sprites/right (5).png'), pygame.image.load('sprites/right (6).png'), pygame.image.load('sprites/right (7).png'), pygame.image.load('sprites/right (8).png'),
              pygame.image.load('sprites/right (9).png'), pygame.image.load('sprites/right (10).png'), pygame.image.load('sprites/right (11).png'), pygame.image.load('sprites/right (12).png'),
              pygame.image.load('sprites/right (13).png'), pygame.image.load('sprites/right (14).png'), pygame.image.load('sprites/right (15).png')]

walk_left = [pygame.image.load('sprites/left (4).png'),
             pygame.image.load('sprites/left (5).png'), pygame.image.load('sprites/left (6).png'), pygame.image.load('sprites/left (7).png'), pygame.image.load('sprites/left (8).png'),
             pygame.image.load('sprites/left (9).png'), pygame.image.load('sprites/left (10).png'), pygame.image.load('sprites/left (11).png'), pygame.image.load('sprites/left (12).png'),
             pygame.image.load('sprites/left (13).png'), pygame.image.load('sprites/left (14).png'), pygame.image.load('sprites/left (15).png')]

player_stand = [pygame.image.load('sprites/front (1).png'), pygame.image.load('sprites/front (2).png'), pygame.image.load('sprites/front (3).png'),
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


class Object:
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
                self.x = display_width + 50 + random.randrange(0, 50)
            else:
                self.x = display_width + random.randrange(100, 300)


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


def draw_window():
    global anim_count
    win.fill((0, 0, 0))

    # win.blit(background, (0, 0)) - for background

    if anim_count + 1 >= 60:
        anim_count = 0

    if left:
        win.blit(walk_left[anim_count // 5], (player_x, player_y))
        anim_count += 1
    elif right:
        win.blit(walk_right[anim_count // 5], (player_x, player_y))
        anim_count += 1
    else:
        win.blit(player_stand[anim_count // 12], (player_x, player_y))
        anim_count += 1

    for bullet in bullets:
        bullet.draw(win)


def jump():
    global player_y, jump_count, is_jump

    if jump_count >= -10:
        if jump_count < 0:
            player_y += (jump_count ** 2) // 1.5
        else:
            player_y -= (jump_count ** 2) // 1.5
        jump_count -= 1
    else:
        is_jump = False
        jump_count = 10

# def shooting(bullets)


def create_spikes(spikes, x=500):
    spikes.append(Object(x + 100, display_height - 90, 30, 80))
    spikes.append(Object(x + 300, display_height - 60, 40, 50))
    spikes.append(Object(x + 550, display_height - 75, 50, 65))


def draw_spikes(spikes, speed=6):
    global anim_count
    for spike in spikes:
        if spike.width == 30:
            win.blit(fire1[anim_count // 6], (spike.x, spike.y))
        elif spike.width == 40:
            win.blit(fire2[anim_count // 6], (spike.x, spike.y))
        elif spike.width == 50:
            win.blit(fire3[anim_count // 6], (spike.x, spike.y))
        spike.move(speed)


def draw_hearts(heart, speed=5):
    win.blit(pygame.image.load('sprites/heart.png'), (heart.x, heart.y))
    heart.move(speed)


def print_text(message, x, y, font_color=(255, 255, 255), font='21002.ttf', font_size=30):
    font = pygame.font.Font(font, font_size)
    text = font.render(message, True, font_color)
    win.blit(text, (x, y))


def pause():
    paused = True
    while paused:
        clock.tick(60)

        print_text('PAUSED. Press ENTER to continue', 20, 200)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            paused = False

        pygame.display.update()


def check_collision(array):
    for i in array:
        if player_y + player_height >= i.y:
            if i.x <= player_x < i.x + i.width:
                return True
            elif i.x <= player_x + player_width < i.x + i.width:
                return True
    return False


def game_over(points):
    win.blit(pygame.image.load('sprites/oof.png'), (0, 0))
    while True:
        clock.tick(60)

        if high_score(points):
            print_text('NEW BEST SCORE!!!', 80, 200, font_size=40, font_color=(255, 255, 0))

        print_text('GAME OVER', 110, 90, font_size=50)
        print_text(('your score: ' + str(points)), 175, 150, font_size=20)
        print_text(('Best score: ' + open('highscore.txt', 'r').read()), 174, 175, font_color=(255, 255, 0), font_size=20)
        print_text('R - restart', 185, 250, font_size=25)
        print_text('ESC - exit', 185, 275, font_size=25)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            restart()
        elif keys[pygame.K_ESCAPE]:
            pygame.quit()

        pygame.display.update()


def move_left():
    global left, right, last_move, player_x, player_speed
    if player_x > 5:
        left = True
        right = False
        last_move = 'left'
        player_x -= player_speed


def move_right():
    global left, right, last_move, player_x, player_width, player_speed
    if player_x < (500 - player_width - 5):
        left = False
        right = True
        last_move = 'right'
        player_x += player_speed


def stand():
    global left, right
    left = False
    right = False


def restart():
    global player_y, player_x, spikes, bullets
    player_x = 50
    player_y = display_height - 60
    run_game(points=0, spikes=[])


def high_score(points):
    if int(open('highscore.txt', 'r').read()) < points:
        file = open('highscore.txt', 'w')
        file.write(str(points))
        return True

# shooting
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

"""


def run_game(points=0, lives=20, spikes=[], heart=Object(1500, 200, 30, 30)):
    global is_jump
    obstacle_speed = 6
    run = True
    best = open('highscore.txt', 'r').read()
    while run:

        clock.tick(60)
        points += 1

        if points == 1:
            create_spikes(spikes)
        elif points % 1000 == 0:
            obstacle_speed += 1

        # bugfix
        if player_y > display_height - 60:
            restart()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            pause()

        if keys[pygame.K_a]:
            move_left()
        elif keys[pygame.K_d]:
            move_right()
        else:
            stand()

        if not is_jump:
            if keys[pygame.K_SPACE]:
                is_jump = True
        else:
            jump()

        draw_window()

        draw_spikes(spikes, obstacle_speed)
        draw_hearts(heart, obstacle_speed)

        if check_collision([heart]) and is_jump:
            lives += 3
            heart = Object(random.randrange(2000, 5000), 200, 30, 30)

        if check_collision(spikes):
            if lives <= 0:
                game_over(points)
            else:
                win.blit(pygame.image.load('sprites/oof.png'), (0, 0))
                lives -= 1

        print_text(('HP: ' + str(lives)), 0, 30, font_size=20)
        print_text(('your score: ' + str(points)), 0, 0, font_size=20)
        print_text(('best score: ' + best), display_width - 170, 0, font_size=20)

        pygame.display.update()


if __name__ == '__main__':
    run_game()

pygame.quit()

# TODO add hearts as a healing
# TODO add shooting