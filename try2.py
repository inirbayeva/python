Нуржан ПП КБТУ ФИТ, [12.04.21 23:44]
import pygame
import sys
from pygame.locals import *
import random
import time

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (120, 120, 150)
ORANGE = (253, 106, 2)
BGREEN = (194, 178, 128)

pygame.init()

pygame.mixer.music.load("8747401215bc7bd.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)

size = width, height = (1000, 600)
SCORE = 0
COINS = 0
SPEED = 5

screen = pygame.display.set_mode(size)
pygame.display.set_caption("TSIS 8")

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Good Game", True, BLACK)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player2.png")
        self.surf = pygame.Surface((40, 75))
        self.rect = self.surf.get_rect(center=(width/2, 520))

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 190:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < width - 190:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy2.png")
        self.surf = pygame.Surface((42, 70))
        self.rect = self.surf.get_rect(center=(random.randint(240, width-240), 0))
        self.speed = random.randint(1,5)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED+self.speed)
        if self.rect.top > height:
            SCORE += 1
            self.rect.bottom = 0
            self.speed = random.randint(1, 5)
            self.rect.left = random.randint(200, width-242)

class Coins(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Coin.png")
        self.surf = pygame.Surface((42, 42))
        self.rect = self.surf.get_rect(center=(random.randint(221, width-221), 0))

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > height:
            self.rect.bottom = 0
            self.rect.left = random.randint(200, width-242)

class Track1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("track2.png")
        self.surf = pygame.Surface((20, 60))
        self.y1 = (0, 120, 240, 360, 480, 600)
        self.y = list(self.y1)
        self.rect1 = self.surf.get_rect(center=(390, 0))
        self.rect2 = self.surf.get_rect(center=(390, 120))
        self.rect3 = self.surf.get_rect(center=(390, 240))
        self.rect4 = self.surf.get_rect(center=(390, 360))
        self.rect5 = self.surf.get_rect(center=(390, 480))
        self.rect6 = self.surf.get_rect(center=(390, 600))

    def move(self):
        if self.rect1.top > height:
            self.rect1.top = -120
        self.rect1.move_ip(0, SPEED)

        if self.rect2.top > height:
            self.rect2.top = -120
        self.rect2.move_ip(0, SPEED)

        if self.rect3.top > height:
            self.rect3.top = -120
        self.rect3.move_ip(0, SPEED)

        if self.rect4.top > height:
            self.rect4.top = -120
        self.rect4.move_ip(0, SPEED)

        if self.rect5.top > height:
            self.rect5.top = -120
        self.rect5.move_ip(0, SPEED)

        if self.rect6.top > height:
            self.rect6.top = -120
        self.rect6.move_ip(0, SPEED)

Нуржан ПП КБТУ ФИТ, [12.04.21 23:44]


class Track2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("track2.png")
        self.surf = pygame.Surface((20, 60))
        self.y1 = (0, 120, 240, 360, 480, 600)
        self.y = list(self.y1)
        self.rect1 = self.surf.get_rect(center=(590, 0))
        self.rect2 = self.surf.get_rect(center=(590, 120))
        self.rect3 = self.surf.get_rect(center=(590, 240))
        self.rect4 = self.surf.get_rect(center=(590, 360))
        self.rect5 = self.surf.get_rect(center=(590, 480))
        self.rect6 = self.surf.get_rect(center=(590, 600))

    def move(self):
        if self.rect1.top > height:
            self.rect1.top = -120
        self.rect1.move_ip(0, SPEED)

        if self.rect2.top > height:
            self.rect2.top = -120
        self.rect2.move_ip(0, SPEED)

        if self.rect3.top > height:
            self.rect3.top = -120
        self.rect3.move_ip(0, SPEED)

        if self.rect4.top > height:
            self.rect4.top = -120
        self.rect4.move_ip(0, SPEED)

        if self.rect5.top > height:
            self.rect5.top = -120
        self.rect5.move_ip(0, SPEED)

        if self.rect6.top > height:
            self.rect6.top = -120
        self.rect6.move_ip(0, SPEED)

class Green1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        if random.randint(1, 10)!=2:
            self.image = pygame.image.load("tree2.png")
        else:
            self.image = pygame.image.load("tree3.png")
        self.surf = pygame.Surface((100, 100))
        self.rect = self.surf.get_rect(center=(random.randint(50, 150), 0))

    def move(self):
        self.rect.move_ip(0, SPEED)

class Green2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        if random.randint(1, 10) != 2:
            self.image = pygame.image.load("tree2.png")
        else:
            self.image = pygame.image.load("tree3.png")
        self.surf = pygame.Surface((100, 100))
        self.rect = self.surf.get_rect(center=(random.randint(850, 950), 0))

    def move(self):
        self.rect.move_ip(0, SPEED)

fps = pygame.time.Clock()
ran = random.randint(0, 100)

T1 = Track1()
T2 = Track2()
P = Player()
E = Enemy()
C = Coins()
G11 = Green1()
G21 = Green2()
tracks1 = pygame.sprite.Group()
tracks1.add(T1)
tracks2 = pygame.sprite.Group()
tracks2.add(T2)
enemies = pygame.sprite.Group()
enemies.add(E)

all_sprites = pygame.sprite.Group()
all_sprites.add(P)
all_sprites.add(E)

greens = pygame.sprite.Group()
greens.add(G11)
greens.add(G21)
coins = pygame.sprite.Group()
coins.add(C)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while True:
    for events in pygame.event.get():
        if events.type == QUIT:
            pygame.quit()
            sys.exit()
        if events.type == INC_SPEED:
            SPEED += 0.3

    screen.fill(GRAY)
    pygame.draw.rect(screen, ORANGE, (210, 0, 2, height))
    pygame.draw.rect(screen, ORANGE, (790, 0, 2, height))
    pygame.draw.rect(screen, BGREEN, (0, 0, 200, height))
    pygame.draw.rect(screen, BGREEN, (800, 0, 200, height))

    if random.randint(1,50) == 2:
        G1 = Green1()
        G2 = Green2()
        greens.add(G1)
        greens.add(G2)

    for i in greens:
        screen.blit(i.image, i.rect)
        i.move()

    for i in tracks1:
        screen.blit(i.image, i.rect1)
        screen.blit(i.image, i.rect2)
        screen.blit(i.image, i.rect3)
        screen.blit(i.image, i.rect4)
        screen.blit(i.image, i.rect5)
        screen.blit(i.image, i.rect6)
        i.move()

    for i in tracks2:
        screen.blit(i.image, i.rect1)
        screen.blit(i.image, i.rect2)
        screen.blit(i.image, i.rect3)
        screen.blit(i.image, i.rect4)
        screen.blit(i.image, i.rect5)
        screen.blit(i.image, i.rect6)
        i.move()

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

Нуржан ПП КБТУ ФИТ, [12.04.21 23:44]


    if ran == 2:
        for c in coins:
            screen.blit(c.image, c.rect)
            c.move()
            if c.rect.bottom > 594:
                ran = 0
    else:
        ran = random.randint(0, 100)

    if pygame.sprite.spritecollideany(P, coins):
        pygame.mixer.Sound('Sound_19349.mp3').play()
        pygame.mixer.music.set_volume(1.5)
        for c in coins:
            c.rect.top = 0
            c.rect.left = random.randint(200, width-242)
            ran = 0
        COINS += 1

    if pygame.sprite.spritecollideany(P, enemies):
        pygame.mixer.music.stop()
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(1)

        screen.fill(GREEN)
        screen.blit(pygame.image.load("game_over.png"), (0, 0))

        co = font_small.render("COINS:" + str(COINS), True, BLACK)
        sc = font_small.render("SCORE:" + str(SCORE), True, BLACK)
        screen.blit(co, (30, 30))
        screen.blit(sc, (30, 70))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(3)
        pygame.quit()
        sys.exit()

    co = font_small.render("COINS:" + str(COINS), True, BLACK)
    sc = font_small.render("SCORE:" + str(SCORE), True, BLACK)
    screen.blit(co, (10, 10))
    screen.blit(sc, (width - 120, 10))
    pygame.display.flip()
    fps.tick(60)

pygame.quit()