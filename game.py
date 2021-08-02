import pygame
import random

pygame.init()
display_width = 1000
display_height = 500
win = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('POOPRUN')

clock = pygame.time.Clock()
FPS = 60

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
walk_right = [_.convert() for _ in walk_right]

walk_left = [pygame.image.load('sprites/left (4).png'),
             pygame.image.load('sprites/left (5).png'), pygame.image.load('sprites/left (6).png'), pygame.image.load('sprites/left (7).png'), pygame.image.load('sprites/left (8).png'),
             pygame.image.load('sprites/left (9).png'), pygame.image.load('sprites/left (10).png'), pygame.image.load('sprites/left (11).png'), pygame.image.load('sprites/left (12).png'),
             pygame.image.load('sprites/left (13).png'), pygame.image.load('sprites/left (14).png'), pygame.image.load('sprites/left (15).png')]
walk_left = [_.convert() for _ in walk_left]

player_stand = [pygame.image.load('sprites/front (1).png'), pygame.image.load('sprites/front (2).png'), pygame.image.load('sprites/front (3).png'),
                pygame.image.load('sprites/front (4).png'), pygame.image.load('sprites/front (5).png')]
player_stand = [_.convert() for _ in player_stand]

fire1 = [pygame.image.load('sprites/fire1.png'), pygame.image.load('sprites/fire2.png'), pygame.image.load('sprites/fire3.png'), pygame.image.load('sprites/fire4.png'),
         pygame.image.load('sprites/fire5.png'), pygame.image.load('sprites/fire5.png'), pygame.image.load('sprites/fire4.png'), pygame.image.load('sprites/fire3.png'),
         pygame.image.load('sprites/fire2.png'), pygame.image.load('sprites/fire1.png')]
#fire1 = [_.convert() for _ in fire1]

fire2 = [pygame.image.load('sprites/fire11.png'), pygame.image.load('sprites/fire22.png'), pygame.image.load('sprites/fire33.png'), pygame.image.load('sprites/fire44.png'),
         pygame.image.load('sprites/fire55.png'), pygame.image.load('sprites/fire55.png'), pygame.image.load('sprites/fire44.png'), pygame.image.load('sprites/fire33.png'),
         pygame.image.load('sprites/fire22.png'), pygame.image.load('sprites/fire11.png')]
#fire2 = [_.convert() for _ in fire2]

fire3 = [pygame.image.load('sprites/fire111.png'), pygame.image.load('sprites/fire222.png'), pygame.image.load('sprites/fire333.png'), pygame.image.load('sprites/fire444.png'),
         pygame.image.load('sprites/fire555.png'), pygame.image.load('sprites/fire555.png'), pygame.image.load('sprites/fire444.png'), pygame.image.load('sprites/fire333.png'),
         pygame.image.load('sprites/fire222.png'), pygame.image.load('sprites/fire111.png')]
#fire3 = [_.convert() for _ in fire3]

"""background = [pygame.image.load('sprites/background1.png'), pygame.image.load('sprites/background2.png'), pygame.image.load('sprites/background3.png'),
              pygame.image.load('sprites/background4.png'), pygame.image.load('sprites/background5.png'), pygame.image.load('sprites/background6.png'),
              pygame.image.load('sprites/background7.png'), pygame.image.load('sprites/background8.png'), pygame.image.load('sprites/background7.png'),
              pygame.image.load('sprites/background6.png'), pygame.image.load('sprites/background5.png'), pygame.image.load('sprites/background4.png'),
              pygame.image.load('sprites/background3.png'), pygame.image.load('sprites/background2.png'), pygame.image.load('sprites/background1.png')]
background = [_.convert() for _ in background]"""


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


class Button:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.inactive_color = (120, 25, 25)
        self.active_color = (160, 25, 25)
        self.outline_color = (200, 25, 25)

    def draw(self, x, y, message, action=None):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse_x < x + self.width and y < mouse_y < y + self.height:
            pygame.draw.rect(win, self.active_color, (x, y, self.width, self.height))
            pygame.draw.rect(win, self.outline_color, (x, y, self.width, self.height), 2)

            if click[0] == 1:
                if action == 'continue':
                    return False
                elif action is not None:
                    action()
        else:
            pygame.draw.rect(win, self.inactive_color, (x, y, self.width, self.height))
            pygame.draw.rect(win, self.outline_color, (x, y, self.width, self.height), 2)

        print_text(message, x + (self.width - (len(message)/2 * (self.height - 10)) - 10)//2, y + 5, font_size=self.height - 10)

def choice():
    check = random.randint(0, 5)
    if check == 0:
        return True
    else:
        return False


def start_menu():
    menu = True
    while menu:
        clock.tick(FPS)
        win.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        button = Button(300, 60)
        button.draw((display_width - button.width)//2, 150, 'PLAY', restart)
        button.draw((display_width - button.width)//2, 300, 'EXIT', pygame.quit)

        pygame.display.update()


def draw_window(spikes, heart, obstacle_speed):
    global anim_count, FPS
    win.fill((30, 0, 0))
    pygame.draw.rect(win, (50, 0, 0), (0, 480, 1000, 20))

    if anim_count + 1 >= 60:
        anim_count = 0

    if left:
        win.blit(walk_left[anim_count // (FPS//12)], (player_x, player_y))
        anim_count += 1
    elif right:
        win.blit(walk_right[anim_count // (FPS//12)], (player_x, player_y))
        anim_count += 1
    else:
        win.blit(player_stand[anim_count // (FPS//5)], (player_x, player_y))
        anim_count += 1

    draw_spikes(spikes, obstacle_speed)
    draw_hearts(heart, obstacle_speed)


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


def create_spikes(spikes, x=1000):
    spikes.append(Object(x + 100, display_height - 90, 30, 80))
    spikes.append(Object(x + 300, display_height - 60, 40, 50))
    spikes.append(Object(x + 550, display_height - 75, 50, 65))


def draw_spikes(spikes, speed=6):
    global anim_count, FPS
    for spike in spikes:
        if spike.width == 30:
            win.blit(fire1[anim_count // (FPS//10)], (spike.x, spike.y))
        elif spike.width == 40:
            win.blit(fire2[anim_count // (FPS//10)], (spike.x, spike.y))
        elif spike.width == 50:
            win.blit(fire3[anim_count // (FPS//10)], (spike.x, spike.y))
        spike.move(speed)


def draw_hearts(heart, speed=5):
    win.blit(pygame.image.load('sprites/heart.png'), (heart.x, heart.y))
    heart.move(speed)


def print_text(message, x, y, font_color=(255, 255, 255), font='21002.ttf', font_size=30):
    font = pygame.font.Font(font, font_size)
    text = font.render(message, True, font_color)
    win.blit(font.render(message, True, (0, 0, 0)), (x + 2, y + 2))
    win.blit(text, (x, y))


def pause():
    paused = True
    while paused:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        button = Button(400, 40)
        button.draw((display_width - button.width)//2, 150, 'CONTINUE')
        button.draw((display_width - button.width)//2, 200, 'RESTART', restart)
        button.draw((display_width - button.width)//2, 250, 'MAIN MENU', start_menu)
        button.draw((display_width - button.width)//2, 300, 'EXIT', pygame.quit)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            paused = False

        pygame.display.update()


def check_collision(object, x, y, width, height):
    player = pygame.Rect(x, y, width, height)
    obstacle = pygame.Rect(object.x, object.y, object.width, object.height)
    return player.colliderect(obstacle)


def game_over(points):
    win.blit(pygame.image.load('sprites/oof.png'), (0, 0))
    while True:
        clock.tick(FPS)

        if high_score(points):
            print_text('NEW BEST SCORE!!!', display_width // 4 + 80, 200, font_size=40, font_color=(255, 255, 0))

        print_text('GAME OVER', display_width // 4 + 110, 90, font_size=50)
        print_text(('your score: ' + str(points)), display_width // 4 + 175, 150, font_size=20)
        print_text(('Best score: ' + open('highscore.txt', 'r').read()), display_width // 4 + 174, 175, font_color=(255, 255, 0), font_size=20)

        button = Button(400, 40)
        button.draw((display_width - button.width)//2, 250, 'RESTART', restart)
        button.draw((display_width - button.width)//2, 300, 'MAIN MENU', start_menu)
        button.draw((display_width - button.width)//2, 350, 'EXIT', pygame.quit)

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
    if player_x < (display_width - player_width - 5):
        left = False
        right = True
        last_move = 'right'
        player_x += player_speed


def stand():
    global left, right
    left = False
    right = False


def restart():
    global player_y, player_x
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


def run_game(points=0, hp=20, spikes=[], heart=Object(1500, display_height - 250, 30, 30), max_hp=40):
    global is_jump
    obstacle_speed = 6
    run = True
    best = open('highscore.txt', 'r').read()
    create_spikes(spikes)
    heart_rate = 5000
    while run:

        player = (player_x, player_y, player_width, player_height)
        clock.tick(FPS)
        points += 1

        if points % 1000 == 0:
            heart_rate += 1000
            obstacle_speed += 1
        elif points % 3001 == 0:
            index = random.randint(0, 2)
            width = [30, 40, 50]
            height = [80, 50, 65]
            spikes.append(Object(1000 + random.randint(100, 1000),
                                 display_height - height[index] - 10, width[index], height[index]))

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

        if check_collision(heart, *player):
            if hp <= max_hp - 3:
                hp += 3
            else:
                hp = 40
            # spawning heart again after eating
            heart = Object(random.randrange(heart_rate - 3000, heart_rate), display_height - 250, 30, 30)

        draw_window(spikes, heart, obstacle_speed)

        for spike in spikes:
            if check_collision(spike, *player):
                if hp <= 0:
                    game_over(points)
                else:
                    win.blit(pygame.image.load('sprites/oof.png'), (0, 0))
                    hp -= 1

        pygame.draw.rect(win, (0, 0, 0), (35, 30, 160, 25))
        pygame.draw.rect(win, (255, 255, 255), (35, 30, hp * 4, 25))
        print_text('HP', 0, 30, font_size=20)
        print_text(('your score: ' + str(points)), 0, 0, font_size=20)
        print_text(('best score: ' + best), display_width - 170, 0, font_size=20)

        pygame.display.update()


if __name__ == '__main__':
    start_menu()

pygame.quit()

# TODO add shooting
# TODO добавить лужи которые замедляют
# TODO добавить что-то на потолке, что дамажит
# TODO добавить врагов
