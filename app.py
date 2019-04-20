import pygame
from pygame.locals import *
from random import *

pygame.display.init()  # Initialize display module
screen = pygame.display.set_mode([500, 600], 0, 32)  # Setup window size to display
screen.fill((0, 0, 0))  # Fill the screen with a default color - temporary
clock = pygame.time.Clock()  # Instantiating clock from framework

moveForce = 5

player_x_position = 250
player_y_position = 500

counter = 5

class Enemy():
    def __init__(self, x=0, y=0):
        self.x_position = x
        self.y_position = y
        self.rect = pygame.rect.Rect((x, y, 16, 16))

    def draw(self):
        pygame.draw.rect(screen, (83, 66, 244), self.rect)

    def destroy(self):
        self.rect = pygame.rect.Rect((0, 0, 0, 0))

    def update_position(self):
        self.y_position += 2
        self.rect = pygame.rect.Rect((self.x_position, self.y_position, 16, 16))

enemies = []

class Shot():
    def __init__(self, x=0, y=0):
        self.isShot = False
        self.x_position = x
        self.y_position = y
        self.rect = pygame.rect.Rect((x, y, 16, 16))

    def draw(self):
        pygame.draw.rect(screen, (86, 244, 66), self.rect)

    def update_position(self):
        self.y_position -= 5
        self.rect = pygame.rect.Rect((self.x_position, self.y_position, 16, 16))

            
shots = []

# Updating function
while True:
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), pygame.rect.Rect((player_x_position, player_y_position, 16, 16)))

    if counter >= 5:
        enemies.append(Enemy(randint(0, 500), 0))
        enemies[-1].update_position()
        enemies[-1].draw()
        print('heeeey')
        counter = 0

    counter += clock.get_time()/1000

    # just to trigger input from keyboard
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                shots.append(Shot(player_x_position, player_y_position - 30))
                print('space')

    key = pygame.key.get_pressed()

    if key[pygame.K_d]:
        player_x_position += moveForce
        print('d')
    if key[pygame.K_w]:
        player_y_position -= moveForce
        print('w')
    if key[pygame.K_a]:
        player_x_position -= moveForce
        print('a')
    if key[pygame.K_s]:
        player_y_position += moveForce
        print('s')

    for shot in shots:
        shot.update_position()
        shot.draw()
        if shot.rect.collidelist(enemies) != -1:
            enemies[shot.rect.collidelist(enemies)].destroy()
            enemies.remove(enemies[shot.rect.collidelist(enemies)])

    for enemy in enemies:
        enemy.update_position()
        enemy.draw()
    

    pygame.display.flip()  # Updating frame
    clock.tick_busy_loop(30)  # Framerate clock

    