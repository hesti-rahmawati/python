import sys
import random

import pygame
from pygame.locals import *

pygame.init()

'''IMAGES'''

player_ship = 'plyship.png'
enemy_ship = 'enemyship.png'
ufo_ship = 'ufo.png'
player_bullet ='pbullet.png'


screen = pygame.display.set_mode((0,0),FULLSCREEN)
s_width,s_height = screen.get_size()
clock = pygame.time.Clock()
FPS =60

background_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
ufo_group = pygame.sprite.Group()
player_bullet = pygame.sprite.Group()

sprite_group = pygame.sprite.Group()

class Background(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()

        self.image = pygame.Surface([x,y])
        self.image.fill('white')
        self.image.set_colorkey('black')
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y +=1
        self.rect.x +=1
        if self.rect.y >s_height:
            self.rect.y = random.randrange(-10,0)
            self.rect.x = random.randrange(-400,s_width)

class player(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image = pygame.image.load("images/plyship.png")
        self.rect = self.image.get_rect()
        self.image.set_colorkey('black')
    def update(self):
        mouse = pygame.mouse.get_pos()
        self.rect.x = mouse[0]
        self.rect.y = mouse[1]

    def shoot(self):
        bullet = PlayerBullet(player_bullet)
        mouse =pygame.mouse.get_pos()
        bullet.rect.x = mouse[0]
        bullet.rect.y = mouse[1]
        player_group.add(bullet)
        sprite_group.add(bullet)



class Enemy(player):
    def __init__(self,img):
        super().__init__(img)
        self.rect.x = random.randrange(0,s_width)
        self.rect.y = random.randrange(-500,0)
        screen.blit(self.image,(self.rect.x,self.rect.y))

    def update(self):
        self.rect.y += 1
        if self.rect.y > s_height:
            self.rect.x = random.randrange(0,s_width)
            self.rect.y = random.randrange(-2000,0)

class Ufo(Enemy):
    def __init__(self,img):
        super().__init__(img)
        self.rect.x =-200
        self.rect.y = 200
        self.move = 1
    
    def update(self):
        self.rect.x += self.move
        if self.rect.x >s_width +200:
            self.move *= -1
        elif self.rect.x < -200:
            self.move *= -1

class PlayerBullet(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.imaage.set_coorkey('black')

    def update(self):
        self.rect.y -= 5
        if self.rect.y <0:
            self.kill()


class Game:
    def __init__(self):
        self.run_game()

    def create_background(self):
        for i in range(20):
            x = random.randint(1,9)
            background_image = Background(x,x)
            background_image.rect.x = random.randrange(0,s_width)
            background_image.rect.x = random.randrange(0,s_height)
            background_group.add(background_image)
            sprite_group.add(background_image)
    
    def create_player(self):
        self.player = player(player_ship)
        player_group.add(self.player)
        sprite_group.add(self.player)

    def create_enemy(self):
        for i in range(10):
            self.enemy = Enemy(enemy_ship)
            sprite_group.add(self.enemy)
            sprite_group.add(self.enemy)

    def create_ufo(self):
        for i in range(1):
            self.ufo = Ufo(ufo_ship)
            ufo_group.add(self.ufo)
            sprite_group.update()


    def run_update(self):
        sprite_group.draw(screen)
        sprite_group.update()



    def run_game(self):
        self.create_background()
        self.create_player()
        self.create_enemy()
        self.create_ufo()
        while True:
            screen.fill('black')
            self.run_update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    self.player.shoot()
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            pygame.display.update()
            clock.tick(FPS)
def main():
    game =Game()

if __name__=='__main__':
    main()
