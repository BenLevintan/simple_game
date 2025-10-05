import pygame
import sys
import random

WHITE = 255, 255, 255
BIRD_RAND_SPEED_FACTOR =  1

class Birds:
    def __init__(self, pos_x, pos_y , speed):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed = speed
        self.surface = pygame.image.load('assets/characters/birds.png').convert_alpha()
        self.surface.set_colorkey(WHITE)

    def bird_movement(self):
        self.pos_x -= self.speed + random.randint( - BIRD_RAND_SPEED_FACTOR, BIRD_RAND_SPEED_FACTOR)
        if self.pos_x < -100:
            self.pos_x = 1400 + random.randint(0, 400)
            self.pos_y = 50 + random.randint(-20, 20)

    def draw(self, screen):
        screen.blit(self.surface, (self.pos_x, self.pos_y))

SNAIL_SIZE = 50, 40

class Snail:
    def __init__(self, pos, speed):
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.speed = speed
        self.surface = pygame.image.load('assets/characters/snail.png').convert_alpha()
        self.surface = pygame.transform.scale(self.surface, SNAIL_SIZE)
        self.surface.set_colorkey(WHITE)
        self.rect = self.surface.get_rect(topleft=(self.pos_x, self.pos_y))
        self.is_jumping = True
        self.gravity = 1

    def snail_movement(self, pos):
        self.pos_x -= self.speed
        if self.pos_x < -100:
            self.pos_x = pos[0]
            self.pos_y = pos[1]   
        
        self.rect.topleft = (self.pos_x, self.pos_y)

    def draw(self, screen):
        screen.blit(self.surface, self.rect.topleft)

PLAYER_SIZE = 50, 50

class Player:
    def __init__(self, pos, speed):
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.speed = speed
        self.surface = pygame.image.load('assets/characters/main3.png').convert_alpha()
        self.surface = pygame.transform.scale(self.surface, PLAYER_SIZE)
        self.surface.set_colorkey(WHITE)
        self.surface_mirror = pygame.transform.flip(self.surface, True, False)
        self.surface_mirror.set_colorkey(WHITE)  # Set color key after flipping
        self.rect = self.surface.get_rect(topleft=(pos[0], pos[1]))
        self.is_jumping = False
        self.jump_count = 10
        self.gravity = 1
        self.face_right = True  # Initially facing right

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.gravity -= 20

    def player_movement(self, keys):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            if not self.is_jumping:
                self.jump()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.face_right = False  # Set facing left
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.face_right = True  # Set facing right

    def draw(self, screen):
        if self.face_right:
            screen.blit(self.surface, self.rect.topleft)
        else:
            screen.blit(self.surface_mirror, self.rect.topleft)